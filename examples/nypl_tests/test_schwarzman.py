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

    def test_schwarzman(self):

        # https://www.nypl.org/locations/schwarzman
        print("test_schwarzman()\n")

        # assert breadcrumbs and hero
        self.assert_element(SchwarzmanPage.home)
        self.assert_element(SchwarzmanPage.locations)
        self.assert_element(SchwarzmanPage.hero)

        # assert 'Visit' and 'Research' tabs
        self.assert_element(SchwarzmanPage.visit)
        self.assert_element(SchwarzmanPage.research)
        # asserting title
        self.assert_title("Stephen A. Schwarzman Building | The New York Public Library")

        # assert that clicking on 'directions' and '202x holiday hours' will open the correct page
        # using 'text assertion' method from utility.py
        self.text_assertion(SchwarzmanPage.directions, "google.com/maps")
        self.text_assertion(SchwarzmanPage.holiday_closings, "nypl.org/help/closings")
        self.text_assertion(SchwarzmanPage.research, "nypl.org/locations/schwarzman/research")
        self.text_assertion(SchwarzmanPage.learn_more_link, "nypl.org/locations/schwarzman/research")
