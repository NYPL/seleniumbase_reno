import pytest

from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_home import HomePage


class HomePageTest(NyplUtils):

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
    def test_homepage(self):
        print("test_homepage()\n")

        self.image_assertion()
        self.assert_title(HomePage.home_title)
        self.assert_element(HomePage.hero)

        # TODO: Skipping assert_links_valid until the double html issue is resolved on the homepage
        # self.assert_links_valid(HomePage.all_links)

        # Assert all h2 headings and 'See More' buttons
        h2_amount = len(self.find_elements(HomePage.h2_heading))
        for x in range(1, h2_amount + 1):
            self.assert_element(HomePage.h2_heading + "[" + str(x) + "]")

        # 'In the Collection' section has no 'See More' button, so one fewer than h2 elements
        for x in range(1, h2_amount):
            self.assert_element(HomePage.see_more + "[" + str(x) + "]")

        # Test each section's h2 link navigation by name, not position
        if self.is_element_present(HomePage.section_spotlight):
            print("\n=== Testing Spotlight ===")
            self.link_assertion(HomePage.section_spotlight + "//a", "spotlight")
            print("✓ Spotlight link passed\n")

        print("=== Testing What's On ===")
        self.link_assertion(HomePage.section_whats_on + "//a", "events")
        print("✓ What's On link passed\n")

        print("=== Testing Discover ===")
        self.link_assertion(HomePage.section_discover + "//a", "remote")
        print("✓ Discover link passed\n")

        print("=== Testing Staff Picks ===")
        self.link_assertion(HomePage.section_staff_picks + "//a", "staff")
        print("✓ Staff Picks link passed\n")

        print("=== Testing In the Collection ===")
        self.link_assertion(HomePage.section_in_collection + "//a", "borrow")
        print("✓ In the Collection link passed\n")

        print("=== Testing From Our Blog ===")
        self.link_assertion(HomePage.section_blog + "//a", "blog")
        print("✓ From Our Blog link passed\n")

        print("=== Testing Explore More ===")
        self.link_assertion(HomePage.section_explore + "//a", "locations")
        print("✓ Explore More link passed\n")

    @pytest.mark.smoke
    def test_slider(self):
        print("test_slider()\n")

        slide_length = len(self.find_elements(HomePage.new_noteworthy_slide))
        print("slide amount: " + str(slide_length))
        try:
            self.assert_true(slide_length >= 1)
        except AssertionError:
            self.wait(2)
            self.assert_true(slide_length >= 1)

        if not self.is_element_present(HomePage.slide_next):
            print("Slideshow not present on this environment, skipping slider interaction.")
            return

        self.scroll_to(HomePage.slide_next)

        for x in range(5):
            self.js_click(HomePage.slide_next)

        for x in range(3):
            self.js_click(HomePage.slide_prev)
