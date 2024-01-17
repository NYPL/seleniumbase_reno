from seleniumbase import BaseCase


class BlogIndividualPage(BaseCase):
    home = '(//*[contains(text(), "Home")])[1]'
    blog = '(//*[contains(text(), "Blog")])[1]'

    home_title = 'A Reading List for Climate Week NYC | The New York Public Library'

    page_link_amount = '//*[@id="main-content"]//li//h3//a'

    def open_blog_individual_page(self):
        prod = "https://www.nypl.org/blog/2022/09/22/reading-list-climate-week-nyc"
        qa = "https://qa-www.nypl.org/blog/2022/09/22/reading-list-climate-week-nyc"

        if self.env == "qa":
            print("Running on QA Env")
            self.open(qa)

        else:
            print("Running on Production Env")
            self.open(prod)
