from seleniumbase import BaseCase


class SchwarzmanPage(BaseCase):

    home = '//*[@id="block-nypl-emulsify-breadcrumbs"]/nav/ul/li[1]/a'
    locations = '//*[@id="block-nypl-emulsify-breadcrumbs"]/nav/ul/li[2]/a'
    hero = '//*[@id="block-content-hero-header"]/div/div[2]/h1/span'

    visit = '//*[@id="audience-navigation--"]/li[1]/a'
    research = '//*[@id="audience-navigation--"]/li[2]/a'
    directions = '//*[@id="block-entityviewcontent"]/div/div/div/a'
    holiday_closings = '//*[@id="block-entityviewcontent"]/div/div/div/div[5]/a'
    learn_more_link = '//*[@id="block-nypl-emulsify-content"]/div/div/div[1]/div/p[2]/a'

    def open_schwarzman_page(self):
        # self.open("https://www.nypl.org/locations/schwarzman")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/locations/schwarzman")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/locations/schwarzman")
