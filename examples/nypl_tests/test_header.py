import pytest
import os
import re

import requests
from dotenv import load_dotenv

from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_header import HeaderPage

# Load environment variables from .env file
load_dotenv()


class HeaderTest(NyplUtils):
    # https://www.nypl.org/

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open main page
        self.open_home_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")

        super().tearDown()

    @pytest.mark.smoke
    def test_header_main(self):
        print("test_header()\n")

        # assert NYPL LOGO
        self.assert_element(HeaderPage.lion_logo)

        # assert LOGIN tab
        self.assert_element(HeaderPage.login_button)

        # assert LOCATIONS tab
        self.link_assertion(HeaderPage.locations, "locations")

        # assert GET A LIBRARY CARD tab
        self.link_assertion(HeaderPage.get_a_library_card, "card")

        # assert GET EMAIL UPDATES tab
        self.link_assertion(HeaderPage.get_email_updates, "email")

        # assert DONATE tab
        self.link_assertion(HeaderPage.donate, "Donation")

        # assert SHOP tab
        self.link_assertion(HeaderPage.shop, "shop")

        # assert Books/Music/Movies
        self.link_assertion(HeaderPage.books_music_movies, "books")

        # assert Research
        self.link_assertion(HeaderPage.research, "research")

        # assert Education
        self.link_assertion(HeaderPage.education, "education")

        # assert Events
        self.link_assertion(HeaderPage.events, "events")

        # assert Connect
        self.link_assertion(HeaderPage.connect, "connect")

        # assert Give
        self.link_assertion(HeaderPage.give, "give")

        # assert Get Help
        self.link_assertion(HeaderPage.get_help, "help")

        # assert Search
        self.click(HeaderPage.search_button)
        self.assert_text("Close")

    # @pytest.mark.skip(reason="Chris covering this in his RC automation suite")
    @pytest.mark.smoke
    def test_login_catalog(self):
        print("test_login_catalog()\n")

        # Retrieve username and password from environment variables
        username = os.getenv('CATALOG_USERNAME')
        password = os.getenv('CATALOG_PASSWORD')

        # Debug print statements to check if the variables are set
        # print(f"Username: {username}")
        # print(f"Password: {password}")

        # Ensure username and password are not None
        if not username or not password:
            raise Exception("Environment variables USERNAME and PASSWORD must be set!")

        # Proceed with the login process
        self.nypl_login_catalog(username, password)

        # assert that the login is successful and the new URL is 'https://borrow.nypl.org/'
        try:
            print(self.get_current_url())
            assert 'borrow' in self.get_current_url()
        except AssertionError:
            print("in except clause, trying again after waiting for a few seconds...")
            self.wait(3)  # wait and try again
            print(self.get_current_url())
            assert 'borrow' in self.get_current_url()
        # assert title 'NYPL catalog'
        self.assert_title('New York Public Library')

        # assert Overview tab in sidebar
        self.assert_element(HeaderPage.my_bookshelf)

    @pytest.mark.skip(reason="Chris covering this in his RC automation suite")
    @pytest.mark.smoke
    def test_research_catalog(self):
        print("test_research_catalog()\n")

        # Retrieve username and password from environment variables
        username = os.getenv('CATALOG_USERNAME')
        password = os.getenv('CATALOG_PASSWORD')

        # Ensure username and password are not None
        if not username or not password:
            raise Exception("Environment variables USERNAME and PASSWORD must be set!")

        # Debug print statements to check if the variables are set
        print(f"Username: {username}")
        print(f"Password: {password}")

        # Proceed with the login process
        self.nypl_login_research(username, password)

        self.wait(2)
        # assert title 'Account | Research Catalog | NYPL'
        self.assert_title('My Account')
        # assert 'My Account' h2 element for Research Catalog
        self.assert_element(HeaderPage.my_account_research_catalog)

        # assert tabs

        # assert 'Search' tab
        self.assert_element(HeaderPage.catalog_search_tab)
        # assert 'Subject Heading Explorer'
        self.assert_element(HeaderPage.subject_heading_explorer_tab)
        # assert "My Account" tab
        self.assert_element(HeaderPage.my_account_tab)
        # assert "Log Out" tab
        self.assert_element(HeaderPage.log_out_tab)

        # assert 'Checkouts' tab
        self.assert_element(HeaderPage.checkouts_tab)
        # assert 'Requests" tab
        self.assert_element(HeaderPage.requests_tab)
        # assert 'Account settings' tab
        self.assert_element(HeaderPage.account_settings_tab)

        # assert search functionality
        # search for a keyword
        keyword = "book"
        self.click(HeaderPage.catalog_search_tab)
        self.send_keys(HeaderPage.research_catalog_searchbar, keyword)  # search for a title
        self.send_keys(HeaderPage.research_catalog_searchbar, Keys.ENTER)  # press Enter

        # assert title
        try:
            self.assert_title('Search Results | Research Catalog | NYPL')
        except AssertionError:
            print("Title assertion failed. Waiting for 3 seconds before retrying...")
            self.wait(3)
            # Optionally, you can retry the assertion or perform other actions here
            self.assert_title('Search Results | Research Catalog | NYPL')  # Retry assertion

        # assert the h2 result display
        self.assert_element(HeaderPage.h2_display_result)

        # click logout
        try:
            self.click(HeaderPage.research_catalog_logout)  # attempt to click logout
        except NoSuchElementException:
            print("inside except block, will wait for a few seconds")
            self.wait(3)
            self.click(HeaderPage.research_catalog_logout)  # retry clicking logout after waiting for 2 seconds

    @pytest.mark.smoke
    def test_search_books_music_movies(self):
        # asserting the search results with keywords
        self.click(HeaderPage.search_tab)
        keyword = 'midtown'.lower()  # keyword in lowercase
        print("keyword: " + keyword)  # optional print
        self.click(HeaderPage.circulating_catalog)
        self.send_keys(HeaderPage.search_bar, keyword)  # searching for keyword
        self.click(HeaderPage.search_submit_button)  # submitting the keyword

        try:
            print(self.get_current_url())
            assert 'borrow' in self.get_current_url()
        except AssertionError:
            print("in except clause, trying again after waiting for a few seconds...")
            self.wait(3)  # wait and try again
            print(self.get_current_url())
            assert 'borrow' in self.get_current_url()

    @pytest.mark.smoke
    def test_search_research_catalog(self):
        # asserting the search results with keywords
        self.click(HeaderPage.search_tab)
        keyword = 'midtown'.lower()  # keyword in lowercase
        print("keyword: " + keyword)  # optional print
        self.click(HeaderPage.research_catalog)
        self.send_keys(HeaderPage.search_bar, keyword)  # searching for keyword
        self.click(HeaderPage.search_submit_button)  # submitting the keyword


        # assert search results is greater than 0
        # 1- using anchor links amounts
        search_result_amount_1 = len(self.find_elements(HeaderPage.search_result_rc_1))
        print("Search result: " + str(search_result_amount_1))
        self.assert_true(search_result_amount_1 >= 1)

        # 2- using the result text and extracting the number from that
        text = self.get_text(HeaderPage.search_result_rc_2)
        print("Raw result text:", text)  # <--- ADD THIS
        match = re.search(r'(?:about|of)\s+([\d,]+)\s+results', text)
        if match:
            total_results = int(match.group(1).replace(',', ''))
            print("Total results: " + str(total_results))
            self.assert_true(total_results >= 1)
        else:
            self.fail("Could not extract total result count from search result text")

        try:
            print(self.get_current_url())
            assert 'research' in self.get_current_url()
        except AssertionError:
            print("in except clause, trying again after waiting for a few seconds...")
            self.wait(3)  # wait and try again
            print(self.get_current_url())
            assert 'research' in self.get_current_url()

    @pytest.mark.smoke
    def test_search_library_website(self):
        # asserting the search results with keywords
        self.click(HeaderPage.search_tab)
        keyword = 'midtown'.lower()  # keyword in lowercase
        print("keyword: " + keyword)  # optional print
        self.click(HeaderPage.website_search)
        self.send_keys(HeaderPage.search_bar, keyword)  # searching for keyword
        self.click(HeaderPage.search_submit_button)  # submitting the keyword

        # assert search results is greater than 0
        # 1- using anchor links amounts
        search_result_amount_1 = len(self.find_elements(HeaderPage.search_result_slw_1))
        print("Search result: " + str(search_result_amount_1))
        self.assert_true(search_result_amount_1 >= 1)

        # 2- using the result text and extracting the number from that
        text = self.get_text(HeaderPage.search_result_slw_2)
        print("Raw result text:", text)  # <--- ADD THIS
        match = re.search(r'(?:about|of)\s+([\d,]+)\s+results', text)
        if match:
            total_results = int(match.group(1).replace(',', ''))
            print("Total results: " + str(total_results))
            self.assert_true(total_results >= 1)
        else:
            self.fail("Could not extract total result count from search result text")


# todo: left here > add a try except for _1 and _2 locators and also change the library_website assertion
# todo: for the research catalog to be have more depth