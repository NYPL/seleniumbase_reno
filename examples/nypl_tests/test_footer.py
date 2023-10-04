from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_footer import FooterPage


class FooterTest(NyplUtils):

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

    def test_footer(self):
        print("test_footer()\n")

        # asserting footer links with link assertion function to verify they go to the correct URL
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

        # print(self.dic["press"])
        # self.assert_element(self.dic[0])

        # assert footer links elements
        links_list = ["accessibility", "press", "careers", "space_rental", "privacy_policy"
            , "other_policies", "terms_conditions", "governance", "rules_regulations"
            , "about_nypl", "language"]

        x = 0
        while x < len(links_list):
            self.assert_element(FooterPage.footer_links_dic["" + links_list[x] + ""])
            x += 1

        # social media assertions
        self.assert_element(FooterPage.facebook)
        self.click(FooterPage.facebook)
        self.assert_true('www.facebook.com/nypl' in self.get_current_url())
        # self.go_back()
        self.open_home_page()

        self.assert_element(FooterPage.twitter)
        self.click(FooterPage.twitter)
        self.assert_true('twitter.com' in self.get_current_url())
        print(self.get_current_url())
        # self.go_back()
        self.open_home_page()

        self.assert_element(FooterPage.instagram)
        self.click(FooterPage.instagram)
        print(self.get_current_url())

        self.assert_true('instagram.com/' in self.get_current_url())

        # self.go_back()
        self.open_home_page()

        self.assert_element(FooterPage.youtube)
        self.click(FooterPage.youtube)
        self.assert_true('www.youtube.com/user/NewYorkPublicLibrary' in self.get_current_url())
        # self.go_back()
        self.open_home_page()
