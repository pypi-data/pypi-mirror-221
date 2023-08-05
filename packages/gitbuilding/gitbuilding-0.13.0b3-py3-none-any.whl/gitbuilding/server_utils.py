'''
This module contains key utilities for the sever that do not sit within the main server
classes nor withing the live editor
'''

import posixpath
import logging
from gitbuilding.native_file_operations import (delete_local_file,
                                                localise)

_LOGGER = logging.getLogger('BuildUp.GitBuilding')

class GBWebPath():
    """
    GBWebPath is a class that parses paths from the server and can return either the
    corresponding local path or the correct special path.
    """

    def __init__(self, rawpath, doc):
        self._web_path = rawpath
        self._gb_path = None
        self._gb_file = None
        self._missing_page = False
        self._homepage = False

        self._process_path(rawpath, doc)

    def _process_path(self, rawpath, doc):
        """
        Check for special cases then process path as normal
        """
        if rawpath is None:
            self._homepage = True
            self._web_path = 'index.html'
            self._gb_path = doc.config.landing_page
            if self._gb_path is not None:
                self._gb_file = doc.get_file(self._gb_path)
        elif rawpath == "missing":
            self._missing_page = True
        else:
            self._process_standard_path(rawpath, doc)

    def _process_standard_path(self, rawpath, doc):
        base_path, ext = posixpath.splitext(rawpath)
        if ext == '':
            self._web_path += '.html'
            ext = '.html'

        if ext.lower() == '.html':
            self._gb_path = base_path + '.md'
        else:
            self._gb_path = rawpath

        self._gb_file = doc.get_file(self._gb_path)


    @property
    def is_homepage(self):
        """
        Return true if the link is to the homepage
        """
        return self._homepage

    @property
    def is_empty_homepage(self):
        """
        Return true if the link is to the homepage but no homepage is set
        """
        return self._homepage and self._gb_path is None

    @property
    def is_missing_page(self):
        """
        Return true if the link the GitBuilding special page "missing"
        """
        return self._missing_page

    @property
    def is_markdown(self):
        """
        Return true if the GitBuilding expects this file to be markdown. Returns true
        even if the file cannot be found
        """
        return self._gb_path.endswith('.md')

    @property
    def web_path(self):
        """
        Return the html path
        """
        return self._web_path

    @property
    def gb_path(self):
        """
        Return the path  for this file as handled internally by gitbuilding
        (relative to the doc directory)
        """
        return self._gb_path

    @property
    def gb_path_deduplicated(self):
        """
        Return the path  for this file as handled internally by gitbuilding. If the file is a
        duplicate created by multiple paths through the documentation this will
        return the orignal
        """
        if self._gb_file is None:
            return self._gb_path
        if self._gb_file.duplicate_of is None:
            return self._gb_path
        return self._gb_file.duplicate_of

    @property
    def variables(self):
        """
        Return the variables set on this page
        """
        if self._gb_file is None:
            return None
        return self._gb_file.variables

    @property
    def gb_file(self):
        """
        Return the gitbuilding file object for this path
        """
        return self._gb_file

    @property
    def os_path(self):
        """
        Return the filepath in the native os format
        """
        return localise(self._gb_path)

class DroppedFiles:
    """
    Pretty simple class for handling the files dropped into the editor. This
    could be handled with a list of dictionaries but the syntax for checking
    and finding the correct file gets really ugly.
    """

    def __init__(self):
        self._files = []

    def add_file(self, output_file, temp_file):
        """
        Add a dropped file to be tracked. Inputs are the filename in the
        output, and the temporary filename
        """
        if not self.contains(output_file):
            self._files.append({'output_path':output_file,
                                'temp_path':temp_file})

    @property
    def _out_paths(self):
        return [fdict['output_path'] for fdict in self._files]

    def get(self, filename):
        """
        Get the temp file for location for `filename`. Returns None if the
        filename does not exist
        """

        out_paths = self._out_paths
        if filename in out_paths:
            return self._files[out_paths.index(filename)]['temp_path']
        return None

    def contains(self, filename):
        """
        Returns true if `filename` is listed as an output filename.
        """
        return self.get(filename) is not None

    def remove(self, filename):
        """
        Removes the record for the dropped file and deletes the temporary file
        from disk
        """
        out_paths = self._out_paths
        if filename in out_paths:
            ind = out_paths.index(filename)
            temp_file = self._files[ind]['temp_path']
            #The dropped file is an absolute path
            img_dir, basename = posixpath.split(temp_file)
            delete_local_file(basename, img_dir)
            self._files.pop(ind)
            return True
        return False
