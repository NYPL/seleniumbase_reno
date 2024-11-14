from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_billy_rose import BillyRosePage


class BillyRoseTest(NyplUtils):

    # https://www.nypl.org/locations/lpa/billy-rose-theatre-division

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open main page
        self.open_billy_rose_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_billy_rose_main(self):
        print("test_billy_rose_main()\n")

        # assert title
        self.assert_title('Billy Rose Theatre Division | The New York Public Library')

        # assert images on the page
        self.image_assertion()

        # assert all links on the page
        self.assert_links_valid(BillyRosePage.all_links)

        # assert breadcrumbs
        self.assert_element(BillyRosePage.home)
        self.assert_element(BillyRosePage.locations)
        self.assert_element(BillyRosePage.nypl_performing)

        # assert left directions pane
        self.assert_element(BillyRosePage.directions)
        self.assert_element(BillyRosePage.email)
        self.assert_element(BillyRosePage.holiday_closings)

