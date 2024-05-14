from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_press_individual import PressIndividualPage


class PressIndividualTest(NyplUtils):
    # https://www.nypl.org/press/actress-comedian-tv-host-sherri-shepherd-and-chef-restaurateur-melba-wilson-lead-celebrity

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open main page
        self.open_press_individual_page()

    def tearDown(self):
        print("\nRUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_press_individual_main(self):
        print("test_press_individual()\n")

        # assert title
        self.assert_title(PressIndividualPage.home_title)

        # assert images on the page
        self.image_assertion()

        # assert breadcrumbs
        self.assert_element(PressIndividualPage.home)
        self.assert_element(PressIndividualPage.press_releases)

        # asserting photos anchor link- 'here'
        self.assert_element(PressIndividualPage.photos)  # asserting the element
        self.link_assertion(PressIndividualPage.photos, "drive")  # asserting the link after clicking the element

