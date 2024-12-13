from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_sf_early_literacy import EarlyLiteracyPage


class EarlyLiteracyTest(NyplUtils):

    # https://www.nypl.org/education/early-literacy

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        self.set_window_size(1920, 1080)

        # open main page
        self.open_early_literacy_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_early_literacy(self):
        print("test_early_literacy()\n")

        # assert title
        self.assert_title(EarlyLiteracyPage.title)

        # assert images on the page
        self.image_assertion()

        # assert all links on the page
        self.assert_links_valid(EarlyLiteracyPage.all_links)

        # assert breadcrumbs
        self.assert_element(EarlyLiteracyPage.home_button)  # home
        self.assert_element(EarlyLiteracyPage.education)  # education

        # assert Newsletter Subscription
        self.assert_newsletter_signup(EarlyLiteracyPage)
        