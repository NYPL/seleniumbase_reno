from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_blog_channels import BlogChannelsPage
import re, random


class BlogChannelsTest(NyplUtils):

    # https://www.nypl.org/blog/channels

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open main page
        self.open_blog_channels_page()

    def tearDown(self):
        print("\nRUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_blog_channels(self):
        print("test_blog_channels()\n")

        # assert title
        self.assert_title(BlogChannelsPage.home_title)

        # assert images on the page
        self.image_assertion()

        # assert breadcrumbs
        self.assert_element(BlogChannelsPage.home)
        self.assert_element(BlogChannelsPage.blog)

        # assert that channel link amount is >= 1
        links = len(self.find_elements('//*[@id="page-container--content-primary"]/div/ul/li//a'))
        # print(links)  # optional print
        self.assert_true(links >= 1, "no visible links on the page")
