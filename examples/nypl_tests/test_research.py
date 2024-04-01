from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_research import ResearchPage


class ResearchTest(NyplUtils):

    # https://www.nypl.org/research

    def setUp(self):
        super().setUp()
        print("=================================")
        print("\nRUNNING BEFORE EACH TEST")

        # open research page
        self.open_research_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_research_main(self):
        print("test_main_page()\n")

        # asserting the images on the page
        self.image_assertion()

        # assert breadcrumbs
        self.assert_element(ResearchPage.home)
        self.assert_element(ResearchPage.research)
        self.assert_element(ResearchPage.h1)

        # assert search the research catalog
        self.assert_element(ResearchPage.search_the_research_catalog)
        self.send_keys(ResearchPage.search_bar, "catcher in the rye")
        self.click(ResearchPage.search_button)
        self.assert_title("Search Results | Research Catalog | NYPL")
        self.go_back()

        # assert h2 sections
        self.assert_links_valid(ResearchPage.start_your_research)
        self.assert_links_valid(ResearchPage.visit_the_library_research_center)
        self.assert_links_valid(ResearchPage.other_centers)
        self.assert_links_valid(ResearchPage.explore_exhibitions_events)
        self.assert_links_valid(ResearchPage.find_fellowships)
        self.assert_links_valid(ResearchPage.get_research_support)

        # assert email subscription
        self.assert_element(ResearchPage.email_subscription)
        self.send_keys(ResearchPage.email_subs_input, "joedoe@gmail.com")
        self.click(ResearchPage.submit_email)
        self.assert_element(ResearchPage.email_subscription)
        self.go_back()