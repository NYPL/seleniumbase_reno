from selenium.common import NoSuchElementException

from examples.nypl_pages.page_schwarzman import SchwarzmanPage
from examples.nypl_utility.utility import NyplUtils


class Schwarzman(NyplUtils):

    # https://www.nypl.org/locations/schwarzman

    def setUp(self):
        super().setUp()
        print("=================================")
        print("\nRUNNING BEFORE EACH TEST")

        # open blog page
        self.open_schwarzman_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_schwarzman_main(self):
        print("test_schwarzman_main()\n")

        # asserting the images on the page
        self.image_assertion()

        # asserting title
        self.assert_title("Stephen A. Schwarzman Building | The New York Public Library")

        # assert breadcrumbs and hero
        self.assert_element(SchwarzmanPage.home)
        self.assert_element(SchwarzmanPage.hero)

        # assert 'Visit' and 'Research' tabs
        self.assert_element(SchwarzmanPage.visit)
        self.assert_element(SchwarzmanPage.research)

        # assert all links on the page
        self.assert_links_valid(SchwarzmanPage.all_links)

    def test_schwarzman_research(self):
        print("test_schwarzman_research()")

        # clicking the 'Research' tab
        self.click(SchwarzmanPage.research)

        # assert title
        self.assert_title("Research at Stephen A. Schwarzman Building | The New York Public Library")

        # asserting the images on the page
        self.image_assertion()

        # assert all links on the page
        self.assert_links_valid(SchwarzmanPage.all_links)
        # todo: update the assert_links_valid function so it wouldnt get bottom nav links like "Mor at NYPL" etc

    def test_schwarzman_left_sidebar(self):
        # assert address in the left panel
        expected_address = "Fifth Avenue and 42nd Street"
        actual_address = self.get_text(SchwarzmanPage.address)
        print(actual_address)
        self.assert_true(expected_address in actual_address,
                         "Actual " + expected_address + " doesn't match the expected " + actual_address)

        # assert holiday closings using 'link_assertion' method from utility.py
        self.link_assertion(SchwarzmanPage.holiday_closings, "nypl.org/help/closings")  # assert holiday schedule
