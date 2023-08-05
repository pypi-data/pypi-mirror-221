"""
The live editor provides the documentation preview functionality and the live editing
functionality of the GitBuilding Server. When using `gitbuilding serve` all endpoints
will be forwarded to this module. When using `gitbuilding webapp` this module handleds
the functionality of each launched editor.
"""

import os
import posixpath
import logging
import urllib
from copy import deepcopy
from uuid import uuid4 as uuid
import flask
from flask import request, jsonify
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from gitbuilding import utilities
from gitbuilding import example
from gitbuilding.buildup import Documentation, read_directory, read_external_directories, FileInfo
from gitbuilding.buildup.page import Page
from gitbuilding.buildup.parts import UsedPart
from gitbuilding.buildup.files import is_filepath_safe
from gitbuilding.buildup.utilities import as_posix
from gitbuilding import render
from gitbuilding.server_utils import GBWebPath, DroppedFiles
from gitbuilding.previewers import gitbuilding_previewers
from gitbuilding.config import load_config_from_file, get_raw_config_data, check_config_string
from gitbuilding.native_file_operations import (GBPATH,
                                                TMPDIR,
                                                localise,
                                                is_local_file,
                                                make_dir_if_needed,
                                                as_native_path,
                                                write_local_file,
                                                create_zip,
                                                copy_local_files,
                                                make_dir_if_needed_abs)

_LOGGER = logging.getLogger('BuildUp.GitBuilding')


