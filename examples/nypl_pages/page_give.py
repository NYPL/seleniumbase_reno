from seleniumbase import BaseCase


class GivePage(BaseCase):

    home = '(//*[contains(text(), "Home")])[1]'
    h1 = '//*[@id="mainContent"]//h1'
    donate = '(//*[contains(text(), "Donate")])[2]'

    all_links = '((//*[@id="page-container--content-primary"]//li)//a)'  # locator for 'page-container'

    donation_form = '//*[@id="donation-form"]'
    donate_text_field = '//*[@id="donation-ways"]'
    single_donation = '(//*[contains(text(), "Single Donation")])[1]'
    monthly_donation = '(//*[contains(text(), "Monthly Donation")])[1]'

    def open_give_page(self):
        # self.open("https://www.nypl.org/give")

        base_url = "https://www.nypl.org/give"
        qa_base_url = "https://qa-www.nypl.org/give"

        url = f"{base_url}"
        qa_url = f"{qa_base_url}"

        # Open the appropriate URL based on the environment
        if self.env == "qa":
            print(f"Running on QA Env: Opening : {qa_url}")
            self.open(qa_url)
        else:
            print(f"Running on Production Env: Opening : {url}")
            self.open(url)
