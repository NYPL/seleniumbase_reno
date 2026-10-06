from utility.utility import NyplUtils
from pages.page_research import ResearchPage


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

        # assert all links on the page
        self.assert_links_valid(ResearchPage.all_links)

        # assert Newsletter Subscription
        self.assert_newsletter_signup(ResearchPage)

        # assert search the research catalog
        self.assert_element(ResearchPage.search_the_research_catalog)
        research_url = self.get_current_url()  # Capture URL before search
        self.send_keys(ResearchPage.search_bar, "catcher in the rye")
        self.click(ResearchPage.search_button)
        # high-level check: the search moved to a results page that loaded OK (not its exact title)
        self.assert_navigated_from(research_url)
