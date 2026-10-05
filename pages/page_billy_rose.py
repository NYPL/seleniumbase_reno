from seleniumbase import BaseCase


class BillyRosePage(BaseCase):

    home = '(//*[contains(text(), "Home")])[1]'
    locations = '(//*[contains(text(), "Locations")])[2]'
    nypl_performing = '(//*[contains(text(), "New York Public Library for the")])[1]'

    all_links = '((//*[@id="page-container--content-primary"]//li)//a)'  # locator for 'basic-page'

    directions = '(//*[contains(text(), "Directions")])[1]'
    email = '(//*[contains(text(), "mail")])[2]'
    holiday_closings = '(//*[contains(text(), "Holiday Closings")])[1]'

    def open_billy_rose_page(self):

        qa = "https://qa-www.nypl.org/locations/lpa/billy-rose-theatre-division"
        prod = "https://www.nypl.org/locations/lpa/billy-rose-theatre-division"

        if self.env == "qa":
            print("Running on QA Env")
            self.open(qa)

        else:
            print("Running on Production Env")
            self.open(prod)
