from seleniumbase import BaseCase


class EducationKidsPage(BaseCase):
    home_button = '(//*[contains(text(), "Home")])[1]'
    education = '(//*[contains(text(), "Education")])[2]'
    title = "Kids | The New York Public Library"

    total_h2 = '(//*[@id="mainContent"]//h2)'

    all_links = '((//*[@id="page-container--content-primary"]//li)//a)'  # locator for 'page-container'

    # kids newsletter signup locators
    email_subscription = '(//*[contains(text(), "Connect with Us")])[1]'
    email_subs_input = '//*[@id="email-input"]'
    submit_email = '(//*[contains(text(), "Submit")])[1]'
    subs_confirmation = '(//*[contains(text(), "Connect with Us")])[1]//..//..//*[contains(text(), "Thank you!")]'

    def open_education_kids_page(self):
        # self.open("https://www.nypl.org/education/kids")

        prod = "https://www.nypl.org/education/kids"
        qa = "https://www.nypl.org/education/kids"

        if self.env == "qa":
            print("Running on QA Env")
            self.open(qa)

        else:
            print("Running on Production Env")
            self.open(prod)
