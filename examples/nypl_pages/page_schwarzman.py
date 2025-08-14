from seleniumbase import BaseCase


class SchwarzmanPage(BaseCase):
    home = '(//*[contains(text(), "Home")])[1]'
    hero = '(//*[@id[contains(., "hero")]])//h1'

    visit = '//*[@href="/locations/schwarzman"]'
    research = '//*[@href="/locations/schwarzman/research"]'

    all_links = '((//*[@id="page-container--content-primary"]//li)//a)'  # all links locator for 'Emulsify'

    holiday_closings = '(//*[contains(text(), "Holiday Closings")])[1]'
    address = '//*[@id="page-container--content-secondary"]'

    def open_schwarzman_page(self):
        # self.open("https://www.nypl.org/locations/schwarzman")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/locations/schwarzman")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/locations/schwarzman")
