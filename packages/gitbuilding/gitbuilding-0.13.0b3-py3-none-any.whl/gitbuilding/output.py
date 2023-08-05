"""
This module handles all the Builder classes that produce outputs.
Currently the outputs are
* HTML provided by StaticSiteBuilder
* Markdown provided by MarkdownBuilder
to make a custom Builder you can inherit from the Builder class.
"""

import posixpath
import sys
import logging
import regex as re
try:
    from PIL import Image
    from weasyprint import HTML
except ImportError:
    pass
from gitbuilding.render import GBRenderer, URLRulesHTML, URLRulesPDF
from gitbuilding.buildup import Documentation, URLRules, read_directory, read_external_directories
from gitbuilding.config import load_config_from_file
from gitbuilding import utilities
from gitbuilding.previewers import gitbuilding_previewers
import gitbuilding.buildup.utilities as buildup_utilities
from gitbuilding.native_file_operations import (GBPATH,
                                                TMPDIR,
                                                as_native_path,
                                                make_local_dir,
                                                make_local_dir_abs,
                                                make_dir_if_needed,
                                                make_dir_if_needed_abs,
                                                is_local_file,
                                                exists_on_disk,
                                                copy_local_files,
                                                copy_local_directory,
                                                write_local_file,
                                                create_zip)

_LOGGER = logging.getLogger('BuildUp.GitBuilding')

class Builder():
    """
    Base class for Builder classes. Do not use this class.
    """

    def __init__(self, working_dir, url_rules, previewers, rem_title=False, rem_bottom_nav=False):
        """
        working dir is the documentation directory
        rem_title is set to true to override configuration and
        remove the title from the landing page
        """
        self._working_dir = working_dir
        config_file = 'buildconf.yaml'
        configuration = load_config_from_file(config_file, self._working_dir)
        if rem_title:
            configuration.remove_landing_title = True
        if rem_bottom_nav:
            configuration.remove_bottom_nav = True
        license_file = utilities.handle_licenses(configuration)
        self._doc = Documentation(configuration, working_dir, url_rules, previewers)
        file_list = read_directory(working_dir,
                                   include_list=['static/Icons/info.png'],
                                   exclude_list=configuration.exclude)
        if license_file is not None:
            file_list.append(license_file)
        external_files = read_external_directories(configuration.external_dirs,
                                                   exclude_list=configuration.exclude)
        self._doc.buildall(file_list, external_files)
        self._out_dir = "_build"
        #Setting explictly whether out dir is external to set expectations and avoid OS specific edge cases
        self._out_dir_abs = False

    @property
    def doc(self):
        """
        Returns the buildup Documentation object for the site.
        """
        return self._doc

    def _make_clean_directory(self):
        """
        Make a clean and empty directory for the output
        """
        if self._out_dir_abs:
            make_local_dir_abs(self._out_dir, remove_existing=True)
        else:
            make_local_dir(self._out_dir, self._working_dir, remove_existing=True)

    def build(self):
        """
        This method should be overridden for in derived classes
        """
        raise RuntimeError('`build` should be overridden by other Builder classes')

    def _build_file(self, outfile):
        """
        Writes the output for any buildup page and copies over other
        output files
        """

        if outfile.path.startswith('..'):
            _LOGGER.warning('Skipping %s.', outfile.path)
            return
        full_out_path = self._out_dir+'/'+outfile.path

        if self._out_dir_abs:
            make_dir_if_needed_abs(full_out_path, isfile=True)
        else:
            make_dir_if_needed(full_out_path, self._working_dir, isfile=True)

        if outfile.dynamic_content:
            self._build_dynamic_content(outfile, full_out_path)
        else:
            self._build_static_conent(outfile, full_out_path)

    def _build_dynamic_content(self, outfile, full_out_path):
        pass

    def _build_static_conent(self, outfile, full_out_path):
        if is_local_file(outfile.location_on_disk, self._working_dir):
            copy_local_files(outfile.location_on_disk,
                             full_out_path,
                             self._working_dir,
                             force_relative=False)

