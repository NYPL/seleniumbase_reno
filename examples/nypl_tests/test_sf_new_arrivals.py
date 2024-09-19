from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_sf_new_arrivals import NewArrivalsPage
import pytest


class NewArrivals(NyplUtils):
    # https://www.nypl.org/books-music-movies/new-arrivals

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open new arrivals page
        self.open_new_arrivals_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    @pytest.mark.smoke
    def test_new_arrivals(self):
        # https://www.nypl.org/books-music-movies/new-arrivals
        print("test_new_arrivals()\n")
        # self.open_new_arrivals_page(category='')

        # asserting the images on the page
        self.image_assertion()

        # assert page elements
        self.assert_element(NewArrivalsPage.side_bar_bmm)  # assert sidebar 'Books/Music/Movies' element

        # assert toggle bar
        self.assert_element(NewArrivalsPage.toggle_display)  # assert toggle display bar
        # assert 'new arrivals/on order' toggle
        self.assert_element(NewArrivalsPage.switch_display)  # assert switch display for 'New arrivals/On Order'
        self.assert_element(NewArrivalsPage.new_arrivals)  # assert 'new arrivals' button
        self.assert_element(NewArrivalsPage.on_order)  # assert 'on order' button'
        # assert 'list/grid' toggle
        self.assert_element(NewArrivalsPage.switch_view)  # assert switch display for 'List/Grid' view
        self.assert_element(NewArrivalsPage.list_view)  # assert 'list' button
        self.assert_element(NewArrivalsPage.grid_view)  # assert 'grid' button

