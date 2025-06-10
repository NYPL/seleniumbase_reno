from seleniumbase import BaseCase


class EducationPage(BaseCase):

    # breadcrumbs
    home_button = '(//*[contains(text(), "Home")])[1]'

    title = "Education | The New York Public Library"  # title

    all_links = '((//*[@id="page-container--content-primary"]//li)//a)'  # locator for 'page-container'

    # newsletter signup locators
    email_subscription = '(//*[contains(text(), "Sign Up for Our Newsletter")])[1]'
    email_subs_input = '//*[@id="email-input"]'
    submit_email = '(//*[contains(text(), "Submit")])[1]'
    subs_confirmation = '(//*[contains(text(), "Sign Up for Our Newsletter")])[1]//..//..//*[contains(text(), "Thank you!")]'

    def open_education_page(self):
        # self.open("https://www.nypl.org/education")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/education")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/education")
