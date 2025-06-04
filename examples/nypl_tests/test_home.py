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
    def test_home_page(self):
        print("test_home_page()\n")

        # check images on the page
        self.image_assertion()

        # assert title
        self.assert_title(HomePage.home_title)
        # assert hero h1
        self.assert_element(HomePage.hero)

        # assert all links on the page
        # self.assert_links_valid(HomePage.all_links)
        # TODO skipping above assertion until the double html issue resolved on the homepage

        # assert all the h2  and 'See More' buttons ("Spotlight", "What's on", "Discover", "Staff Picks",
        # "New & Noteworthy", "From Our Blog", "Updates") in a loop
        h2_amount = len(self.find_elements(HomePage.h2_heading))  # getting the length
        for x in range(1, h2_amount + 1):
            # asserting h2 elements
            self.assert_element(HomePage.h2_heading + "[" + str(x) + "]")

        # assert 'See More' buttons. 'in the collection' excluded, one fewer than h2 elements
        for x in range(1, h2_amount):  # Looping until h2_amount - 1
            self.assert_element(HomePage.see_more + "[" + str(x) + "]")

        # asserting h2 links by clicking and comparing the URL on the next page
        self.link_assertion(HomePage.h2_heading + "[1]", "spotlight")
        self.link_assertion(HomePage.h2_heading + "[2]", "events")
        self.link_assertion(HomePage.h2_heading + "[3]", "remote")
        self.link_assertion(HomePage.h2_heading + "[4]", "staff")
        self.link_assertion(HomePage.h2_heading + "[5]//a", "new")
        self.link_assertion(HomePage.h2_heading + "[6]", "blog")
        self.link_assertion(HomePage.h2_heading + "[7]", "locations")

    @pytest.mark.smoke
    def test_slider(self):
        # new & noteworthy/in the collection slider
        print("test_slider()\n")

        # getting the length of the slide and asserting it is more than 0
        slide_length = len(self.find_elements(HomePage.new_noteworthy_slide))
        print("slide amount: " + str(slide_length))
        try:
            self.assert_true(slide_length >= 1)
        except AssertionError:
            print("inside try/except block for slide length assertion")
            self.wait(2)
            self.assert_true(slide_length >= 1)

        # Asserting that we can click the "next" button
        for x in range(5):
            try:
                self.click(HomePage.slide_next)
            except NoSuchElementException:
                print("inside try/except block for 'Next button' assertion")
                self.wait(2)
                self.click(HomePage.slide_next)

        # Asserting that we can click the "previous" button
        for x in range(3):
            try:
                self.click(HomePage.slide_prev)
            except NoSuchElementException:
                print("inside try/except block for 'Previous button' assertion")
                self.wait(2)
                self.click(HomePage.slide_prev)
