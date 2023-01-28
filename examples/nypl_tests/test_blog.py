import time

from examples.nypl_pages.blog_page import BlogPage
from selenium.common.exceptions import NoSuchElementException


class BlogTests(BlogPage):

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
        # https://www.nypl.org/blog
        print("test_nypl_blog()\n")

        # Home button
        self.click_xpath(self.home_button)
        self.assert_title(self.home_title)
        self.go_back()

        # Blog button
        self.assert_text('Blog', self.blog_button)

        # NYPL Blog
        self.assert_text("NYPL Blog", self.nypl_blog)

        # NYPL Blog -paragraph text assert ("Not sure..." text)
        self.assert_text("sure what", self.nypl_blog_paragraph)

    def test_featured_posts(self):
        print("test_featured_posts()\n")
        # Featured Posts are dynamic, new posts added daily, so can't test every post
        # posts have dynamic id's and so can't use xpath and hence the new additions full xpath cannot be used either
        # post amount on the first page will be tested, which is 6

        # assert 'Featured Posts' h2 text
        self.assert_text("Featured Posts", self.featured_posts)

        # View all blog posts
        self.assert_element(self.view_all_blogs)
        self.click(self.view_all_blogs)
        self.wait_for_element(self.explore_by_h2)  # waiting until the clicked page opens
        # print(self.get_current_url())
        self.assert_true('/blog/all' in self.get_current_url())
        self.go_back()

        # Take a look at the latest posts from the NYPL Blog:
        take_a_look_text = "Take a look at the latest posts from the NYPL Blog:"
        self.assert_text(take_a_look_text, self.take_a_look_text)

    def test_post_links(self):
        print("test_post_links()\n")
        # TODO need try/catch for posts links amount assertion
        # find posts links elements
        post_links_elements = self.find_elements(self.post_links)
        number_of_posts_links_elements = len(post_links_elements)

        # post links amount assertion
        self.assert_true(0 <= number_of_posts_links_elements <= 6, "Number of posts do not match expected 1-6")

        for x in post_links_elements:
            pass

        try:
            self.assert_true(1 <= number_of_posts_links_elements <= 6, "Number of posts do not match expected 1-6")
        except NoSuchElementException:
            print("Exception here")

    def test_more_at_nypl_links(self):
        print("test_more_at_nypl_links()\n")
        # links clicked and titles asserted, only Find Your Next Book title is Dynamic, so passed on that

        # More at NYPL menu text
        self.assert_text("More at NYPL", self.more_at_nypl)

        # Get a Library Card
        self.assert_link_text("Get a Library Card")
        self.click_link_text("Get a Library Card")
        self.assert_title("Get a Free Library Card Today! | The New York Public Library")
        self.go_back()

        # Find Your Next Book, title and years for the link and page are dynamic "Winter 2022 picks...".
        # "-Winter/Fall/Summer/Spring- 2022 Picks for Adults | The New York Public Library"
        # TODO title is dynamic and needs to match the 'Season'
        # TODO test stops if title does not match, find a TRY / CATCH to keep running tests

        # assert 'Find Your Next' web element
        self.assert_element(self.find_your_next)

        # Search Library Locations
        self.assert_link_text("Search Library Locations")
        self.click_link_text("Search Library Locations")
        self.assert_title("Location Finder | The New York Public Library")
        self.go_back()

        # Reserve a Computer
        self.assert_link_text("Reserve a Computer")
        self.click_link_text("Reserve a Computer")
        self.assert_title("Reserving a Computer | The New York Public Library")
        self.go_back()
        print("reached the end of the test suite")

    def test_need_help_ask_nypl(self):
        print("test_need_help_ask_nypl()\n")
        # fin the case of dynamic xpaths, full xpaths used

        # Need Help? Ask NYPL menu text
        self.assert_text("Need Help? Ask NYPL", self.need_help)

        # Email us your question
        self.assert_link_text("Email us your question")
        self.click_link_text("Email us your question")
        # print(self.get_title())  # optional print
        # this title seems to be changing at times, might need to update this once in a while
        self.assert_title("AskNYPL - LibAnswers")
        self.go_back()

        # Chat with a librarian
        self.assert_link_text('Chat with a librarian')
        self.click('/html/body/div[1]/div/div/main/div[2]/div[2]/nav[2]/ul/li[2]/a')
        # print(self.get_title())  # optional print
        # this title seems to be changing at times, might need to update this once in a while
        self.assert_title("AskNYPL - LibAnswers")
        self.go_back()

        # Text (917) 983-4584
        self.assert_text("Text (917) 983-4584", self.text_917)

        # Call (917) ASK-NYPL
        self.assert_link_text("Call (917) ASK-NYPL")
        self.assert_text("Call (917) ASK-NYPL", self.call_917)

        # (917) 275-6975
        self.assert_link_text("Call (917) ASK-NYPL")
        self.assert_partial_link_text("917) 275-6975")
        self.assert_text("(917) 275-6975", self.string_917_275)

        # TTY 212-930-0020
        self.assert_text("TTY 212-930-0020", self.tty_212)

    def test_support_nypl(self):
        print("test_support_nypl()\n")
        # Support NYPL
        self.assert_text('Support NYPL', self.support_nypl)
        self.wait(1)

        # Volunteer
        self.assert_link_text("Volunteer")
        self.assert_text("Volunteer", self.volunteer)
        self.wait(1)

        # Support Your Library
        # print(self.get_current_url())
        self.assert_element(self.support_nypl_link)
        self.assert_text("Support Your Library", self.support_your_library)
        self.wait(1)

        self.click_xpath(self.support_your_library)
        self.assert_true('donation' in self.get_current_url())
        self.go_back()

    def test_post_images(self):
        print("test_post_images()\n")
        # checking the blog post image links present
        for num in range(1, 7):
            image = '/html/body/div[1]/div/div/main/div[2]/div[1]/div[1]/ul/li[' + str(num) + ']/div/div[1]/div/span/img'
            self.assert_elements_present(image)
            print("Image " + str(num) + " is present")
            # optional, printing the image links
            # self.wait(1)
            print(self.get_image_url(image))

        # hardcoded version below
        '''
        self.assert_elements_present('/html/body/div[1]/div/div/main/div[2]/div[1]/div[1]/ul/li[1]/div/div[1]/div/img')
        self.assert_elements_present('/html/body/div[1]/div/div/main/div[2]/div[1]/div[1]/ul/li[2]/div/div[1]/div/img')
        self.assert_elements_present('/html/body/div[1]/div/div/main/div[2]/div[1]/div[1]/ul/li[3]/div/div[1]/div/img')
        self.assert_elements_present('/html/body/div[1]/div/div/main/div[2]/div[1]/div[1]/ul/li[4]/div/div[1]/div/img')
        self.assert_elements_present('/html/body/div[1]/div/div/main/div[2]/div[1]/div[1]/ul/li[5]/div/div[1]/div/img')
        self.assert_elements_present('/html/body/div[1]/div/div/main/div[2]/div[1]/div[1]/ul/li[6]/div/div[1]/div/img')

        print(self.get_image_url('/html/body/div[1]/div/div/main/div[2]/div[1]/div[1]/ul/li[1]/div/div[1]/div/img'))
        print(self.get_image_url('/html/body/div[1]/div/div/main/div[2]/div[1]/div[1]/ul/li[2]/div/div[1]/div/img'))
        print(self.get_image_url('/html/body/div[1]/div/div/main/div[2]/div[1]/div[1]/ul/li[3]/div/div[1]/div/img'))
        print(self.get_image_url('/html/body/div[1]/div/div/main/div[2]/div[1]/div[1]/ul/li[4]/div/div[1]/div/img'))
        print(self.get_image_url('/html/body/div[1]/div/div/main/div[2]/div[1]/div[1]/ul/li[5]/div/div[1]/div/img'))
        print(self.get_image_url('/html/body/div[1]/div/div/main/div[2]/div[1]/div[1]/ul/li[6]/div/div[1]/div/img'))
        
        '''

    def test_explore_by_channel(self):
        print("test_explore_by_channel()\n")
        # Explore By Channel header
        self.assert_text("Explore By Channel", self.explore_by_channel)

        # view all channels link
        self.assert_text("View all channels", self.view_all_channels)
        # click on view all channels
        self.click_xpath(self.view_all_channels)
        # check if we are in the view all channels page
        time.sleep(1)
        # print(self.get_current_url())  # optional print of the URL
        print(self.get_current_url())
        self.assert_true("/blog/channels" in self.get_current_url())
        # go back
        self.go_back()
        # 'The NYPL' paragraph element and text assertion
        self.assert_element(self.the_nypl_blog_text)
        the_nypl_text = "The NYPL blog channels can help you discover more posts around the topics you care about." \
                        " From Black Culture to Women's History and Romance to Horror–there is something for everyone."
        self.assert_text(the_nypl_text, self.the_nypl_blog_text)

        # POETRY & BOOK LISTS image assertions
        self.assert_elements_present(self.first_img, self.second_img)

        # Poetry and Book Lists link text and page assertion
        self.assert_link_text(self.first_box)
        self.click_xpath(self.first_box)
        # print(self.get_current_url())  # optional pint of the URL
        self.wait_for_element(self.explore_by_h2)  # waiting until the clicked page opens
        print(self.get_current_url())
        self.assert_true('blog/all?channel=' in self.get_current_url())
        self.go_back()
        self.assert_link_text(self.second_box)
        self.click_xpath(self.second_box)
        self.wait_for_element(self.explore_by_h2)  # waiting until the clicked page opens
        self.assert_true('blog/all?channel=' in self.get_current_url())
        self.go_back()
        # Poetry & Book Lists paragraph texts assertion
        first_box_text = '/html/body/div[1]/div/div[2]/main/div[2]/div[1]/div[2]/ul/li[1]/div/div[2]/div/div'
        second_box_text = '/html/body/div[1]/div/div[2]/main/div[2]/div[1]/div[2]/ul/li[2]/div/div[2]/div/div'
        self.assert_element(first_box_text)
        self.assert_element(second_box_text)
