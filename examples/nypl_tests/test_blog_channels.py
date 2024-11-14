from examples.nypl_pages.page_blog_channels import BlogChannelsPage
from examples.nypl_utility.utility import NyplUtils


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

        # assert all links on the page
        self.assert_links_valid(BlogChannelsPage.all_links)

        # assert breadcrumbs
        self.assert_element(BlogChannelsPage.home)
        self.assert_element(BlogChannelsPage.blog)

        # assert that "Explore By Channel" link amount is >= 1
        links = len(self.find_elements(BlogChannelsPage.explore_by_channel_links))
        # print(links)  # optional print
        self.assert_true(links >= 1, "no visible 'Explore by Channel' links on the page")


