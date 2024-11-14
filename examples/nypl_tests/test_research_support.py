import requests
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException

from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_research_support import ResearchSupportPage


class ResearchSupportTest(NyplUtils):

    # https://www.nypl.org/research/support

    def setUp(self):
        super().setUp()
        #print("=================================")
        #print("\nRUNNING BEFORE EACH TEST")

        # open research page
        self.open_research_support_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_research_support_main(self):
        print("test_main_page()\n")

        # asserting the images on the page
        self.image_assertion()

        # assert breadcrumbs
        self.assert_element(ResearchSupportPage.home)
        self.assert_element(ResearchSupportPage.research)

        # assert hero
        self.assert_element(ResearchSupportPage.h1)

        # assert all links on the page
        self.assert_links_valid(ResearchSupportPage.all_links)

        # assert Newsletter Subscription
        self.assert_newsletter_signup(ResearchSupportPage)

