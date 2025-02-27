from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_bl_best_books import BestBooksPage
import random


class BookListsBestBooks(NyplUtils):

    # https://www.nypl.org/books-more/recommendations/best-books/adults
    # https://www.nypl.org/books-more/recommendations/best-books/teens
    # https://www.nypl.org/books-more/recommendations/best-books/kids

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open book lists page
        # self.open_best_books_page()  # opening URLs from within the tests itself

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")

        super().tearDown()

    def test_best_books_adults(self):
        # https://www.nypl.org/books-more/recommendations/best-books/adults
        print('test_best_books_adults()\n')
        self.open_best_books_page(category='adults')

        # assert images on the page
        self.image_assertion()

        # assert all links on the page
        self.assert_links_valid(BestBooksPage.all_links)

        # assert breadcrumbs and page elements
        self.assert_element(BestBooksPage.home)
        self.assert_element(BestBooksPage.books_and_more)
        self.assert_element(BestBooksPage.recommendations)
        self.assert_element(BestBooksPage.h1_heading)
        self.assert_true("Best Books" in self.get_text(BestBooksPage.h1_heading))
        self.assert_element(BestBooksPage.adults_tab)
        self.assert_element(BestBooksPage.submit)
        self.assert_element(BestBooksPage.filter_results_below)
        self.assert_element(BestBooksPage.additional_info_h3)
        self.wait(1)

        # assert left side filter
        self.assert_left_side_filters(BestBooksPage)

        # assert book number in the page >= 1
        h3_amount = int(self.get_text(BestBooksPage.book_results).split()[0])  # book result amount
        print("\nBook result amount is = " + str(h3_amount))  # optional print of the amount seen in h3 element
        # optional print of the number of the displayed books in the page
        self.assert_true(h3_amount >= 1, "Adults book number and amount no >= 1")

    def test_best_books_teens(self):
        # https://www.nypl.org/books-more/recommendations/best-books/teens
        print('test_best_books_teens()\n')
        self.open_best_books_page(category='teens')

        # assert images on the page
        self.image_assertion()

        # assert all links on the page
        self.assert_links_valid(BestBooksPage.all_links)

        # assert breadcrumbs and page elements
        self.assert_element(BestBooksPage.home)
        self.assert_element(BestBooksPage.books_and_more)
        self.assert_element(BestBooksPage.recommendations)
        self.assert_element(BestBooksPage.h1_heading)
        self.assert_true("Best Books" in self.get_text(BestBooksPage.h1_heading))
        self.assert_element(BestBooksPage.teens_tab)
        self.assert_element(BestBooksPage.submit)
        self.assert_element(BestBooksPage.filter_results_below)
        self.assert_element(BestBooksPage.additional_info_h3)
        self.wait(1)

        # assert left side filter
        self.assert_left_side_filters(BestBooksPage)

        # assert book number in the page >= 1
        h3_amount = int(self.get_text(BestBooksPage.book_results).split()[0])  # book result amount
        print("\nBook result amount is = " + str(h3_amount))  # optional print of the amount seen in h3 element
        # optional print of the number of the displayed books in the page
        self.assert_true(h3_amount >= 1, "Adults book number and amount no >= 1")

    def test_best_books_kids(self):
        # https://www.nypl.org/books-more/recommendations/best-books/kids
        print('test_best_books_kids()\n')
        self.open_best_books_page(category='kids')

        # assert images on the page
        self.image_assertion()

        # assert all links on the page
        self.assert_links_valid(BestBooksPage.all_links)

        # assert breadcrumbs and page elements
        self.assert_element(BestBooksPage.home)
        self.assert_element(BestBooksPage.books_and_more)
        self.assert_element(BestBooksPage.recommendations)
        self.assert_element(BestBooksPage.h1_heading)
        self.assert_true("Best Books" in self.get_text(BestBooksPage.h1_heading))
        self.assert_element(BestBooksPage.kids_tab)
        self.assert_element(BestBooksPage.submit)
        self.assert_element(BestBooksPage.filter_results_below)
        self.assert_element(BestBooksPage.additional_info_h3)
        self.wait(1)

        # assert left side filter
        self.assert_left_side_filters(BestBooksPage)

        # assert book number in the page >= 1
        h3_amount = int(self.get_text(BestBooksPage.book_results).split()[0])  # book result amount
        print("\nBook result amount is = " + str(h3_amount))  # optional print of the amount seen in h3 element
        # optional print of the number of the displayed books in the page
        self.assert_true(h3_amount >= 1, "Adults book number and amount no >= 1")

    def test_best_books_year_dropdown(self):
        # https://www.nypl.org/books-more/recommendations/best-books/adults
        print('test_best_books_year_dropdown()\n')

        # asserting the year in h2 heading matches selected year on the dropdown

        # asserting adults
        self.open_best_books_page(category='adults')
        # getting the year from h2 heading
        h2_heading_year = (self.get_text(BestBooksPage.h2_heading_best_books).split())
        # getting the selected year
        selected_year = self.get_text(BestBooksPage.selected_year)
        # optional printing both years to see
        print(h2_heading_year)
        print(self.get_text(BestBooksPage.selected_year))
        # asserting both years
        self.assert_true(selected_year in h2_heading_year, "selected year was not found in the h2 heading")

        # asserting teens
        self.open_best_books_page(category='teens')
        # getting the year from h2 heading
        h2_heading_year = (self.get_text(BestBooksPage.h2_heading_best_books).split())
        # getting the selected year
        selected_year = self.get_text(BestBooksPage.selected_year)
        # optional printing both years to see
        print(h2_heading_year)
        print(self.get_text(BestBooksPage.selected_year))
        # asserting both years
        self.assert_true(selected_year in h2_heading_year, "selected year was not found in the h2 heading")

        # asserting kids
        self.open_best_books_page(category='kids')
        # getting the year from h2 heading
        h2_heading_year = (self.get_text(BestBooksPage.h2_heading_best_books).split())
        # getting the selected year
        selected_year = self.get_text(BestBooksPage.selected_year)
        # optional printing both years to see
        print(h2_heading_year)
        print(self.get_text(BestBooksPage.selected_year))
        # asserting both years
        self.assert_true(selected_year in h2_heading_year, "selected year was not found in the h2 heading")