class MarkdownBuilder(Builder):
    """
    Class to build a markdown directory from a BuildUp directory.
    """

    def __init__(self, working_dir, url_rules=None):
        """
        working dir is the documentation directory
        """

        if url_rules is None:
            url_rules = URLRules(rel_to_root=False)

        def fix_missing(url, anchor, page):
            if url == "" and  anchor == "":
                url = posixpath.relpath("missing.md", posixpath.dirname(page))
                return url, anchor
            return url, anchor

        url_rules.add_modifier(fix_missing)
        previewers = gitbuilding_previewers(enabled=False)
        super().__init__(working_dir, url_rules, previewers)


    def _write_missing_page(self):
        """
        Write the page for any part which is missing from the documentation
        """
        missing_page_file = self._out_dir + "/missing.md"
        write_local_file(missing_page_file, self._working_dir, "# GitBuilding Missing Part")

    def _build_dynamic_content(self, outfile, full_out_path):
        if outfile.files_to_zip is not None:
            create_zip(full_out_path, outfile.files_to_zip, self._working_dir)
        else:
            write_local_file(full_out_path, self._working_dir, outfile.content)

    def build(self):
        """
        Builds the whole markdown folder
        """

        self._make_clean_directory()
        self._write_missing_page()
        for outfile in self.doc.output_files:
            self._build_file(outfile)

class StaticSiteBuilder(Builder):
    """
    Class to build a static website from a BuildUp directory.
    """

    def __init__(self, working_dir, url_rules=None, previewers=None, root=None, rem_bottom_nav=False, no_server=False):
        """
        working dir is the documentation directory
        """
        if url_rules is None:
            url_rules = URLRulesHTML(no_server=no_server)
        if previewers is None:
            previewers = gitbuilding_previewers(enabled=True, no_server=no_server)
        super().__init__(working_dir,
                         url_rules,
                         previewers,
                         rem_title=True,
                         rem_bottom_nav=rem_bottom_nav)
        if root is None:
            root = self._doc.config.website_root
        self._renderer = GBRenderer(working_dir, self._doc.config, url_rules, root=root, no_server=no_server)

        # site dir is not setable as we would then need to do all the checks for
        # not writing over a specific directory
        self._out_dir = "_site"

    def _write_missing_page(self):
        """
        Write the page for any part which is missing from the documentation
        """
        missing_page_file = self._out_dir + "/missing.html"
        write_local_file(missing_page_file, self._working_dir, self._renderer.missing_page())

    def _build_dynamic_content(self, outfile, full_out_path):
        if outfile.path.endswith('.md'):
            self._markdown_content(outfile, full_out_path)
        elif outfile.files_to_zip is not None:
            create_zip(full_out_path, outfile.files_to_zip, self._working_dir)
        else:
            write_local_file(full_out_path, self._working_dir, outfile.content)

    def _markdown_content(self, outfile, full_out_path):
        if outfile.path == self.doc.config.landing_page:
            full_out_path = self._out_dir + "/index.html"
        else:
            full_out_path = posixpath.splitext(full_out_path)[0]+'.html'
        page_html = self._renderer.render_md(outfile.content,
                                             posixpath.splitext(outfile.path)[0]+'.html',
                                             meta_info=outfile.meta_info,
                                             editorbutton=False)
        write_local_file(full_out_path, self._working_dir, page_html)

    def _copy_static_files(self):
        """
        Copies all the static web files that come as default with gitbuilding.
        This includes the CSS, the favicons, and the 3D viewer
        """
        static_dir = GBPATH + "/static"
        copy_local_directory(static_dir,
                             self._out_dir,
                             self._working_dir,
                             force_relative=False,
                             ignore_dirs=["webapp", "local-server"])

    def _copy_local_assets(self):
        """
        Copies all assets from the local directory. This is custom CSS and favicons
        """
        copy_local_directory("assets", self._out_dir, self._working_dir, force_relative=False)

    def build(self):
        """
        Builds the whole static site
        """

        self._make_clean_directory()
        self._write_missing_page()
        for outfile in self.doc.output_files:
            self._build_file(outfile)
        self._copy_static_files()
        if exists_on_disk("assets", self._working_dir):
            self._copy_local_assets()

