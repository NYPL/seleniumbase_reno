import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys

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
        self.click(HeaderPage.search)
        self.assert_text("Close")

    @pytest.mark.skip(reason="Chris Mulholland covering this in his own test suite")
    def test_login_catalog(self):
        print("test_login_catalog()\n")

        # using nypl_login_catalog method to login
        self.nypl_login_catalog("qatester", "Nyplqa1542*")  # barcode: 25555010494130

        # assert title 'NYPL catalog'
        self.assert_title('New York Public Library')
        # assert 'my bookshelf' tab
        self.assert_element(HeaderPage.my_bookshelf)

        # assert search functionality
        # search for a keyword
        keyword = "book"
        self.send_keys(HeaderPage.catalog_searchbar, keyword)  # search for a title
        self.send_keys(HeaderPage.catalog_searchbar, Keys.ENTER)  # press Enter

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
            self.click(HeaderPage.catalog_login)  # retry clicking logout after waiting for 2 seconds
        try:
            self.click(HeaderPage.catalog_logout)  # attempt to click logout
        except NoSuchElementException:
            print("inside except block, will wait for a few seconds")
            self.wait(3)
            self.click(HeaderPage.catalog_logout)  # retry clicking logout after waiting for 2 seconds

    # @pytest.mark.skip(reason="test")
    @pytest.mark.smoke
    def test_research_catalog(self):
        print("test_research_catalog()\n")

        # using nypl_login_catalog method to login
        self.nypl_login_research("qatester", "Nyplqa1542*")  # barcode: 25555010494130

        # assert title 'Account | Research Catalog | NYPL'
        self.assert_title('Account | Research Catalog | NYPL')
        # assert 'My Account' element for Research Catalog
        self.assert_element(HeaderPage.my_account_research_catalog)

        # assert search functionality
        # search for a keyword
        keyword = "book"
        self.send_keys(HeaderPage.research_catalog_searchbar, keyword)  # search for a title
        self.send_keys(HeaderPage.research_catalog_searchbar, Keys.ENTER)  # press Enter

        # assert that 'research' is in the URL on the result page URL
        current_url_text = self.get_current_url()
        print(current_url_text)
        self.assert_true("research" in current_url_text)

        # assert title
        self.assert_title('Search Results | Research Catalog | NYPL')
        # assert the h2 result display
        self.assert_element(HeaderPage.h2_display_result)

        # click logout
        try:
            self.click(HeaderPage.research_catalog_logout)  # attempt to click logout
        except NoSuchElementException:
            print("inside except block, will wait for a few seconds")
            self.wait(3)
            self.click(HeaderPage.research_catalog_logout)  # retry clicking logout after waiting for 2 seconds
