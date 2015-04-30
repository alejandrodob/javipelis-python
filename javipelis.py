import os

if os.name == 'nt':
    import win32api, win32con


class Finder(object):

    def __init__(self):
        self._directors = []
        self._movies = []

    @property
    def directors(self):
        return self._directors

    @property
    def movies(self):
        return self._movies

    def discover(self, path):
        files_in_path = [f for f in os.listdir(path) if not self._is_hidden(f)]
        self._directors = self._extract_directors(files_in_path)
        self._movies = self._extract_movies(files_in_path)

    def _extract_directors(self, filenames_list):
        return [self._get_director_name(filename).strip()
                for filename in filenames_list
                if self._get_director_name(filename)]

    def _get_director_name(self, filename):
        if len(filename.split('.')) > 1:
            return filename.split('.')[0]

    def _extract_movies(self, filenames_list):
        return [self._get_movie_title(filename).strip()
                for filename in filenames_list
                if self._get_movie_title(filename)]

    def _get_movie_title(self, filename):
        if len(filename.split('.')) > 1:
            return filename.split('.')[1]

    def _is_hidden(self, _file):
        if os.name == 'nt':
            attribute = win32api.GetFileAttributes(_file)
            return attribute & (win32con.FILE_ATTRIBUTE_HIDDEN | win32con.FILE_ATTRIBUTE_SYSTEM)
        else:
            return _file.startswith('.')
