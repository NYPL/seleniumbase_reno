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

        # social media links assertions with 'link assertion' utility function to verify they go to the correct URL
        self.link_assertion(FooterPage.facebook, "facebook.com/nypl")
        self.link_assertion(FooterPage.twitter, "x.com/nypl")
        self.link_assertion(FooterPage.instagram, "instagram.com/nypl")
        self.link_assertion(FooterPage.youtube, "youtube.com/user/NewYorkPublicLibrary")
