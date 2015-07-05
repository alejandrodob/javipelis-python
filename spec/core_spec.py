import os
import sys
topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)
import javipelis

TEST_DIR = 'spec/movie-test-dir'

with description('movie finder'):

    with context('when created with a root directory'):

        with before.each:
            self.finder = javipelis.Finder(TEST_DIR)

        with it('creates entries for found directors'):

            assert 'Kubrik, Stanley' in self.finder.directors, self.finder.directors

        with it('does not create noisy entries for random files found'):

            assert '' not in self.finder.directors, self.finder.directors
            assert None not in self.finder.directors, self.finder.directors

        with it('stores the title of the movies found for each director'):

            assert 'Alien' in self.finder.movie_titles(), self.finder.movie_titles()

        with it('does not create noisy entries for hidden files found'):

            assert 'hidden' not in self.finder.movies, self.finder.movies
            assert None not in self.finder.movies, self.finder.movies
            assert '' not in self.finder.movies, self.finder.movies

        with it('stores the year of the movie, if exists'):

            assert '1971' in [movie.get('year') for movie in self.finder.movies]
