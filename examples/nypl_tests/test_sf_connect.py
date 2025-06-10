from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_sf_connect import ConnectPage


class ConnectTest(NyplUtils):

    # https://www.nypl.org/connect

    def setUp(self):
        super().setUp()
        print("=================================")
        print("\nRUNNING BEFORE EACH TEST")

        # open connect page
        self.open_connect_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_connect(self):
        # https://www.nypl.org/connect
        print("test_sf_connect()\n")

        # # check images on the page
        # self.image_assertion()

        # asserting breadcrumbs and page elements
        self.assert_element(ConnectPage.home)
        self.assert_element(ConnectPage.connect)
        self.assert_element(ConnectPage.h1)

        # # assert title
        self.assert_title(ConnectPage.connect_title)

        # assert all links on the page
        self.assert_links_valid(ConnectPage.all_links)

        # assert Newsletter Subscription
        self.assert_newsletter_signup(ConnectPage)

        # assert social media links (Twitter, Instagram, Facebook)
        # self.assert_element(ConnectPage.follow_us_twitter)  # does not consist as of 6/10/2025
        self.assert_element(ConnectPage.follow_us_instagram)
        self.assert_element(ConnectPage.follow_us_facebook)
