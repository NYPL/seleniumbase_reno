import pytest

from examples.nypl_pages.header_page import Header


class HeaderTest(Header):

    # https://www.nypl.org/

    # todo: add Login functionality

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open blog page
        self.open_home_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")

        super().tearDown()

    def test_header(self):
        print("test_header()\n")

        # assert NYPL LOGO
        self.assert_element(self.lion_logo)

        # assert LOGIN tab
        self.assert_element_present(self.login)
        self.click(self.login)
        self.assert_element(self.login_close)

        # assert LOCATIONS tab
        self.assert_element(self.locations)
        self.click(self.locations)
        self.assert_true('www.nypl.org/locations' in self.get_current_url())
        self.go_back()

        # assert GET A LIBRARY CARD tab
        self.assert_element(self.get_a_library_card)
        self.click(self.get_a_library_card)
        # print(self.get_current_url())
        self.assert_true('www.nypl.org/library-card' in self.get_current_url())
        self.go_back()

        # assert GET EMAIL UPDATES tab
        self.assert_element(self.get_email_updates)
        self.click(self.get_email_updates)
        print(self.get_current_url())
        print(self.get_title())
        self.assert_title(self.get_email_updates_page_title)
        self.go_back()

        # assert DONATE tab
        self.assert_element(self.donate)
        self.click(self.donate)
        self.assert_true("Donation" in self.get_current_url())
        self.go_back()

        # assert SHOP tab
        self.assert_element(self.shop)
        self.click(self.shop)
        self.assert_title(self.shop_page_title)
        self.go_back()

        # assert Books/Music/Movies
        self.assert_element(self.books_music_movies)
        self.click(self.books_music_movies)
        self.assert_title(self.books_music_movies_title)
        self.go_back()

        # assert Research
        self.assert_element(self.research)
        self.click(self.research)
        self.assert_title(self.research_title)
        self.go_back()

        # assert Education
        self.assert_element(self.education)
        self.click(self.education)
        self.assert_title(self.education_title)
        self.go_back()

        # assert Events
        self.assert_element(self.events)
        self.click(self.events)
        self.assert_title(self.events_title)
        self.go_back()

        # assert Connect
        self.assert_element(self.connect)
        self.click(self.connect)
        self.assert_title(self.connect_title)
        self.go_back()

        # assert Give
        self.assert_element(self.give)
        self.click(self.give)
        self.assert_title(self.give_title)
        self.go_back()

        # assert Get Help
        self.assert_element(self.get_help)
        self.click(self.get_help)
        self.assert_title(self.get_help_title)
        self.go_back()

        # assert Search
        self.assert_element(self.search)
        self.click(self.search)
        self.assert_text("Close")

    def test_login_catalog(self):
        print("test_login_catalog()\n")

        # click login button
        self.click(self.login)
        # click 'log into the catalog'
        self.click(self.login_catalog)
        # enter username
        self.send_keys(self.username, "qatester")
        # enter password
        self.send_keys(self.password, "1234")
        # click submit
        self.click(self.submit)

        # assert title 'NYPL catalog'
        self.assert_title('NYPL Catalog')
        # assert 'my account' tab
        self.assert_element(self.my_account)
        # click logout
        self.click(self.logout)
        # assert the 'login' button after logging out
        self.assert_element(self.login_back)

        print(self.get_current_url())

    def test_login_research_catalog(self):
        print("test_login_research_catalog()\n")

        # click login button
        self.click(self.login)
        # click log into the research catalog
        self.click(self.login_research_catalog)
        # enter username
        self.send_keys(self.username, "qatester")
        # enter password
        self.send_keys(self.password, "1234")
        # click submit
        self.click(self.submit)

        # assert title 'Account | Research Catalog | NYPL'
        self.assert_title('Account | Research Catalog | NYPL')
        # assert 'My Account' element for Research Catalog
        self.assert_element(self.my_account_research_catalog)
        # assert 'advanced search' button
        self.assert_element(self.advanced_search_research)
        self.click(self.advanced_search_research)
        self.assert_title('Advanced Search | Research Catalog | NYPL')
        # negative test scenario for advanced search without filling the fields and submitting
        self.click(self.advanced_search_research_submit)
        self.assert_element(self.submit_warning)

    @pytest.mark.skip(reason="Chris Mulholland covering this in his own test suite")
    def test_search_functionality(self):
        print("test_search_functionality()\n")

        # click login button
        self.click(self.login)
        # click log into the research catalog
        self.click(self.login_research_catalog)
        # enter username
        self.send_keys(self.username, "qatester")
        # enter password
        self.send_keys(self.password, "1234")
        # click submit
        self.click(self.submit)

        # assert search functionality
        self.click(self.search_research_catalog)
        # self.wait(3)
        print(self.get_current_url())
        # assert title
        self.assert_title('Search Results | Research Catalog | NYPL')
        # assert the h2 result display
        self.assert_element(self.h2_display_result)
        # assert next button
        self.assert_element(self.next_button)
        # click 'next' button
        self.click(self.next_button)
        # click/assert 'previous' button
        self.click(self.previous_button)



