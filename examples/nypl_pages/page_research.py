from seleniumbase import BaseCase


class ResearchPage(BaseCase):

    home = '//*[@id="__next"]/div/div[2]/nav/ol/li[1]/a/span'

    def open_research_page(self):
        # self.open("https://www.nypl.org/research")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://www.nypl.org/research")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/research")
