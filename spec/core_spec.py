import os
import sys
topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)
import javipelis

with description('movie finder'):

    with context('discovering folders and files'):

        with before.all:
            self.test_dir = 'spec/movie-test-dir'

        with before.each:
            self.finder = javipelis.Finder()

        with it('creates entries for found directors'):
            self.finder.discover(self.test_dir)

            assert 'Kubrik, Stanley' in self.finder.directors, self.finder.directors

        with it('does not create noisy entries for random files found'):
            self.finder.discover(self.test_dir)

            assert '' not in self.finder.directors, self.finder.directors
            assert None not in self.finder.directors, self.finder.directors

        with it('stores the title of the movies found for each director'):
            self.finder.discover(self.test_dir)

            assert 'Alien' in self.finder.movie_titles(), self.finder.movie_titles()

        with it('does not create noisy entries for hidden files found'):
            self.finder.discover(self.test_dir)

            assert 'hidden' not in self.finder.movies, self.finder.movies
            assert None not in self.finder.movies, self.finder.movies
            assert '' not in self.finder.movies, self.finder.movies

        with it('stores the year of the movie, if exists'):
            self.finder.discover(self.test_dir)

            assert '1971' in [movie.get('year') for movie in self.finder.movies]
