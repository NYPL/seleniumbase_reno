from seleniumbase import BaseCase


class SnflTeenPage(BaseCase):
    home = '//*[@id="block-nypl-emulsify-breadcrumbs"]/nav/ul/li[1]/a'
    locations = '//*[@id="block-nypl-emulsify-breadcrumbs"]/nav/ul/li[2]/a'
    snfl = '//*[@id="block-nypl-emulsify-breadcrumbs"]/nav/ul/li[3]/a'

    directions = '//*[@id="block-entityviewcontent"]/div/div/div/a'
    email = '//*[@id="block-entityviewcontent"]/div/div/div/div[3]/a'
    holiday_closings = '//*[@id="block-entityviewcontent"]/div/div/div/div[6]/a'

    events = '//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/div/div/div/div/a'

    # teen center resources
    teen_center_1 = '//*[@id="block-nypl-emulsify-content"]/div/div/div[3]/ul/li[1]/div[1]/h3/a'
    teen_center_2 = '//*[@id="block-nypl-emulsify-content"]/div/div/div[3]/ul/li[2]/div[1]/h3/a'
    teen_center_3 = '//*[@id="block-nypl-emulsify-content"]/div/div/div[3]/ul/li[3]/div[1]/h3/a'
    teen_center_4 = '//*[@id="block-nypl-emulsify-content"]/div/div/div[3]/ul/li[4]/div[1]/h3/a'
    teen_center_5 = '//*[@id="block-nypl-emulsify-content"]/div/div/div[3]/ul/li[5]/div[1]/h3/a'
    teen_center_6 = '//*[@id="block-nypl-emulsify-content"]/div/div/div[3]/ul/li[6]/div[1]/h3/a'


    def open_snfl_teen_page(self):
        # self.open("https://www.nypl.org/locations/snfl/teen")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/locations/snfl/teen")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/locations/snfl/teen")
