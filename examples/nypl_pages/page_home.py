from seleniumbase import BaseCase


class HomePage(BaseCase):
    hero = '(//*[@id[contains(., "hero")]])//h1'
    home_title = 'The New York Public Library'

    h2_heading = '(//*[@id="content-primary"]//h2)'
    see_more = '(//a[contains(text(), "See More")])'

    slide_next = '//*[@id="slideshow-next-button"]'
    slide_prev = '//*[@id="slideshow-prev-button"]'
    new_noteworthy_slide = '(//*[@id="content-primary"]//h2)[5]//..//..//..//li'

    def open_home_page(self):
        # self.open("https://www.nypl.org/")

        base_url = "https://www.nypl.org/"
        qa_base_url = "https://qa-www.nypl.org/"

        url = f"{base_url}"
        qa_url = f"{qa_base_url}"

        # Open the appropriate URL based on the environment
        if self.env == "qa":
            print(f"Running on QA Env: Opening : {qa_url}")
            self.open(qa_url)
        else:
            print(f"Running on Production Env: Opening : {url}")
            self.open(url)
