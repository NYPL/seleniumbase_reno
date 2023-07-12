import requests
from selenium.webdriver.common.by import By

from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_research_support import ResearchSupportPage


class ResearchSupportTest(NyplUtils):

    # https://www.nypl.org/research/support

    def setUp(self):
        super().setUp()
        print("=================================")
        print("\nRUNNING BEFORE EACH TEST")

        # open research page
        self.open_research_support_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_main_page(self):
        print("test_main_page()\n")

        # asserting the images on the page
        self.image_assertion()

        # assert breadcrumbs
        self.assert_element(ResearchSupportPage.home)
        self.assert_element(ResearchSupportPage.research)
        self.assert_element(ResearchSupportPage.h1)

        # assert h2 sections
        self.assert_links_valid(ResearchSupportPage.how_to_start_your_search)
        self.assert_links_valid(ResearchSupportPage.additional_info_section)
        self.assert_links_valid(ResearchSupportPage.specialized_support)
        self.assert_links_valid(ResearchSupportPage.additional_research_services)
        self.assert_links_valid(ResearchSupportPage.find_fellowship)
        self.assert_links_valid(ResearchSupportPage.additional_fellowships)

        # assert email subscription
        self.assert_element(ResearchSupportPage.email_subscription)
        self.send_keys(ResearchSupportPage.email_subs_input, "joedoe@gmail.com")
        self.click(ResearchSupportPage.submit_email)
        self.assert_element(ResearchSupportPage.email_subscription)
        self.go_back()



