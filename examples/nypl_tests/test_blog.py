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

    def test_nypl_blog(self):
        print("test_nypl_blog()\n")

        # asserting the images on the page
        self.image_assertion()

        # assert Home button
        self.assert_element(BlogPage.home_button)

        # assert title
        self.assert_title(BlogPage.title)

        # assert Blog button text
        self.assert_element(BlogPage.blog_button)

        # 'NYPL Blog' text in h1
        self.assert_text("NYPL Blog", BlogPage.nypl_blog)

    def test_featured_posts(self):
        print("test_featured_posts()\n")
        # Featured Posts are dynamic, new posts added daily, so can't test every post
        # posts have dynamic id's and so need to update with better locators
        # post amount on the first page will be tested, which is 6

        # assert 'Featured Posts' h2 text
        self.assert_text("Featured Posts", BlogPage.featured_posts)

        # assert 'View all blog posts' element
        self.assert_element(BlogPage.view_all_blogs)
        self.click(BlogPage.view_all_blogs)
        self.wait_for_element(BlogPage.explore_by_h2)  # waiting until the clicked page loads
        # print(self.get_current_url())
        self.assert_true('/blog/all' in self.get_current_url())
        self.go_back()
        self.wait_for_element(BlogPage.featured_posts)  # wait for the page load. sync issue here without this wait.

        # find posts links elements
        number_of_posts_links_elements = len(self.find_elements(BlogPage.post_links))

        # post links amount assertion
        print(number_of_posts_links_elements)
        self.assert_true(0 <= number_of_posts_links_elements <= 6, "actual :" + str(number_of_posts_links_elements))

    def test_more_at_nypl_links(self):
        print("test_more_at_nypl_links()\n")
        # links clicked and titles asserted, only Find Your Next Book title is Dynamic, so passed on that

        # More at NYPL menu text
        self.assert_text("More at NYPL", BlogPage.more_at_nypl)

        # Get a Library Card item
        self.assert_link_text("Get a Library Card")
        self.click_link_text("Get a Library Card")
        self.assert_title("Get a Free Library Card Today! | The New York Public Library")
        self.go_back()
        self.wait_for_element(BlogPage.more_at_nypl)

        # Find Your Next Book, title and years for the link and page are dynamic "Winter 2022 picks...".
        # "-Winter/Fall/Summer/Spring- 2022 Picks for Adults | The New York Public Library"
        # TODO title is dynamic and needs to match the 'Season'
        # TODO test stops if title does not match, find a TRY / CATCH to keep running tests

        # assert 'Find Your Next' web element
        self.assert_element(BlogPage.find_your_next)

        # Search Library Locations
        self.assert_link_text("Search Library Locations")
        self.click_link_text("Search Library Locations")
        self.assert_title("Location Finder | The New York Public Library")
        self.go_back()
        self.wait_for_element(BlogPage.more_at_nypl)

        # Reserve a Computer
        self.assert_link_text("Reserve a Computer")
        self.click_link_text("Reserve a Computer")
        self.assert_title("Reserving a Computer | The New York Public Library")
        self.go_back()
        self.wait_for_element(BlogPage.more_at_nypl)

    def test_need_help_ask_nypl(self):
        print("test_need_help_ask_nypl()\n")
        # fin the case of dynamic xpaths, full xpaths used

        # Need Help? Ask NYPL menu text
        self.assert_text("Need Help? Ask NYPL", BlogPage.need_help)

        # Email us your question
        self.assert_link_text("Email us your question")
        self.click_link_text("Email us your question")
        # print(self.get_title())  # optional print
        # this title seems to be changing at times, might need to update this once in a while
        self.assert_title("AskNYPL - LibAnswers")
        self.go_back()
        self.wait_for_element(BlogPage.need_help)

        # Chat with a librarian
        self.assert_link_text('Chat with a librarian')
        self.click('/html/body/div[1]/div/div/main/div[2]/div[2]/nav[2]/ul/li[2]/a')
        # print(self.get_title())  # optional print
        # this title seems to be changing at times, might need to update this once in a while
        self.assert_title("AskNYPL - LibAnswers")
        self.go_back()
        self.wait_for_element(BlogPage.need_help)

        # Text (917) 983-4584
        self.assert_text("Text (917) 983-4584", BlogPage.text_917)

        # Call (917) ASK-NYPL
        self.assert_link_text("Call (917) ASK-NYPL")
        self.assert_text("Call (917) ASK-NYPL", BlogPage.call_917)

        # (917) 275-6975
        self.assert_link_text("Call (917) ASK-NYPL")
        self.assert_partial_link_text("917) 275-6975")
        self.assert_text("(917) 275-6975", BlogPage.string_917_275)

        # TTY 212-930-0020
        self.assert_text("TTY 212-930-0020", BlogPage.tty_212)

    def test_support_nypl(self):
        print("test_support_nypl()\n")

        # assert 'Support NYPL' text
        self.assert_text('Support NYPL', BlogPage.support_nypl)

        # assert 'Volunteer' link text and text
        self.assert_link_text("Volunteer")
        self.assert_text("Volunteer", BlogPage.volunteer)

        # assert 'Support Your Library' element and text
        # print(self.get_current_url())
        self.assert_element(BlogPage.support_nypl_link)
        self.assert_text("Support Your Library", BlogPage.support_your_library)

        # assert 'donation' word in the URL after clicking 'Support Your Library' link
        self.click_xpath(BlogPage.support_your_library)
        self.assert_true('donation' in self.get_current_url())

    def test_explore_by_channel(self):
        print("test_explore_by_channel()\n")

        # assert 'Explore By Channel' text
        self.assert_text("Explore By Channel", BlogPage.explore_by_channel)

        # assert 'View all channels' link text
        self.assert_text("View all channels", BlogPage.view_all_channels)

        # assert loaded page contains 'channels' in the URL, after clicking 'view all channels',
        self.click_xpath(BlogPage.view_all_channels)  # click on 'view all channels'
        # print(self.get_current_url())  # optional print for debugging
        self.assert_true("channels" in self.get_current_url())
        self.go_back()  # go back
        self.wait_for_element(BlogPage.explore_by_channel)  # wait for the chanel element

        # assertions for 2 Bottom Boxes.
        # These are dynamic boxes. e.g. > "Book Lists - Romance - Poetry..."
        # assert first box
        self.assert_link_text(BlogPage.first_box)
        self.click_xpath(BlogPage.first_box)
        # print(self.get_current_url())  # optional pint of the URL
        self.wait_for_element(BlogPage.explore_by_h2)  # waiting until the clicked page opens
        # print(self.get_current_url())  # optional print for debugging
        self.assert_true('blog/all?channel=' in self.get_current_url())
        self.go_back()
        self.wait_for_element(BlogPage.view_all_channels)

        # assert seconds box
        self.assert_link_text(BlogPage.second_box)
        self.click_xpath(BlogPage.second_box)
        self.wait_for_element(BlogPage.explore_by_h2)  # waiting until the clicked page opens
        self.assert_true('blog/all?channel=' in self.get_current_url())
        # self.go_back()
