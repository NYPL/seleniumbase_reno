from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_sf_visit import VisitPage


class VisitTest(NyplUtils):

    # https://www.nypl.org/visit

    def setUp(self):
        super().setUp()
        print("=================================")
        print("\nRUNNING BEFORE EACH TEST")

        # open visit page
        self.open_visit_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_visit(self):
        # https://www.nypl.org/visit
        print("test_sf_visit()\n")

        # # check images on the page
        # self.image_assertion()

        # asserting breadcrumbs and page elements
        self.assert_element(VisitPage.home)
        self.assert_element(VisitPage.visit)
        self.assert_element(VisitPage.h1)

        # # assert title
        self.assert_title(VisitPage.visit_title)

        # assert all links on the page
        # self.assert_links_valid(VisitPage.all_links)

        # assert Newsletter Subscription
        self.assert_newsletter_signup(VisitPage)

        # assert social media links (Twitter, Instagram, Facebook)
        # self.assert_element(VisitPage.follow_us_twitter)  # does not consist as of 6/10/2025
        self.assert_element(VisitPage.follow_us_instagram)
        self.assert_element(VisitPage.follow_us_facebook)
