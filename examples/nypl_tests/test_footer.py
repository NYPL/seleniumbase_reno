from examples.nypl_pages.page_footer import Footer


class FooterTest(Footer):

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
        # assert nypl logo
        self.assert_element(self.nypl_logo)
        # assert main building image
        self.assert_element(self.main_building_image)

        # assert links
        links_list = ["accessibility", "press", "careers", "space_rental", "privacy_policy"
            , "other_policies", "terms_conditions", "governance", "rules_regulations"
            , "about_nypl", "language"]

        # print(self.dic["press"])
        # self.assert_element(self.dic[0])

        x = 0
        while x < len(links_list):
            self.assert_element(self.footer_links_dic["" + links_list[x] + ""])
            x += 1

        # social media assertions
        social_media = ["facebook", "twitter", "instagram", "youtube"]

        self.assert_element(self.facebook)
        self.click(self.facebook)
        self.assert_true('https://www.facebook.com/nypl' in self.get_current_url())
        # self.go_back()
        self.open_home_page()

        self.assert_element(self.twitter)
        self.click(self.twitter)
        self.assert_true('https://twitter.com/nypl' in self.get_current_url())
        print(self.get_current_url())
        # self.go_back()
        self.open_home_page()

        self.assert_element(self.instagram)
        self.click(self.instagram)
        print(self.get_current_url())

        self.assert_true('instagram.com/' in self.get_current_url())

        # self.go_back()
        self.open_home_page()

        self.assert_element(self.youtube)
        self.click(self.youtube)
        self.assert_true('https://www.youtube.com/user/NewYorkPublicLibrary' in self.get_current_url())
        # self.go_back()
        self.open_home_page()
