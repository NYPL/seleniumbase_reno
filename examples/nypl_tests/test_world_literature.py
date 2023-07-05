from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_world_litetature import WorldLiteraturePage


class WorldLiteratureTest(NyplUtils):

    # https://www.nypl.org/spotlight/world-literature-festival

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open world literature page
        self.open_world_literature_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")

        super().tearDown()

    def test_world_literature(self):
        print("test_world_literature()\n")

        # check images on the page
        self.image_assertion()

        # assert title
        self.assert_title(WorldLiteraturePage.world_literature_title)

        # asserting breadcrumbs
        self.assert_element(WorldLiteraturePage.home)  # assert home breadcrumb
        self.assert_element(WorldLiteraturePage.spotlight)  # assert events breadcrumb

        # asserting hero
        self.assert_element(WorldLiteraturePage.hero)

        # asserting the links in "Authors in Conversation"
        talks_link_amount = len(self.find_elements(WorldLiteraturePage.authors_in_conversation_links))
        # print(talks_link_amount)  # optional print
        self.assert_true(talks_link_amount >= 1, "no links or conversations on Authors in Conversation")

        # asserting the links in "Panel Events"
        panel_events_link_amount = len(self.find_elements(WorldLiteraturePage.panel_events__links))
        # print(panel_events_link_amount)  # optional print
        self.assert_true(panel_events_link_amount >= 1, "no events link on Panel Events")

        # asserting the links in "Live From NYPL"
        live_from_nypl_link_amount = len(self.find_elements(WorldLiteraturePage.live_from_nypl_links))
        # print(live_from_nypl_link_amount)  # optional print
        self.assert_true(live_from_nypl_link_amount >= 1, "no events link on Live From NYPL")

        # asserting "Explore All Events" link
        self.link_assertion(WorldLiteraturePage.explore_all_events, "events")
        # asserting "Reading Recommendations" link
        self.link_assertion(WorldLiteraturePage.reading_recommendations, "blog")

        # asserting the link amount in "Multilingual Resources at the..."
        multilingual_resources__link_amount = len(self.find_elements(WorldLiteraturePage.multilingual_resources))
        # print(multilingual_resources__link_amount)  # optional print
        self.assert_true(multilingual_resources__link_amount >= 1, "no events link on Multilingual Resources...")
        # asserting "Multilingual Resources" links
        # list of multilingual resources links to compare in the for loop
        multilingual_resources_resources_links = ["nypl.org/spotlight/multilingual",
                                                  "nypl.org/spotlight/multilingual/bn",
                                                  "nypl.org/spotlight/multilingual/zh",
                                                  "nypl.org/spotlight/multilingual/fr",
                                                  "nypl.org/spotlight/multilingual/it",
                                                  "nypl.org/spotlight/multilingual/ja",
                                                  "nypl.org/spotlight/multilingual/ko",
                                                  "nypl.org/spotlight/multilingual/ru",
                                                  "nypl.org/spotlight/multilingual/es"]
        # loop to compare links in teen center resources, using link_assertion utility function
        for y in range(1, 10):
            self.link_assertion(f"(//*[contains(text(), 'Multilingual')]//parent::h2//following-sibling::div//a)[{y}]",
                                multilingual_resources_resources_links[y - 1])

        # asserting "Recommended: Literature in Translation" link
        self.link_assertion(WorldLiteraturePage.recommended_literature, "recommended-translations")

        # asserting "Top Checkouts in World Languages" link
        self.link_assertion(WorldLiteraturePage.top_checkouts, "top-checkouts")

        # asserting the links in "Learn a language"
        learn_a_language_nypl_link_amount = len(self.find_elements(WorldLiteraturePage.learn_a_language))
        # print(learn_a_language_nypl_link_amount)  # optional print
        self.assert_true(learn_a_language_nypl_link_amount >= 1, "no events link on Learn a Language...")

        # asserting "Highlights from the 2022..." link
        self.link_assertion(WorldLiteraturePage.highlights_from, "recommendations")

        # asserting "Get a Digital Library Card" link
        self.link_assertion(WorldLiteraturePage.get_a_digital_lib_card, "library-card")

        # asserting "Download the NYPL App" link
        self.link_assertion(WorldLiteraturePage.download_the_nypl_app, "app")

        # asserting "Get Started with SimplyE" link
        self.link_assertion(WorldLiteraturePage.get_started_with_simplyE, "simplye")

        # asserting "Get Help" link
        self.link_assertion(WorldLiteraturePage.get_help, "contact-us")

        # asserting "Get Help" link
        self.link_assertion(WorldLiteraturePage.get_help, "contact-us")

        # asserting the links in "Connect with the Library"
        connect_with_the_library_link_amount = len(self.find_elements(WorldLiteraturePage.connect_with_the_library))
        # print(connect_with_the_library_link_amount)  # optional print
        self.assert_true(connect_with_the_library_link_amount >= 1, "no links on Connect wth the Library")

        # asserting "Help us Support All New yorkers" link
        self.link_assertion(WorldLiteraturePage.help_us_support, "Donation")