class WatchdogHandler(FileSystemEventHandler):
    """
    This is a watchdog that checks if any files in the working directory are modified
    If the are self.on_any_event() is executed. This will descide if to rebuild the
    documentation.
    """
    def __init__(self, editor, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._editor = editor

    def on_any_event(self, event):
        """
        This will run on any file system event. If a file has been modified the
        documentation will be set to rebuild
        """
        if event.is_directory:
            return
        if event.event_type == 'closed':
            # Seems mad but closed it called on each modification,
            # modified is called twice and is annoying to deduplicate
            path = os.path.relpath(event.src_path, self._editor.working_dir)
            if path.endswith(('.md', '.yml', '.yaml')):
                print(f"File {path} modified. Rebuilding docs!")
                self._editor.rebuild_docs(total_rebuild=True)

class LiveEditor():
    """
    This is the live editor for a single document. Live editors are created and tracked by
    sever.LiveEditorManager. LiveEditorManager creates the URL rules and forwards the endpoints
    to the correct LiveEditor. This LiveEditor is responsible for serving a preview of the
    documentation as well as editing features.
    """

    def __init__(self, working_dir, url_prefix, handler):

        self._url_prefix = url_prefix
        self._building = True
        rules = render.URLRulesHTML()
        self._handler = handler
        log_length = self._handler.log_length
        self._working_dir = working_dir

        # Setup watchdog for external changes
        event_handler = WatchdogHandler(self)
        self._observer = Observer()
        self._observer.schedule(event_handler, self._working_dir, recursive = True)
        self._observer.start()

        self._config_file = 'buildconf.yaml'
        configuration = load_config_from_file(self._config_file, self._working_dir)
        configuration.remove_landing_title = True
        self._license_file = utilities.handle_licenses(configuration)
        self.doc = Documentation(configuration, self._working_dir, rules, gitbuilding_previewers())
        file_list = read_directory(self._working_dir,
                                   include_list=['static/Icons/info.png'],
                                   exclude_list=configuration.exclude)
        if self._license_file is not None:
            file_list.append(self._license_file)
        external_files = read_external_directories(configuration.external_dirs,
                                                   exclude_list=configuration.exclude)
        self.doc.buildall(file_list, external_files)
        self._read_config()
        self._global_log = self._handler.log_from(log_length)

        # Two render objects, one for static one for live
        self.renderer = render.GBRenderer(self._working_dir, self._config, rules, static=False)
        self.renderer.set_warning_count(self._global_log)
        # The live renderer shows the static rendering as static=False
        # is used show the header buttons.
        self.live_renderer = render.GBRenderer(self._working_dir, deepcopy(self._config), rules)
        self._unsaved_dropped_files = DroppedFiles()
        self._building = False

    @property
    def working_dir(self):
        """Return the working directory of the editor"""
        return self._working_dir

    def _read_config(self):
        """
        Reads the project data generated when converting BuildUp to markdown
        """
        self._config = self.doc.config

    def _get_docpage(self, path):
        """
        Gets a Page object from the Documentation object
        """
        if path.gb_path_deduplicated in self.doc.pages:
            return self.doc.get_page_by_path(path.gb_path_deduplicated)

        file_obj = FileInfo(path.gb_path, dynamic_content=True, content='# Empty page\n\nEdit me')
        return Page(file_obj, self.doc)

    def raw_md(self, rawsubpath=None):
        """
        Get the raw markdown for pages in the documentation
        Returns this in JSON
        """

        path = GBWebPath(rawsubpath, self.doc)

        page = self._get_docpage(path)
        md = ""
        included_by = []
        if page is not None:
            md = page.get_raw()
            if page.included_by:
                # Note that page.included_bywill only show the pages that include it,
                # but will miss duplicates
                for file_obj in self.doc.output_files:
                    if rawsubpath in file_obj.includes:
                        included_by.append(file_obj.path)

        #Warn in live editor about duplicated pages.
        duplicated_by = []
        if path.gb_path_deduplicated in self.doc.page_order.duplicates:
            duplicates = self.doc.page_order.duplicates[path.gb_path_deduplicated]
            for duplicate in duplicates:
                duplicate_path = GBWebPath(duplicate.root, self.doc)
                duplicated_by.append(self._get_docpage(duplicate_path).title)

        # return the markdown
        if rawsubpath is None:
            return jsonify({"md": md})
        return jsonify({"md": md,
                        "page": rawsubpath,
                        "duplicated_by": duplicated_by,
                        "included_by": included_by})

    def part_list(self, rawsubpath=None):
        partlist = []
        path = GBWebPath(rawsubpath, self.doc)
        page = self._get_docpage(path)
        path_deduplicated = path.gb_path_deduplicated

        for part in self.doc.global_partlist:
            on_page=False
            if part in page.part_list:
                page_part = page.part_list[page.part_list.index(part)]
                if isinstance(page_part, UsedPart):
                    on_page=True
            partlist.append({"name": part.name,
                             "link": part.link_needed_on_page(path_deduplicated),
                             "category": part.category,
                             "onPage": on_page})
        partlist.sort(key=lambda part: part["name"].lower())
        for i, part in enumerate(partlist):
            part["id"] = i+1
        return jsonify({"partlist": partlist})

    def save_edit(self, rawsubpath=None):
        """
        Saves the edits from the live editor and full rebuilds the documentation
        """

        path = GBWebPath(rawsubpath, self.doc)

        #Get the JSON from the request
        content = request.get_json()

        if content["md"] is None:
            return jsonify({"saved": False})

        self._save_uploaded_files(content)
        saved = self._save_page(path, content["md"])
        if saved:
            self.rebuild_docs()
        return jsonify({"saved": saved})

    def _save_uploaded_files(self, content):
        """
        Save each uploaded file listed in the json request if they are used in the markdown
        """
        for uploaded_file in content["uploadedFiles"]:
            # Check if file is still there. It may already have been removed
            # if multiple copies of the same file were dropped.
            if self._unsaved_dropped_files.contains(uploaded_file):
                if uploaded_file in content["md"]:
                    try:
                        make_dir_if_needed(uploaded_file, self._working_dir, isfile=True)
                        copy_local_files(self._unsaved_dropped_files.get(uploaded_file),
                                         uploaded_file,
                                         self._working_dir,
                                         force_relative=False)
                    except FileNotFoundError:
                        _LOGGER.warning("Uploaded file %s may have been deleted",
                                        uploaded_file)
                    #Only remove if copied as multiple editors could have added same file
                    self._unsaved_dropped_files.remove(uploaded_file)

    def _save_page(self, path, md):

        if path.gb_path is None:
            return False

        save_path = path.gb_path_deduplicated
        make_dir_if_needed(save_path, self._working_dir, isfile=True)
        try:
            write_local_file(save_path, self._working_dir, md)
            return True
        except IOError:
            return False

    def _save_config_file(self, yaml):
        try:
            write_local_file(self._config_file, self._working_dir, yaml)
            return True
        except IOError:
            return False

    def create_homepage(self):
        """
        Create a dummy homepage. The link to this endpoint is created in self.empty_homepage
        """
        md = "# Project title\nSome text for this page"
        self._save_page(GBWebPath('index.md', self.doc), md)
        self.rebuild_docs()
        return flask.redirect(self._url_prefix+'/-/editor/')

    def create_from_template(self, template):
        """
        Create a new page from a given template. This is called from the new page interface.
        """
        input_data = request.args.to_dict()
        if 'pagename' not in input_data:
            message = urllib.parse.quote('No page name given')
            return flask.redirect(self._url_prefix+f'/-/new-template/{template}?msg={message}')
        pagename = input_data['pagename']
        if not is_filepath_safe(pagename, allow_external=False):
            message = urllib.parse.quote(f'Page name "{pagename}" contains unsafe characters')
            return flask.redirect(self._url_prefix+f'/-/new-template/{template}?msg={message}')

        path = GBWebPath(pagename, self.doc)

        if path.gb_file is not None:
            message = urllib.parse.quote(f'Page "{pagename}" already exists')
            return flask.redirect(self._url_prefix+f'/-/new-template/{template}?msg={message}')

        if template == 'empty':
            md = ""
        elif template == 'stepbystep':
            md = example.testpage("Example instructions")
        else:
            message = urllib.parse.quote(f'Unknown template specified: "{template}"')
            return flask.redirect(self._url_prefix+f'/-/new-page?msg={message}')

        self._save_page(path, md)
        self.rebuild_docs()
        return flask.redirect(self._url_prefix+f'/{path.web_path}/-/editor/')

    def contents_page(self):
        """
        Return a rendered html page listing all files
        """
        return self.renderer.contents_page(self.doc.output_files)

    def warning_page(self):
        """
        Return a rendered html page of all warnings
        """
        return self.renderer.warning_page(self._global_log)

    def rebuild_docs(self, total_rebuild=False):
        if self._building:
            return
        self._building = True
        try:
            if total_rebuild:
                rules = render.URLRulesHTML()
                configuration = load_config_from_file(self._config_file, self._working_dir)
                configuration.remove_landing_title = True
                self._license_file = utilities.handle_licenses(configuration)
                self.doc = Documentation(configuration, self._working_dir, rules, gitbuilding_previewers())
            log_length = self._handler.log_length
            file_list = read_directory(self._working_dir,
                                    include_list=['static/Icons/info.png'],
                                    exclude_list=self.doc.config.exclude)
            if self._license_file is not None:
                file_list.append(self._license_file)
            external_files = read_external_directories(self.doc.config.external_dirs,
                                                    exclude_list=self.doc.config.exclude)
            self.doc.buildall(file_list, external_files)
            self._read_config()
            self.renderer.config = self._config
            self.renderer.populate_vars()
            self._global_log = self._handler.log_from(log_length)
            self.renderer.set_warning_count(self._global_log)
            self._building = False
        except Exception as error:
            self._building = False
            raise error

    def dropped_file(self, rawsubpath=None):
        """
        This gets run if a file gets dragged and dropped into the editor
        """
        files = request.files
        if rawsubpath is None:
            folder_depth = 0
        else:
            path = GBWebPath(rawsubpath, self.doc)
            folder_depth = len(path.gb_path_deduplicated.split('/')) - 1
        out_filenames = []
        md_line = ''
        # loop through all files and save images
        for file_id in files:
            file_obj = files[file_id]
            if file_obj.mimetype.startswith("image"):
                filename, md = self._process_dropped_file(file_obj, "images", folder_depth)
                out_filenames.append(filename)
                md_line += md
            elif self.doc.previewer_for_uri(file_obj.filename) is not None:
                save_dir = self.doc.previewer_for_uri(file_obj.filename).dir_for_dropped_files
                filename, md = self._process_dropped_file(file_obj, save_dir, folder_depth)
                out_filenames.append(filename)
                md_line += md
            else:
                _LOGGER.warning("Cannot upload file of mimetype: %s", file_obj.mimetype)

        if len(out_filenames) > 0:
            return jsonify({"received": True,
                            "filenames": out_filenames,
                            "md_line": md_line})
        return flask.abort(405)

    def _process_dropped_file(self, file_obj, save_dir, folder_depth):

        filename = as_posix(file_obj.filename.replace(" ", ""))

        #This is going into the markdown so we always use unix paths.
        file_path = f"{save_dir}/{filename}"
        i = 0
        while is_local_file(file_path, self._working_dir):
            if i == 0:
                path_no_ext, ext = posixpath.splitext(file_path)
            i += 1
            file_path = f'{path_no_ext}{i:03d}{ext}'

        _, ext = posixpath.splitext(filename)
        temp_path = TMPDIR + "/" + str(uuid()) + ext
        file_obj.save(temp_path)
        self._unsaved_dropped_files.add_file(file_path, temp_path)
        md_file_path = '../'*folder_depth + file_path
        md = f'![]({md_file_path})\n'
        return file_path, md


    def undefined_special_page(self, rawsubpath=None):
        """
        Any path in the live editor that starts with /-/ is a special page, these include the 
        live editor and the configuration editor. If /-/ is followed by an unknown path then
        a normal 404 should be returned rather than the standard missing page which allows the page
        to be created.
        """
        # pylint: disable=unused-argument
        return flask.abort(404)

    def live_render(self):
        """
        Runs the live renderer and returns the html as well as warnings
        in JSON format
        """

        content = request.get_json()
        if content["md"] is None:
            return jsonify({"html": "", "log": "", "number": 0})

        log_length = self._handler.log_length
        overloaded_path = None
        if not "page" in content: # Live render landing page
            if self.doc.config.landing_page is not None:
                page = self.doc.landing_page
                overloaded_path = '-/editor/index'
                processed_text, meta_info = page.rebuild(content["md"], overloaded_path)
                title = page.title
                self.live_renderer.config.title = title
                self.live_renderer.populate_vars()
        else:
            path = GBWebPath(content["page"], self.doc)
            page = self._get_docpage(path)
            overloaded_path = path.web_path+'/-/editor/index'
            if page is None:
                return jsonify({"html": "", "log": "", "number": 0})
            show_within = content.get("show_within", "")
            if show_within:
                within_path = GBWebPath(show_within, self.doc)
                within_page = self._get_docpage(within_path)
                if within_page is None:
                    return jsonify({"html": "", "log": "", "number": 0})
                if within_path.variables is not None:
                    within_page = within_page.get_variation(within_path.variables)
                processed_text, meta_info = page.rebuild_within(within_page,
                                                                content["md"],
                                                                overloaded_path)
            else:
                if path.variables is not None:
                    page = page.get_variation(path.variables)
                processed_text, meta_info = page.rebuild(content["md"], overloaded_path)


        html = self.live_renderer.render_md(processed_text,
                                            link=overloaded_path,
                                            meta_info=meta_info,
                                            template=self.live_renderer.IFRAME,
                                            nav=False)
        log = self._handler.log_from(log_length)

        return jsonify({"html": html,
                        "log": render.format_warnings(log),
                        "number": len(log)})

    def new_page(self):
        """
        Brings up the new page creation page
        """
        input_data = request.args.to_dict()
        if 'msg' in input_data:
            msg = input_data['msg']
        else:
            msg = None
        html = self.renderer.new_page(error_message=msg)
        return html

    def new_template(self, template):
        """
        Brings up the form to complete the new page creation
        """
        input_data = request.args.to_dict()
        if 'msg' in input_data:
            msg = input_data['msg']
        else:
            msg = None
        html = self.renderer.new_page_form(template, error_message=msg)
        return html

    def edit_page(self, rawsubpath=None):
        """
        Starts the live editor for a particular page
        """
        path = GBWebPath(rawsubpath, self.doc)
        if path.is_markdown:
            self.live_renderer.config = deepcopy(self._config)
            self.live_renderer.populate_vars()

            page = GBPATH + "/static/webapp/buildup-editor.html"
            native_path = as_native_path(page, self._working_dir)
            return flask.send_file(native_path)

        html = self.renderer.render("<h1>Sorry. Cannot edit this file!</h1>",
                                    link=rawsubpath)
        return html

    def conf_edit(self):
        """
        Starts the configuration editor to edit buildconf.yaml
        """
        page = GBPATH + "/static/webapp/conf-editor.html"
        native_path = as_native_path(page, self._working_dir)
        return flask.send_file(native_path)

    def raw_config(self):
        """
        Returns the raw yaml configuration file as well as other data such as
        supported licenses and list of pages. This an endpoint for the configuration
        editor.
        """
        pages = [page.filepath for page in self.doc.pages]
        if self._license_file is not None:
            if self._license_file.path in pages:
                pages.remove(self._license_file.path)
        return jsonify({"config": get_raw_config_data(self._config_file, self._working_dir),
                        "licenses": utilities.supported_licenses(),
                        "pages": pages})

    def save_config(self):
        """
        Saves the edits from the live editor and full rebuilds the documentation
        """

        #Get the JSON from the request
        content = request.get_json()

        if content["config"] is None:
            return jsonify({"saved": False, "warnings":["Unknown Error."]})

        warning_dict = check_config_string(content["config"])
        if warning_dict == {}:
            self._save_config_file(content["config"])
            self.rebuild_docs(total_rebuild=True)
            return jsonify({"saved": True, "warnings": []})
        warnings = []
        for key in warning_dict:
            warnings.append(key + ":  " + str(warning_dict[key]))

        return jsonify({"saved": False, "warnings":warnings})

    def render_page(self, rawsubpath=None):
        """
        Renders the static version of a page
        """

        path = GBWebPath(rawsubpath, self.doc)
        if path.is_empty_homepage:
            return self.renderer.empty_homepage()
        if path.is_missing_page:
            return self.renderer.missing_page()
        if path.gb_file is None:
            # If the file requested is not chached in the documentation
            # try other means to render it
            return self._render_missing_file(path)

        if path.is_markdown and path.gb_file.dynamic_content:
            return self._render_markdown_page(path)

        return self._send_file_obj(path.gb_file)

    def _render_markdown_page(self, path):
        editorbutton = False
        if path.gb_path_deduplicated in self.doc.pages:
            editorbutton = True
        if path.is_homepage:
            link = None
        else:
            link = path.web_path
        return self.renderer.render_md(path.gb_file.content,
                                       link,
                                       meta_info=path.gb_file.meta_info,
                                       editorbutton=editorbutton)

    def _render_missing_file(self, path):
        """
        Render a file that is not found in the GitBuilding documentation object. This could be
        a recently dragged and dropped file, or a file that is in
        the gitbuilding directory but was not processed during the last full build
        """
        if path.is_markdown:
            page_obj = self.doc.get_page_by_path(path.web_path)
            if page_obj:
                if page_obj.included_in_another_page:
                    md = "# This forms part of another page\n\n"
                    md += ("The content of this page forms part of abother page. It does not "
                           "have its own page in the documentation.\n\n"
                           f"[Edit included content]({self._url_prefix}/{path.web_path}/-/editor)")
                    return self.renderer.render_md(md,
                                                   path.web_path,
                                                   editorbutton=True)
            else:
                # Else give option to create the page.
                return self.renderer.render_md("# Page not found\n Do you want to "
                                            f"[create it]({self._url_prefix}/{path.web_path}/-/editor)?",
                                            path.web_path,
                                            editorbutton=True)

        # For missing files that are not markdown check the temporary
        # files that were drag and dropped.
        temp_file = self._unsaved_dropped_files.get(path.web_path)
        if temp_file is not None:
            native_path = as_native_path(temp_file, self._working_dir)
            return flask.send_file(native_path)

        # If file still missing it may be in the input directory this should only
        # happen when live editing a file
        file_list = read_directory(self._working_dir,
                                   include_list=['static/Icons/info.png'],
                                   exclude_list=self._config.exclude)
        external_files = read_external_directories(self._config.external_dirs,
                                                   exclude_list=self._config.exclude)
        full_file_list = file_list+external_files
        if path.os_path in full_file_list:
            file_obj = full_file_list[full_file_list.index(path.os_path)]
            return self._send_file_obj(file_obj)

        return self._404_or_missing_image(path.web_path)

    def _send_file_obj(self, file_obj):
        if file_obj.dynamic_content:
            return self._send_dynamic_file_obj(file_obj)
        return self._send_static_file_obj(file_obj)

    def _send_static_file_obj(self, file_obj):
        path = file_obj.location_on_disk
        if is_local_file(path, self._working_dir):
            native_path = as_native_path(path, self._working_dir)
            return flask.send_file(native_path)

        return self._404_or_missing_image(file_obj.path)

    def _send_dynamic_file_obj(self, file_obj):
        file_dir = localise(TMPDIR + "/.gbserver")
        make_dir_if_needed_abs(file_dir)
        filename =  posixpath.basename(file_obj.path)
        if file_obj.files_to_zip is not None:
            native_zip_path = as_native_path(filename, file_dir)
            create_zip(native_zip_path, file_obj.files_to_zip, self._working_dir, zip_abs=True)
        else:
            write_local_file(filename,
                             file_dir,
                             file_obj.content)
        native_path = as_native_path(filename, file_dir)
        return flask.send_file(native_path)

    def _404_or_missing_image(self, web_path):
        if web_path.lower().endswith((".jpg", ".jpeg", ".png", ".gif", '.svg',
                                     ".tif", ".tiff", '.webp')):
            if web_path.startswith('orphaned_files'):
                image = "static/local-server/Orphaned_file.png"
            else:
                image = "static/local-server/Missing_image.png"
            native_path = as_native_path(image, localise(GBPATH))
            return flask.send_file(native_path)
        return flask.abort(404)

    def return_assets(self, rawsubpath):
        """
        returns file from the assets directory
        """
        page = "assets/" + rawsubpath
        if is_local_file(page, self._working_dir):
            native_path = as_native_path(page, self._working_dir)
            return flask.send_file(native_path)

        return flask.abort(404)


class DevLiveEditor(LiveEditor):
    """
    Child class of GBServer, this server allows hot-reloading of webapp for
    development.
    """

    def edit_page(self, rawsubpath=None):
        """
        Starts the live editor for a particular page
        """
        path = GBWebPath(rawsubpath, self.doc)
        if path.is_markdown:
            self.live_renderer.config = deepcopy(self._config)
            self.live_renderer.populate_vars()

            url = "http://localhost:8080/static/webapp/buildup-editor.html"
            try:
                req = requests.get(url, timeout=5)
            except requests.exceptions.RequestException:
                msg = (f"ERROR: Could not connect to webapp dev server"
                       f" on '{url}', did you forget to start it?")
                return flask.abort(flask.Response(msg, status=500))
            return req.text

        html = self.renderer.render("<h1>Sorry. Cannot edit this file!</h1>",
                                    link=rawsubpath)
        return html

    def conf_edit(self):
        """
        Configuration editor in dev server
        """

        url = "http://localhost:8080/static/webapp/conf-editor.html"
        try:
            req = requests.get(url, timeout=5)
        except requests.exceptions.RequestException:
            msg = (f"ERROR: Could not connect to webapp dev server"
                    f" on '{url}', did you forget to start it?")
            return flask.abort(flask.Response(msg, status=500))
        return req.text
