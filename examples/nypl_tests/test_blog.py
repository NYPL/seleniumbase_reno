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

        # assert all links on the page
        self.assert_links_valid(BlogPage.all_links)

        # assert Home button
        self.assert_element(BlogPage.home)

        # assert title
        self.assert_title(BlogPage.title)

        # assert Blog button text
        self.assert_element(BlogPage.blog_button)

        # 'NYPL Blog' text in h1
        self.assert_text("NYPL Blog", BlogPage.nypl_blog)

        # assert 'View all channels' element
        self.link_assertion(BlogPage.view_all_channels, "channels")  # assert 'View all channels' link goes to
        # correct page

    def test_featured_posts(self):
        print("test_featured_posts()\n")
        # Featured Posts are dynamic, new posts added daily, so can't test every post

        try:
            # Assert 'Featured Posts' element
            self.assert_element(BlogPage.featured_posts)

            # Assert the 'View all blog posts' link
            self.link_assertion(BlogPage.view_all_blogs, "blog/all")

            # Find post links elements
            featured_posts_elements = self.find_elements(BlogPage.featured_posts_length)
            featured_posts_length = len(featured_posts_elements)

            # Post links amount assertion
            print("Featured Posts amount: " + str(featured_posts_length))
            assert featured_posts_length >= 1, "No Links present. At least 1 Link expected"

        except AssertionError as e:
            print(f"Assertion failed: {e}. Retrying after waiting...")

            # Additional wait time to handle sync issues
            self.wait(2)

            # Retry finding post elements and asserting again
            featured_posts_elements = self.find_elements(BlogPage.featured_posts_length)
            featured_posts_length = len(featured_posts_elements)

            print("Retrying... Featured Posts amount: " + str(featured_posts_length))
            assert featured_posts_length >= 1, "No Links present. At least 1 Link expected"

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







