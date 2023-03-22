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

    def test_main_page(self):
        print("test_research()\n")

        # asserting the images on the page
        self.image_assertion()