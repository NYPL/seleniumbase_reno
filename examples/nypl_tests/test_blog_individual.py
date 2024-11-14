import pytest

from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_blog_individual import BlogIndividualPage
import random


class BlogIndividualTest(NyplUtils):

    # https://www.nypl.org/blog/2022/09/22/reading-list-climate-week-nyc

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open main page
        self.open_blog_individual_page()

    def tearDown(self):
        print("\nRUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_blog_individual(self):
        print("test_blog_individual()\n")

        # assert title
        self.assert_title(BlogIndividualPage.home_title)

        # assert images on the page
        self.image_assertion()

        # assert all links on the page
        self.assert_links_valid(BlogIndividualPage.all_links)

        # assert breadcrumbs
        self.assert_element(BlogIndividualPage.home)
        self.assert_element(BlogIndividualPage.blog)

        # assert that page h3 link amount >= 1
        page_link_amount = len(self.find_elements(BlogIndividualPage.page_link_amount))
        # print(page_link_number)  # optional print
        self.assert_true(page_link_amount >= 1, "no h3 links on the page")

