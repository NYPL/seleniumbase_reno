from seleniumbase import BaseCase


class SchwarzmanPage(BaseCase):
    home = '(//*[contains(text(), "Home")])[1]'
    hero = '(//*[@id[contains(., "hero")]])//h1'

    visit = '(//*[contains(text(), "Research")])[2]//..//..//*[contains(text(), "Visit")][1]'
    research = '(//*[contains(text(), "Visit")][1]//..//..//*[contains(text(), "Research")])[1]'

    all_links = '((//*[@id="page-container--content-primary"]//li)//a)'  # all links locator for 'Emulsify'

    sidebar = '//*[@id="block-entityviewcontent"]'
    holiday_closings = '(//*[contains(text(), "Holiday Closings")])[1]'
    address = '//*[@id="location-info--fifth-avenue-and-42nd-street<br>new-york-ny-10018"]'

    def open_schwarzman_page(self):
        # self.open("https://www.nypl.org/locations/schwarzman")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/locations/schwarzman")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/locations/schwarzman")
