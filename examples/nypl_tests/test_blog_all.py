import pytest

from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_blog_all import BlogAllPage
import random


class BlogAllTests(NyplUtils):

    # https://www.nypl.org/blog/all
    def setUp(self):
        super().setUp()
        print("=================================")
        print("\nRUNNING BEFORE EACH TEST")

        # open blog/all page
        self.open_blog_page_all()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_blog_all_main(self):
        print("test_page_elements()\n")

        # asserting the images on the page
        self.image_assertion()

        # assert all links on the page
        self.assert_links_valid(BlogAllPage.all_links)

        # assert Explore By:
        self.assert_element(BlogAllPage.explore_by)

        # assert filters
        self.assert_element(BlogAllPage.channels)
        self.assert_element(BlogAllPage.subjects)
        self.assert_element(BlogAllPage.libraries)
        self.assert_element(BlogAllPage.divisions)
        self.assert_element(BlogAllPage.audience)
