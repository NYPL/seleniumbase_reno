from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_snfl_teen import SnflTeenPage


class SnflTeenTest(NyplUtils):

    # https://www.nypl.org/locations/snfl/teen

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open main page
        self.open_snfl_teen_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_snfl_teen_main(self):
        print("test_snfl_teen_main()\n")

        # assert title
        self.assert_title('Teen Center | The New York Public Library')

        # assert images on the page
        self.image_assertion()

        # assert breadcrumbs
        self.assert_element(SnflTeenPage.home)
        self.assert_element(SnflTeenPage.locations)
        self.assert_element(SnflTeenPage.snfl)

        # assert all links on the page
        self.assert_links_valid(SnflTeenPage.all_links)

        # assert left directions pane
        self.assert_element(SnflTeenPage.directions)
        self.assert_element(SnflTeenPage.holiday_closings)
        self.assert_element(SnflTeenPage.give)
        self.assert_element(SnflTeenPage.social_media)
        self.assert_element(SnflTeenPage.email)


