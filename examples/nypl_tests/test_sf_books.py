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

        # assert Newsletter Subscription
        self.assert_newsletter_signup(BooksPage)

    def test_books_links(self):
        print("test_books_music_movies_links()\n")

        # Assert 'h3' links for each 'h2' on the page
        total_h2_amount = len(self.find_elements(BooksPage.total_h2))
        print("total h2(x) amount is = " + str(total_h2_amount))

        for x in range(1, total_h2_amount + 1):
            total_h3 = len(self.find_elements('(' + BooksPage.total_h2 + f'[{x}]//..//a)'))
            print("total h3(y) amount is = " + str(total_h3))
            for y in range(1, total_h3 + 1):
                if x == 4 and y == 3:
                    continue
                print("x = " + str(x))
                print("y = " + str(y))
                self.assert_page_loads_successfully('(' + BooksPage.total_h2 + f'[{x}]//..//a)[{y}]')
            print("===============================\n")

