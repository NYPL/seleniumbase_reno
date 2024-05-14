import pytest

from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_footer import FooterPage


class FooterTest(NyplUtils):

    # https://www.nypl.org/

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open home page
        self.open_home_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    @pytest.mark.smoke
    def test_footer(self):
        print("test_footer()\n")

        # asserting footer links with 'link assertion' utility function to verify they go to the correct URL
        self.link_assertion(FooterPage.accessibility, "access")
        self.link_assertion(FooterPage.press, "press")
        self.link_assertion(FooterPage.careers, "pinpointhq")
        self.link_assertion(FooterPage.space_rental, "space")
        self.link_assertion(FooterPage.privacy_policy, "privacy")
        self.link_assertion(FooterPage.other_policies, "policies")
        self.link_assertion(FooterPage.terms_conditions, "terms")
        self.link_assertion(FooterPage.governance, "trustees")
        self.link_assertion(FooterPage.rules_regulations, "policies")
        self.link_assertion(FooterPage.about_nypl, "about")
        self.link_assertion(FooterPage.language, "language")

        # social media links assertions
        # assert facebook
        self.assert_element(FooterPage.facebook)
        self.click(FooterPage.facebook)
        self.assert_true('www.facebook.com/nypl' in self.get_current_url())
        # print(self.get_current_url())  # optional print
        self.open_home_page()

        # assert twitter
        self.assert_element(FooterPage.twitter)
        self.click(FooterPage.twitter)
        self.assert_true('twitter.com' in self.get_current_url())
        # print(self.get_current_url())  # optional print
        self.open_home_page()

        # assert instagram
        self.assert_element(FooterPage.instagram)
        self.click(FooterPage.instagram)
        self.assert_true('instagram.com/' in self.get_current_url())
        # print(self.get_current_url())  # optional print
        self.open_home_page()

        # assert youtube
        self.assert_element(FooterPage.youtube)
        self.click(FooterPage.youtube)
        self.assert_true('www.youtube.com/user/NewYorkPublicLibrary' in self.get_current_url())
        # print(self.get_current_url())  # optional print
        self.open_home_page()
