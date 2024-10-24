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

        # assert links underneath h2 sections
        h2_link_amount = len(self.find_elements(self.all_h2_links))
        print("Total h2 links on the page = " + str(h2_link_amount))

        for x in range(1, h2_link_amount + 1):
            print(str(x) + "- " + self.get_current_url())

            link_xpath = f"{self.all_h2_links}[{x}]//a"

            try:
                self.click(link_xpath)  # attempt to click the link
            except NoSuchElementException:
                print("NoSuchElementException occurred. Waiting for 3 seconds and retrying...")
                self.wait(3)
                self.click(link_xpath)  # attempt to click the link again

            self.wait(2)  # wait for the page to load
            print(self.get_current_url())
            self.open_research_support_page()
            print("====================")

        # assert Newsletter Subscription
        self.assert_element(ResearchSupportPage.email_subscription)
        self.send_keys(ResearchSupportPage.email_subs_input, "joedoe@gmail.com")
        self.click(ResearchSupportPage.submit_email)
        self.assert_element(ResearchSupportPage.email_subscription)
        self.go_back()
