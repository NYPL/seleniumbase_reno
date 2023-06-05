from seleniumbase import BaseCase


class BillyRosePage(BaseCase):

    home = '//*[@id="block-nypl-emulsify-breadcrumbs"]/nav/ul/li[1]/a'
    locations = '//*[@id="block-nypl-emulsify-breadcrumbs"]/nav/ul/li[2]/a'
    nypl_performing = '//*[@id="block-nypl-emulsify-breadcrumbs"]/nav/ul/li[3]/a'

    directions = '//*[@id="block-entityviewcontent"]/div/div/div/a'
    email = '//*[@id="block-entityviewcontent"]/div/div/div/div[3]/a'
    holiday_closings = '//*[@id="block-entityviewcontent"]/div/div/div/div[6]/a'

    def open_billy_rose_page(self):
        # self.open("https://www.nypl.org/locations/lpa/billy-rose-theatre-division")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/locations/lpa/billy-rose-theatre-division")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/locations/lpa/billy-rose-theatre-division")
