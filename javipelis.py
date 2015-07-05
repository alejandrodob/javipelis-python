import os

if os.name == 'nt':
    import win32api, win32con


class Finder(object):

    def __init__(self, root_path):
        self._directors = []
        self._movies = []
        self.discover(root_path)

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
        print files_in_path

    def movie_titles(self):
        return [movie.get('title') for movie in self.movies]

    def _extract_directors(self, filenames_list):
        return [self._get_director_name(filename).strip()
                for filename in filenames_list
                if self._get_director_name(filename)]

    def _get_director_name(self, filename):
        if len(filename.split('.')) > 1:
            return filename.split('.')[0]

    def _extract_movies(self, filenames_list):
        return [self._movie_info(filename)
                for filename in filenames_list
                if self._movie_title(filename)]

    def _movie_title(self, filename):
        if len(filename.split('.')) > 1:
            return filename.split('.')[1].strip()

    def _movie_year(self, filename):
        if len(filename.split('.')) > 1:
            try:
                return filename.split('.')[2].strip()
            except IndexError:
                return filename.split('.')[-1].split(',')[-1].strip()

    def _movie_info(self, filename):
        return {'title': self._movie_title(filename),
                'year': self._movie_year(filename)}

    def _is_hidden(self, _file):
        if os.name == 'nt':
            attribute = win32api.GetFileAttributes(_file)
            return attribute & (win32con.FILE_ATTRIBUTE_HIDDEN | win32con.FILE_ATTRIBUTE_SYSTEM)
        else:
            return _file.startswith('.')
