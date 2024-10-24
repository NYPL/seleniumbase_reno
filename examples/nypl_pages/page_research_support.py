from seleniumbase import BaseCase


class ResearchSupportPage(BaseCase):
    home = '(//*[contains(text(), "Home")])[1]'
    research = '(//*[contains(text(), "Research")])[2]'
    support_services = '(//*[contains(text(), "Support and Services")])[2]'
    h1 = '//*[@data-testid="hero"]'

    all_h2_links = '(//*[@id="page-container--content-primary"]//li)'

    email_subscription = '(//*[contains(text(), "Sign Up for Our Newsletter")])[1]'
    email_subs_input = '//*[@id="email-input"]'
    submit_email = '(//*[contains(text(), "Submit")])[1]'
    subs_confirmation = '(//*[contains(text(), "Sign Up for Our Newsletter")])[1]//..//..//*[contains(text(), "Thank you!")]'

    def open_research_support_page(self):
        # self.open("https://www.nypl.org/research/support")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://www.nypl.org/research/support")

        else:
            # print("Running on Production Env")
            self.open("https://www.nypl.org/research/support")
