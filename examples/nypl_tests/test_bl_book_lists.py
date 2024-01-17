from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_bl_book_lists import BookListsPage


class BookLists125(NyplUtils):

    # https://www.nypl.org/books-more/recommendations/125/adults
    # https://www.nypl.org/books-more/recommendations/best-books/adults
    # https://www.nypl.org/books-more/recommendations/staff-picks/adults

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open book lists page
        # self.open_book_lists_page()  # opening URLs from within the tests itself

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")

        super().tearDown()

    def test_125_adults(self):
        # https://www.nypl.org/books-more/recommendations/125/adults
        print('test_125_adults()\n')
        self.open_book_lists_page(category='adults')

        # asserting the images on the page
        self.image_assertion()

        # assert breadcrumbs and page elements
        self.assert_element(BookListsPage.home)
        self.assert_element(BookListsPage.books_and_more)
        self.assert_element(BookListsPage.recommendations)
        self.assert_element(BookListsPage.h1_heading)
        self.assert_element(BookListsPage.adults_tab_adults)
        self.assert_element(BookListsPage.teens_tab_adults)
        self.assert_element(BookListsPage.kids_tab_adults)
        self.assert_element(BookListsPage.filter_results_below)
        self.assert_element(BookListsPage.additional_info)

        # assert left side filter number more than given amount
        left_filter_length = len(self.find_elements(BookListsPage.left_side_filter))
        # optional print of the length of left side filter, 14 as of June 2022
        print("left side filter length is " + str(left_filter_length))
        # assert that filter is greater than wanted amount, 1 for now
        self.assert_true(left_filter_length > 1, "left side filter amount is not greater than 1")

        # assert clicking every left side filter and
        for x in range(1, left_filter_length + 1):
            filter_text = self.get_text(BookListsPage.left_side_filter + '[' + str(x) + ']/span')
            self.click(BookListsPage.left_side_filter + '[' + str(x) + ']')
            self.wait(1)
            result_text = self.get_text(BookListsPage.filter_results)
            # assert if the filter text matches the filtered actual text when clicked
            self.assert_true(filter_text in result_text,
                             "clicked " + filter_text + " and " + result_text + " don't match")
            # optional print of filters and results
            # print(filter_text + " =? " + result_text)
            # going back after clicking, receiving and checking the texts
            self.go_back()

        # assert total book count on the page (125/adults) equal to 125. 125 as of June 2022
        book_amount = len(self.find_elements(BookListsPage.total_books_found))
        # optional print of the number of the displayed books in the page
        print("book amount is = " + str(book_amount))
        self.assert_true(book_amount == 125, "book amount is not more than expected")

    def test_125_teens(self):
        # https://www.nypl.org/books-more/recommendations/125/teens
        print('test_125_teens()\n')
        self.open_book_lists_page(category='teens')

        # asserting the images on the page
        self.image_assertion()

        # asserting teens tab
        self.click(BookListsPage.teens_tab_teens)
        teens_tab_h1_text = self.get_text(BookListsPage.hero_125)
        # print(teens_tab_h1_text)
        self.assert_true("Teens" in teens_tab_h1_text, "Teens was not found in the heading")

        # assert left side filter number more than given amount
        left_filter_length = len(self.find_elements(BookListsPage.left_side_filter))
        # optional print of the length of left side filter, 12 as of June 2022
        print("left side filter length is " + str(left_filter_length))
        # assert that filter is greater than wanted amount, 1 for now
        self.assert_true(left_filter_length > 1, "left side filter amount is not greater than given amount")

        # asserting left side filter amount
        for x in range(1, left_filter_length + 1):
            filter_text = self.get_text(BookListsPage.left_side_filter + '[' + str(x) + ']/span')
            self.click(BookListsPage.left_side_filter + '[' + str(x) + ']')
            self.wait(1)
            result_text = self.get_text(BookListsPage.filter_results)
            # assert if the filter text matches the filtered actual text when clicked
            self.assert_true(filter_text in result_text,
                             "clicked " + filter_text + " and " + result_text + " don't match")
            # optional print of filters and results
            # print(filter_text + " =? " + result_text)
            # going back after clicking, receiving and checking the texts
            self.go_back()

        # assert book number in the page equals to 125
        book_amount = len(self.find_elements(BookListsPage.total_books_found))
        # optional print of the number of the displayed books in the page
        print("book amount is = " + str(book_amount))
        self.assert_true(book_amount == 125, "Teens book number is not 125")

    def test_125_kids(self):
        # https://www.nypl.org/books-more/recommendations/125/kids
        print('test_125_kids()\n')
        self.open_book_lists_page(category='kids')

        # asserting the images on the page
        self.image_assertion()

        # asserting kids tab
        self.click(BookListsPage.kids_tab_kids)
        kids_tab_h1_text = self.get_text(BookListsPage.hero_125)
        # print(kids_tab_h1_text)
        self.assert_true("Kids" in kids_tab_h1_text, "Kids was not found in the heading")

        # assert left side filter number more than given amount
        left_filter_length = len(self.find_elements(BookListsPage.left_side_filter))
        # optional print of the length of left side filter, 17 as of June 2022
        print("left side filter length is " + str(left_filter_length))
        # assert that filter is greater than wanted amount, 1 for now
        self.assert_true(left_filter_length > 1, "left side filter amount is not greater than given amount")

        # asserting left side filter amount
        for x in range(1, left_filter_length + 1):
            filter_text = self.get_text(BookListsPage.left_side_filter + '[' + str(x) + ']/span')
            self.click(BookListsPage.left_side_filter + '[' + str(x) + ']')
            self.wait(1)
            result_text = self.get_text(BookListsPage.filter_results)
            # assert if the filter text matches the filtered actual text when clicked
            self.assert_true(filter_text in result_text,
                             "clicked " + filter_text + " and " + result_text + " don't match")
            # optional print of filters and results
            # print(filter_text + " =? " + result_text)
            # going back after clicking, receiving and checking the texts
            self.go_back()

        # assert book number in the page equals to 125
        book_amount = len(self.find_elements(BookListsPage.total_books_found))

        # optional print of the number of the displayed books in the page
        print("book amount is = " + str(book_amount))
        self.assert_true(book_amount == 125, "Kids book number is not 125")
