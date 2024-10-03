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

        # assert 'Additional Information' Section by clicking all the links
        additional_info_length = len(self.find_elements(BestBooksPage.additional_info_links))
        print("additional info length is = " + str(additional_info_length))

        for x in range(1, additional_info_length + 1):
            self.assert_page_loads_successfully(BestBooksPage.additional_info_links + "[" + str(x) + "]")

        # assert left side filter number is more than the given amount, == 1
        left_filter_length = len(self.find_elements(BestBooksPage.left_side_filter))
        # optional print of the length of left side filter, 10 as of June 2022
        print("left side filter length is " + str(left_filter_length))
        # assert that filter is greater than wanted amount, 1 for now
        self.assert_true(left_filter_length > 1, "left side filter does not have any result")

        # asserting left side filter content when it is clicked
        for x in range(1, 10):
            x = random.randint(1, left_filter_length)  # choosing a random library in range 1-89 inc.
            filter_text = self.get_text(BestBooksPage.left_side_filter + "[" + str(x) + "]")
            self.click(BestBooksPage.left_side_filter + "[" + str(x) + "]")
            self.wait(1)
            result_text = self.get_text(BestBooksPage.filter_results)
            # assert if the filter text matches the filtered actual text when clicked
            self.assert_true(filter_text in result_text, "clicked '" + filter_text + "' and '" + result_text + "' don't"
                                                                                                               "match")
            # optional print of filters and results
            print(x)  # optional filter number print
            print(filter_text + " =? " + result_text)  # optional filter text vs results text comparison print
            # going back after clicking, receiving and checking the texts
            self.go_back()

        # assert book number in the page == to the amount in the h3
        book_amount = len(self.find_elements(BestBooksPage.total_books_found))
        # amount in the h3
        h3_amount = int(self.get_text(BestBooksPage.book_results).split()[0])
        print("h3 amount is = " + str(h3_amount))  # optional print of the amount seen in h3 element
        # optional print of the number of the displayed books in the page
        print("book amount is = " + str(book_amount))
        self.assert_true(book_amount == h3_amount, "Kids book number and amount in the h3 don't match")

    def test_best_books_teens(self):
        # https://www.nypl.org/books-more/recommendations/best-books/teens
        print('test_best_books_teens()\n')
        self.open_best_books_page(category='teens')

        # assert images on the page
        self.image_assertion()

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

        # assert 'Additional Information' Section by clicking all the links
        additional_info_length = len(self.find_elements(BestBooksPage.additional_info_links))
        print("additional info length is = " + str(additional_info_length))

        for x in range(1, additional_info_length + 1):
            self.assert_page_loads_successfully(BestBooksPage.additional_info_links + "[" + str(x) + "]")

        # assert left side filter number is more than the given amount, == 1
        left_filter_length = len(self.find_elements(BestBooksPage.left_side_filter))
        # optional print of the length of left side filter, 10 as of June 2022
        print("left side filter length is " + str(left_filter_length))
        # assert that filter is greater than wanted amount, 1 for now
        self.assert_true(left_filter_length > 1, "left side filter does not have any result")

        # asserting left side filter content when it is clicked
        for x in range(1, 10):
            x = random.randint(1, left_filter_length)  # choosing a random library in range 1-89 inc.
            filter_text = self.get_text(BestBooksPage.left_side_filter + "[" + str(x) + "]")
            self.click(BestBooksPage.left_side_filter + "[" + str(x) + "]")
            self.wait(1)
            result_text = self.get_text(BestBooksPage.filter_results)
            # assert if the filter text matches the filtered actual text when clicked
            self.assert_true(filter_text in result_text, "clicked '" + filter_text + "' and '" + result_text + "' don't"
                                                                                                               "match")
            # optional print of filters and results
            print(x)  # optional filter number print
            print(filter_text + " =? " + result_text)  # optional filter text vs results text comparison print
            # going back after clicking, receiving and checking the texts
            self.go_back()

        # assert book number in the page == to the amount in the h3
        book_amount = len(self.find_elements(BestBooksPage.total_books_found))
        # amount in the h3
        h3_amount = int(self.get_text(BestBooksPage.book_results).split()[0])
        print("h3 amount is = " + str(h3_amount))  # optional print of the amount seen in h3 element
        # optional print of the number of the displayed books in the page
        print("book amount is = " + str(book_amount))
        self.assert_true(book_amount == h3_amount, "Kids book number and amount in the h3 don't match")

    def test_best_books_kids(self):
        # https://www.nypl.org/books-more/recommendations/best-books/kids
        print('test_best_books_kids()\n')
        self.open_best_books_page(category='kids')

        # assert images on the page
        self.image_assertion()

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

        # assert 'Additional Information' Section by clicking all the links
        additional_info_length = len(self.find_elements(BestBooksPage.additional_info_links))
        print("additional info length is = " + str(additional_info_length))

        for x in range(1, additional_info_length + 1):
            self.assert_page_loads_successfully(BestBooksPage.additional_info_links + "[" + str(x) + "]")

        # assert left side filter number is more than the given amount, == 1
        left_filter_length = len(self.find_elements(BestBooksPage.left_side_filter))
        # optional print of the length of left side filter, 10 as of June 2022
        print("left side filter length is " + str(left_filter_length))
        # assert that filter is greater than wanted amount, 1 for now
        self.assert_true(left_filter_length > 1, "left side filter does not have any result")

        # asserting left side filter content when it is clicked
        for x in range(1, 10):
            x = random.randint(1, left_filter_length)  # choosing a random library in range 1-89 inc.
            filter_text = self.get_text(BestBooksPage.left_side_filter + "[" + str(x) + "]")
            self.click(BestBooksPage.left_side_filter + "[" + str(x) + "]")
            self.wait(1)
            result_text = self.get_text(BestBooksPage.filter_results)
            # assert if the filter text matches the filtered actual text when clicked
            self.assert_true(filter_text in result_text, "clicked '" + filter_text + "' and '" + result_text + "' don't"
                                                                                                               "match")
            # optional print of filters and results
            print(x)  # optional filter number print
            print(filter_text + " =? " + result_text)  # optional filter text vs results text comparison print
            # going back after clicking, receiving and checking the texts
            self.go_back()

        # assert book number in the page == to the amount in the h3
        book_amount = len(self.find_elements(BestBooksPage.total_books_found))
        # amount in the h3
        h3_amount = int(self.get_text(BestBooksPage.book_results).split()[0])
        print("h3 amount is = " + str(h3_amount))  # optional print of the amount seen in h3 element
        # optional print of the number of the displayed books in the page
        print("book amount is = " + str(book_amount))
        self.assert_true(book_amount == h3_amount, "Kids book number and amount in the h3 don't match")

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
