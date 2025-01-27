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

        # assert all links on the page
        self.assert_links_valid(WorldLiteraturePage.all_links)