class PdfBuilder(StaticSiteBuilder):
    """
    Class to build a static website from a BuildUp directory.
    """

    def __init__(self, working_dir, url_rules=None):
        """
        working dir is the documentation directory
        """
        if url_rules is None:
            url_rules = URLRulesPDF()
        previewers = gitbuilding_previewers(enabled=False)
        super().__init__(working_dir, url_rules, previewers, root='', rem_bottom_nav=True)
        self._out_dir = TMPDIR + "/GitBuildingPDF"
        self._out_dir_abs = True
        self._html = {}
        self._installed = 'weasyprint' in sys.modules
        if not self._installed:
            _LOGGER.warning('Trying to build PDF without weasyprint installed')

    def build(self):
        """
        Builds the pdf
        """
        if not self._installed:
            return

        if self._doc.page_order.number_of_paths <= 1:
            if self._doc.page_order.number_of_paths == 1:
                pagelist = self._doc.page_order.pagelists[0]
                page_ordering = buildup_utilities.nav_order_from_pagelist(pagelist)
            else:
                if self._doc.landing_page is None:
                    page_ordering = []
                else:
                    page_ordering = [self._doc.landing_page.filepath]
            filelist = self.doc.output_files
            self._build_from_filelist('Documentation.pdf', filelist, page_ordering)
        else:
            for n in range(self._doc.page_order.number_of_paths):
                filelist = self._doc.output_for_pathlist(n)
                pagelist = self._doc.page_order.pagelists[n]
                page_ordering = buildup_utilities.nav_order_from_pagelist(pagelist)
                filename = self._get_filename_for_page_ordering(page_ordering)
                subtitle = self._get_subtitle_for_page_ordering(page_ordering)
                self._build_from_filelist(filename, filelist, page_ordering, subtitle=subtitle)

    def _get_filename_for_page_ordering(self, page_ordering):
        rootpage = self._doc.get_page_by_path(page_ordering[0])
        return re.sub(r'[^a-zA-Z0-9\_\-]', '', rootpage.title) + '.pdf'

    def _get_subtitle_for_page_ordering(self, page_ordering):
        rootpage = self._doc.get_page_by_path(page_ordering[0])
        return rootpage.title

    def _build_from_filelist(self, filename, filelist, page_ordering, subtitle=None):

        #temp_dir for html site
        self._make_clean_directory()
        for outfile in filelist:
            #outputs dynamics files to the self.html dictionary
            self._build_file(outfile)
        self._copy_static_files()
        if exists_on_disk("assets", self._working_dir):
            self._copy_local_assets()

        combined = ''
        for page in page_ordering:
            combined += self._html[page]
            del self._html[page]
        for page in self._html:
            combined += self._html[page]
        combined = self._renderer.full_pdf(combined, subtitle)
        write_local_file("index.html", self._out_dir, combined)
        make_dir_if_needed('_pdf', self._working_dir)

        html_path = as_native_path('index.html', self._out_dir)
        pdf_path = as_native_path('_pdf/' + filename, self._working_dir)
        HTML(html_path).write_pdf(pdf_path )

    def _build_dynamic_content(self, outfile, _):
        if not outfile.path.endswith('.md'):
            return
        page_html = self._renderer.render_md(outfile.content,
                                             posixpath.splitext(outfile.path)[0],
                                             meta_info=outfile.meta_info,
                                             editorbutton=False,
                                             nav=False,
                                             template=self._renderer.PDFPAGE)
        self._html[outfile.path] = page_html

    def _build_static_conent(self, outfile, full_out_path):
        # Convert all images to a smallish PNG due to GDK_pixbuf bug. Can remove this
        # when upstream bug is fixed
        # Should be fixed as of GDK-Pixbuf 2.42.0 - need to check versions before we remove this
        outpath, ext = posixpath.splitext(full_out_path)
        if ext.lower() in ['.jpg', 'jpeg']:
            img = Image.open(outfile.location_on_disk)
            size_tuple = (1000, round(1000*img.size[1]/img.size[0]))
            r_img = img.resize(size_tuple)
            r_img.save(as_native_path(outpath+'.png', self._working_dir))
        else:
            super(). _build_static_conent(outfile, full_out_path)
