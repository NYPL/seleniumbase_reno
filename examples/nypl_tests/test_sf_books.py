import pytest

from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_sf_books import BooksPage


class BooksTest(NyplUtils):

    # https://www.nypl.org/books-music-movies

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        self.set_window_size(1920, 1080)

        # open main page
        self.open_books_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_books_main(self):
        print("test_books_music_movies_page_main()\n")

        # assert title
        self.assert_title(BooksPage.title)

        # assert images on the page
        self.image_assertion()

        # assert breadcrumbs
        self.assert_element(BooksPage.home_button)  # home
        self.assert_element(BooksPage.books)  # events

        # assert all links on the page
        self.assert_links_valid(BooksPage.all_links)

        # assert Newsletter Subscription
        self.assert_newsletter_signup(BooksPage)

