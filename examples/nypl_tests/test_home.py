import pytest
from selenium.common.exceptions import NoSuchElementException

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

        # Test each h2 link navigation
        print("\n=== Testing H2 Link #1: Spotlight ===")
        self.link_assertion(HomePage.h2_heading + "[1]//a", "spotlight")
        print("✓ Spotlight link passed\n")
        
        print("=== Testing H2 Link #2: Events ===")
        self.link_assertion(HomePage.h2_heading + "[2]//a", "events")
        print("✓ Events link passed\n")
        
        print("=== Testing H2 Link #3: Remote ===")
        self.link_assertion(HomePage.h2_heading + "[3]//a", "remote")
        print("✓ Remote link passed\n")
        
        print("=== Testing H2 Link #4: Staff Picks ===")
        self.link_assertion(HomePage.h2_heading + "[4]//a", "staff")
        print("✓ Staff Picks link passed\n")
        
        print("=== Testing H2 Link #5: Borrow ===")
        self.link_assertion(HomePage.h2_heading + "[5]//a", "borrow")
        print("✓ Borrow link passed\n")
        
        print("=== Testing H2 Link #6: Blog ===")
        self.link_assertion(HomePage.h2_heading + "[6]//a", "blog")
        print("✓ Blog link passed\n")
        
        print("=== Testing H2 Link #7: Locations ===")
        self.link_assertion(HomePage.h2_heading + "[7]//a", "locations")
        print("✓ Locations link passed\n")

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

        for x in range(5):
            try:
                self.click(HomePage.slide_next)
            except NoSuchElementException:
                self.wait(2)
                self.click(HomePage.slide_next)

        for x in range(3):
            try:
                self.click(HomePage.slide_prev)
            except NoSuchElementException:
                self.wait(2)
                self.click(HomePage.slide_prev)
