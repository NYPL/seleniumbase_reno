from seleniumbase import BaseCase


class SnflPage(BaseCase):
    home = '(//*[contains(text(), "Home")])[1]'

    visit = '//*[@id="audience-navigation--"]//*[contains(text(), "Visit")]'
    explore = '//*[@id="audience-navigation--"]//*[contains(text(), "Explore")]'
    read = '//*[@id="audience-navigation--"]//*[contains(text(), "Read")]'

    all_links = '((//*[@id="block-nypl-emulsify-content"]//li)//a)'  # all links locator for 'Emulsify'

    # left side tab locators
    directions = '(//*[contains(text(), "Directions")])[1]'
    holiday_closings = '(//*[contains(text(), "Holiday Closings")])[1]'
    give = '(//*[contains(text(), "Give Now")])[1]'
    social_media = '(//*[contains(text(), "Find Us On")])[1]'

    # "Read" tab locators
    top_checkouts = '(//*[contains(text(), "Top Checkouts")])[1]'
    shelf_help = '(//*[contains(text(), "Shelf Help")])[1]'

    def open_snfl_page(self):
        # self.open("https://www.nypl.org/locations/snfl")

        prod = "https://www.nypl.org/locations/snfl"
        qa = "https://qa-www.nypl.org/locations/snfl"

        if self.env == "qa":
            print("Running on QA Env")
            self.open(qa)

        else:
            print("Running on Production Env")
            self.open(prod)
