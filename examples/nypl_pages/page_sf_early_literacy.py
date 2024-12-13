from seleniumbase import BaseCase


class EarlyLiteracyPage(BaseCase):

    home_button = '(//*[contains(text(), "Home")])[1]'
    education = '(//*[contains(text(), "Education")])[2]'
    title = "Early Literacy | The New York Public Library"

    all_links = '((//*[@id="page-container--content-primary"]//li)//a)'  # locator for 'page-container'

    # kids newsletter signup locators
    email_subscription = '(//*[contains(text(), "Connect with Us")])[1]'
    email_subs_input = '//*[@id="email-input"]'
    submit_email = '(//*[contains(text(), "Submit")])[1]'
    subs_confirmation = '(//*[contains(text(), "Connect with Us")])[1]//..//..//*[contains(text(), "Thank you!")]'

    def open_early_literacy_page(self):
        # self.open("https://www.nypl.org/education/early-literacy")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/education/early-literacy")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/education/early-literacy")
