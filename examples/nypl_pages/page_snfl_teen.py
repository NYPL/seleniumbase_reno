from seleniumbase import BaseCase


class SnflTeenPage(BaseCase):
    home = '//*[@id="block-nypl-emulsify-breadcrumbs"]/nav/ul/li[1]/a'
    locations = '//*[@id="block-nypl-emulsify-breadcrumbs"]/nav/ul/li[2]/a'
    snfl = '//*[@id="block-nypl-emulsify-breadcrumbs"]/nav/ul/li[3]/a'

    directions = '//*[@id="block-entityviewcontent"]/div/div/div/a'
    email = '//*[@id="block-entityviewcontent"]/div/div/div/div[3]/a'
    holiday_closings = '//*[@id="block-entityviewcontent"]/div/div/div/div[6]/a'

    events = '//*[@id="event-section-center"]/following-sibling::*[1]'

    # teen center resources
    teen_center_1 = "//*[contains(text(), 'Teen Center Resources')]/../../following-sibling::*//child::li[1]"
    teen_center_2 = "//*[contains(text(), 'Teen Center Resources')]/../../following-sibling::*//child::li[2]"
    teen_center_3 = "//*[contains(text(), 'Teen Center Resources')]/../../following-sibling::*//child::li[3]"
    teen_center_4 = "//*[contains(text(), 'Teen Center Resources')]/../../following-sibling::*//child::li[4]"
    teen_center_5 = "//*[contains(text(), 'Teen Center Resources')]/../../following-sibling::*//child::li[5]"
    teen_center_6 = "//*[contains(text(), 'Teen Center Resources')]/../../following-sibling::*//child::li[6]"

    def open_snfl_teen_page(self):
        # self.open("https://www.nypl.org/locations/snfl/teen")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/locations/snfl/teen")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/locations/snfl/teen")
