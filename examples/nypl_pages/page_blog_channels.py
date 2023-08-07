from seleniumbase import BaseCase


class BlogChannelsPage(BaseCase):
    home = '(//*[contains(text(), "Home")])[1]'
    blog = '(//*[contains(text(), "Blog")])[2]'

    home_title = 'Blogs: Explore By Channel | The New York Public Library'

    def open_blog_channels_page(self):
        prod_url = "https://www.nypl.org/blog/channels"
        qa_url = "https://qa-www.nypl.org/blog/channels"

        if self.env == "qa":
            print("Running on QA Env")
            self.open(qa_url)

        else:
            print("Running on Production Env")
            self.open(prod_url)
