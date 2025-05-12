import pytest

from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_sf_get_help import GetHelpPage


class GetHelpTest(NyplUtils):

    # https://www.nypl.org/get-help

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # self.set_window_size(1920, 1080)

        # open main page
        self.open_get_help_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_get_help_main(self):
        print("test_get_help_main()\n")

        # assert title
        self.assert_title(GetHelpPage.title)

        # assert images on the page
        self.image_assertion()

        # assert breadcrumbs
        self.assert_element(GetHelpPage.home_button)  # home
        self.assert_element(GetHelpPage.get_help)  # get help

        # assert all links on the page
        self.assert_links_valid(GetHelpPage.all_links)
