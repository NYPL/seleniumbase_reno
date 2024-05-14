import pytest

from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_blog import BlogPage

import time
from selenium.common.exceptions import NoSuchElementException


class BlogTests(NyplUtils):

    # https://www.nypl.org/blog

    def setUp(self):
        super().setUp()
        print("=================================")
        print("\nRUNNING BEFORE EACH TEST")

        # open blog page
        self.open_blog_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    @pytest.mark.smoke
    def test_blog_main(self):
        print("test_nypl_blog()\n")

        # asserting the images on the page
        self.image_assertion()

        # assert Home button
        self.assert_element(BlogPage.home)

        # assert title
        self.assert_title(BlogPage.title)

        # assert Blog button text
        self.assert_element(BlogPage.blog_button)

        # 'NYPL Blog' text in h1
        self.assert_text("NYPL Blog", BlogPage.nypl_blog)

    def test_featured_posts(self):
        print("test_featured_posts()\n")
        # Featured Posts are dynamic, new posts added daily, so can't test every post

        # assert 'View all blog posts' element
        self.assert_element(BlogPage.featured_posts)  # assert 'Featured Posts' element
        self.assert_element(BlogPage.view_all_blogs)  # assert the 'View all blog posts' element
        self.link_assertion(BlogPage.view_all_blogs, "blog")  # assert the 'View all blog posts' link

        # find posts links elements
        featured_posts_length = len(self.find_elements(BlogPage.featured_posts_length))

        # assert all 'Featured Posts' links with utility function
        for x in range(1, featured_posts_length + 1):
            self.assert_page_loads_successfully(BlogPage.featured_posts_length + f'[{x}]//a')

        # post links amount assertion
        print(featured_posts_length)
        expected_featured_post_amount = 6
        self.assert_true(0 <= featured_posts_length <= expected_featured_post_amount,
                         "expected: " + str(expected_featured_post_amount) + ", actual: " + str(featured_posts_length))

    def test_right_side_tab(self):
        print("test_more_at_nypl_links()\n")
        # links clicked and titles asserted, only Find Your Next Book title is Dynamic, so passed on that

        # More at NYPL assertions
        self.assert_element(BlogPage.get_a_library_card)  # assert 'Get a Library Card' element
        self.assert_element(BlogPage.find_your_next_book)  # assert 'Find your next book' element
        self.assert_element(BlogPage.search_library_locations)  # assert 'Search Library Locations' element
        self.assert_element(BlogPage.reserve_a_computer)  # assert 'Reserve a Computer' element

        # 'Get a Library Card' element link assertion
        self.link_assertion(BlogPage.get_a_library_card, "card")
        # Find Your Next Book element link assertion
        self.link_assertion(BlogPage.find_your_next_book, "recommendations")
        # Search Library Locations link assertion
        self.link_assertion(BlogPage.search_library_locations, "locations")
        # Reserve a Computer link assertion
        self.link_assertion(BlogPage.reserve_a_computer, "computer")

        # need help? ASK NYPL assertions
        self.assert_element(BlogPage.need_help_1)  # assert 'Email us your question' element
        self.link_assertion(BlogPage.need_help_1, "libanswers")  # assert 'Email us your question' link
        self.assert_element(BlogPage.need_help_3)  # assert 'Text (917) 983-4584' element
        self.assert_element(BlogPage.need_help_4)  # assert 'Call (917) ASK-NYPL' element
        self.assert_element(BlogPage.need_help_5)  # assert '(917) 275-6975' element
        self.assert_element(BlogPage.need_help_6)  # assert 'TTY 212-930-0020' element

        # Support NYPL assertion
        self.assert_element(BlogPage.volunteer)  # assert 'Volunteer' element
        self.assert_element(BlogPage.support_your_library)  # assert "Support Your Library" element
        self.link_assertion(BlogPage.support_your_library, "donation")  # assert the URL on "Support your Library"

    def test_explore_by_channel(self):
        print("test_explore_by_channel()\n")

        # assert 'Explore By Channel' text
        self.assert_text("Explore By Channel", BlogPage.explore_by_channel)

        # assert 'View all channels' element
        #self.wait(2)
        self.link_assertion(BlogPage.view_all_channels, "channels")  # assert 'View all channels' link goes to
        # correct page

        # assertions for the Bottom Boxes underneath "Explore By Channel". These boxes are dynamic, the content amount
        # and the content itself can change. e.g. > "Book Lists - Romance - Poetry..."

        # get the length/amount of the "Explore By Channel" links/boxes
        box_amount = len(self.find_elements(BlogPage.explore_by_channel_box_amount))

        for x in range(1, box_amount + 1):
            self.link_assertion(f"{BlogPage.explore_by_channel_box_amount}[{x}]", 'blog/all?channel=')


