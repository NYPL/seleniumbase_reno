import pytest
from selenium.webdriver.common.keys import Keys
from seleniumbase.common.exceptions import NoSuchElementException

from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_header import HeaderPage


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

    def test_header(self):
        print("test_header()\n")

        # assert NYPL LOGO
        self.assert_element(HeaderPage.lion_logo)

        # assert LOGIN tab
        self.click(HeaderPage.login_button)
        self.assert_element(HeaderPage.login_button)
        self.click(HeaderPage.login_button)

        # assert LOCATIONS tab
        self.click(HeaderPage.locations)
        self.assert_true('www.nypl.org/locations' in self.get_current_url())
        self.go_back()

        # assert GET A LIBRARY CARD tab
        self.click(HeaderPage.get_a_library_card)
        # print(self.get_current_url())
        self.assert_true('www.nypl.org/library-card' in self.get_current_url())
        self.go_back()

        # assert GET EMAIL UPDATES tab
        self.click(HeaderPage.get_email_updates)
        print(self.get_current_url())
        print(self.get_title())
        self.assert_title(HeaderPage.get_email_updates_page_title)
        self.go_back()

        # assert DONATE tab
        self.assert_element(HeaderPage.donate)
        self.click(HeaderPage.donate)
        self.assert_true("Donation" in self.get_current_url())
        self.go_back()

        # assert SHOP tab
        self.assert_element(HeaderPage.shop)
        self.click(HeaderPage.shop)
        self.assert_title(HeaderPage.shop_page_title)
        self.go_back()

        # assert Books/Music/Movies
        self.assert_element(HeaderPage.books_music_movies)
        self.click(HeaderPage.books_music_movies)
        self.assert_title(HeaderPage.books_music_movies_title)
        self.go_back()

        # assert Research
        self.assert_element(HeaderPage.research)
        self.click(HeaderPage.research)
        self.assert_title(HeaderPage.research_title)
        self.go_back()

        # assert Education
        self.assert_element(HeaderPage.education)
        self.click(HeaderPage.education)
        self.assert_title(HeaderPage.education_title)
        self.go_back()

        # assert Events
        self.assert_element(HeaderPage.events)
        self.click(HeaderPage.events)
        self.assert_title(HeaderPage.events_title)
        self.go_back()

        # assert Connect
        self.assert_element(HeaderPage.connect)
        self.click(HeaderPage.connect)
        self.assert_title(HeaderPage.connect_title)
        self.go_back()

        # assert Give
        self.assert_element(HeaderPage.give)
        self.click(HeaderPage.give)
        self.assert_title(HeaderPage.give_title)
        self.go_back()

        # assert Get Help
        self.assert_element(HeaderPage.get_help)
        self.click(HeaderPage.get_help)
        self.assert_title(HeaderPage.get_help_title)
        self.go_back()

        # assert Search
        self.assert_element(HeaderPage.search)
        self.click(HeaderPage.search)
        self.assert_text("Close")

    # @pytest.mark.skip(reason="Chris Mulholland covering this in his own test suite")
    def test_login_catalog(self):
        print("test_login_catalog()\n")

        # using nypl_login_catalog method to login
        self.nypl_login_catalog("qatester", "1234")

        # assert title 'NYPL catalog'
        self.assert_title('New York Public Library')
        # assert 'my bookshelf' tab
        self.assert_element(HeaderPage.my_bookshelf)

        # assert search functionality
        # search for a keyword
        keyword = "book"
        self.send_keys(HeaderPage.catalog_search_bar, keyword)  # search for a title
        self.send_keys(HeaderPage.catalog_search_bar, Keys.ENTER)  # press Enter

        # assert that 'vega' is in the URL on the result page URL
        current_url_text = self.get_current_url()
        print(current_url_text)
        self.assert_true("vega" in current_url_text)

        # click logout
        try:
            self.click(HeaderPage.catalog_login)  # attempt to click logout
        except NoSuchElementException:
            print("inside except block, will wait for a few seconds")
            self.wait(3)
            self.click(HeaderPage.catalog_logout)  # retry clicking logout after waiting for 2 seconds
        try:
            self.click(HeaderPage.catalog_logout)  # attempt to click logout
        except NoSuchElementException:
            print("inside except block, will wait for a few seconds")
            self.wait(3)
            self.click(HeaderPage.catalog_logout)  # retry clicking logout after waiting for 2 seconds

    # @pytest.mark.skip(reason="test")
    def test_research_catalog(self):
        print("test_research_catalog()\n")

        # using nypl_login_research method to login
        self.nypl_login_research("qatester", "1234")

        # assert title 'Account | Research Catalog | NYPL'
        self.assert_title('Account | Research Catalog | NYPL')
        # assert 'My Account' element for Research Catalog
        self.assert_element(HeaderPage.my_account_research_catalog)

        # assert search functionality
        self.send_keys(HeaderPage.research_catalog_search_bar, "book")  # search for a book
        self.click(HeaderPage.search_research_catalog)  # click the search button
        # self.wait(3)
        print(self.get_current_url())  # get the current URL printed
        # assert title
        self.assert_title('Search Results | Research Catalog | NYPL')
        # assert the h2 result display
        self.assert_element(HeaderPage.h2_display_result)
        # assert next button
        self.assert_element(HeaderPage.next_button)
        # click 'next' button
        self.click(HeaderPage.next_button)
        # click/assert 'previous' button
        self.click(HeaderPage.previous_button)
