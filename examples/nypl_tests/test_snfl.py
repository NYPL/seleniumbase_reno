from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_snfl import SnflPage


class SnflTest(NyplUtils):

    # https://www.nypl.org/locations/snfl

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open main page
        self.open_snfl_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_snfl_main(self):
        print("test_snfl_main()\n")

        # assert title
        self.assert_title('Stavros Niarchos Foundation Library (SNFL) | The New York Public Library')

        # assert images on the page
        self.image_assertion()

        # assert all links on the page
        self.assert_links_valid(SnflPage.all_links)

        # assert breadcrumbs and tabs
        self.assert_element(SnflPage.home)
        self.assert_element(SnflPage.visit)
        self.assert_element(SnflPage.explore)
        self.assert_element(SnflPage.read)

        # assert left directions pane
        self.assert_element(SnflPage.directions)
        self.assert_element(SnflPage.holiday_closings)
        self.assert_element(SnflPage.give)
        self.assert_element(SnflPage.social_media)

        # assert that clicking on 'directions', '202x holiday hours' and links on the page will open the correct pages
        # using 'link_assertion' method from utility.py
        self.link_assertion(SnflPage.directions, "google.com/maps")
        self.link_assertion(SnflPage.holiday_closings, "nypl.org/help/closings")

    def test_snfl_explore(self):
        print("test_snfl_explore()\n")

        # click 'Explore' tab
        self.click(SnflPage.explore)

        print(self.get_title())

        # assert title
        self.assert_title('Explore Stavros Niarchos Foundation Library (SNFL) | The New York Public Library')

        # assert images on the page
        self.image_assertion()

        # assert all links on the page
        self.assert_links_valid(SnflPage.all_links)

    def test_snfl_read(self):
        print("test_snfl_read()\n")

        # click 'Read' tab
        self.click(SnflPage.read)

        print(self.get_title())

        # assert title
        self.assert_title("Stavros Niarchos Foundation Library (SNFL) Reader's Portal | The New York Public Library")

        # assert images on the page
        self.image_assertion()

        # assert all links on the page
        self.assert_links_valid(SnflPage.all_links)

        # assert top checkouts: amount assertion >= 1
        top_checkouts_amount = len(self.find_elements(SnflPage.top_checkouts))
        print("Top checkouts = " + str(top_checkouts_amount))
        self.assert_true(top_checkouts_amount >= 1, "Top checkouts not >= 1, it is " + str(top_checkouts_amount))

        # asser shelf help
        self.assert_element(SnflPage.shelf_help)

