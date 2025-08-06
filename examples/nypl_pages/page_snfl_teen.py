from seleniumbase import BaseCase


class SnflTeenPage(BaseCase):
    # breadcrumbs locators
    home = '(//*[contains(text(), "Home")])[1]'
    locations = '(//*[contains(text(), "Locations")])[2]'
    snfl = '(//*[contains(text(), "Stavros Niarchos")])[1]'

    all_links = '((//*[@id="page-container--content-primary"]//li)//a)'  # all links locator for 'Emulsify'

    # left side tab locators
    directions = '(//*[contains(text(), "Directions")])[1]'
    holiday_closings = '(//*[contains(text(), "Holiday Closings")])[1]'
    give = '(//*[contains(text(), "Give Now")])[1]'
    social_media = '(//*[contains(text(), "Find Us On")])[1]'
    email = '(//*[contains(text(), "snflteens@nypl.org")])[1]'

    def open_snfl_teen_page(self):
        # self.open("https://www.nypl.org/locations/snfl/teen")

        prod = "https://www.nypl.org/locations/snfl/teen"
        qa = "https://qa-www.nypl.org/locations/snfl/teen"

        if self.env == "qa":
            print("Running on QA Env")
            self.open(qa)

        else:
            print("Running on Production Env")
            self.open(prod)
