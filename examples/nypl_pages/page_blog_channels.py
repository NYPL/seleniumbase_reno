from seleniumbase import BaseCase


class BlogChannelsPage(BaseCase):
    home = '(//*[contains(text(), "Home")])[1]'
    blog = '(//*[contains(text(), "Blog")])[2]'

    home_title = 'Blogs: Explore By Channel | The New York Public Library'

    explore_by_channel_links = '(//*[@id="page-container--content-primary"]//li//a)'

    def open_blog_channels_page(self):
        prod = "https://www.nypl.org/blog/channels"
        qa = "https://qa-www.nypl.org/blog/channels"

        if self.env == "qa":
            print("Running on QA Env")
            self.open(qa)

        else:
            print("Running on Production Env")
            self.open(prod)
