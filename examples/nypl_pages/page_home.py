from seleniumbase import BaseCase


class HomePage(BaseCase):
    hero = '//*[@id="hero-293c191e-5888-483d-aba3-93200f4e86a9"]'
    home_title = 'The New York Public Library'
    spotlight = '//*[@id="component-wrapper-heading-21204740-28e6-4580-acd1-6f3d673bfa11"]'

    slide_next = '//*[@id="slideshow-next-button"]'
    slide_prev = '//*[@id="slideshow-prev-button"]'
    new_noteworthy_slide = '//*[@id="content-primary"]/div[5]//li'

    def open_home_page(self):
        # self.open("https://www.nypl.org/")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/")
