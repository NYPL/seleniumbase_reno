from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_sf_new_arrivals import NewArrivalsPage
import pytest


class NewArrivals(NyplUtils):
    # https://www.nypl.org/books-music-movies/new-arrivals

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # Open new arrivals page
        self.open_new_arrivals_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    @pytest.mark.smoke
    def test_new_arrivals(self):
        # https://www.nypl.org/books-music-movies/new-arrivals
        print("test_new_arrivals()\n")

        # Asserting the images on the page
        self.image_assertion()

        # Assert page elements
        self.assert_element(NewArrivalsPage.side_bar_bmm)  # Assert sidebar/anchor tag 'Books/Music/Movies' element

        # Assert there are books/data on the page
        book_amount = len(self.find_elements(NewArrivalsPage.book_amount))
        # print(book_amount)  # print statement for debugging purposes
        self.assert_true(book_amount >= 1, "No Books displayed on the New Arrivals Page")

        # Assert toggle bar
        self.assert_element(NewArrivalsPage.toggle_display)  # Assert toggle display bar
        # Assert 'new arrivals/on order' toggle
        self.assert_element(NewArrivalsPage.switch_display)  # Assert switch display for 'New arrivals/On Order'
        self.assert_element(NewArrivalsPage.new_arrivals)  # Assert 'new arrivals' button
        self.assert_element(NewArrivalsPage.on_order)  # Assert 'on order' button
        # Assert 'list/grid' toggle
        self.assert_element(NewArrivalsPage.switch_view)  # Assert switch display for 'List/Grid' view
        self.assert_element(NewArrivalsPage.list_view)  # Assert 'list' button
        self.assert_element(NewArrivalsPage.grid_view)  # Assert 'grid' button

        # Assert selected filters apply and return result at the end
        self.click(self.filter_button)  # Click 'Filter' button
        self.click(self.filter_book)  # Click 'Book' filter
        self.click(self.filter_adult)  # Click 'Adult' filter

        self.click(self.filter_spanish)  # Click 'Spanish' filter
        self.click(self.filter_italian)  # Click 'Italian' filter
        self.click(self.filter_arabic)  # Click 'Arabic' filter
        self.click(self.filter_english)  # Click 'English' filter

        # if there is an issue with indexing service that services new-arrivals, it won’t update solr. check below ticket
        # https://newyorkpubliclibrary.atlassian.net/browse/RENO-4463

        self.click(self.filter_fiction)  # Click 'All fiction' filter
        self.click(self.button_apply)  # Click 'Apply' button
        self.assert_element(self.selected_filters)  # Assert the selected filters are present

        # assert the search result is > 1
        search_result_amount = len(self.find_elements(NewArrivalsPage.serch_result))
        print("Search result amount: " + str(search_result_amount))
        self.assert_true(search_result_amount > 1)

        # Assert 'load more' button and click it
        self.assert_element(NewArrivalsPage.load_more_button)  # Assert 'load more' button
        self.click(NewArrivalsPage.load_more_button)  # Click 'load more' button
