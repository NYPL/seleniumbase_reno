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
        self.assert_element(BookListsPage.adults_tab_adults)
        self.assert_element(BookListsPage.teens_tab_adults)
        self.assert_element(BookListsPage.kids_tab_adults)
        self.assert_element(BookListsPage.filter_results_below)
        self.assert_element(BookListsPage.additional_info)

        # assert left side filter
        self.assert_left_side_filters(BookListsPage)

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

        # assert left side filter
        self.assert_left_side_filters(BookListsPage)

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

        # assert left side filter
        self.assert_left_side_filters(BookListsPage)

        # assert book number in the page equals to 125
        book_amount = len(self.find_elements(BookListsPage.total_books_found))

        # optional print of the number of the displayed books in the page
        print("\nbook amount is = " + str(book_amount))
        self.assert_true(book_amount == 125, "Kids book number is not 125")
