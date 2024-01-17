from seleniumbase import BaseCase


class GivePage(BaseCase):

    home = '(//*[contains(text(), "Home")])[1]'
    h1 = '//*[@id="main-content"]//h1'
    donate = '(//*[contains(text(), "Donate")])[2]'

    donation_form = '//*[@id="donation-form"]'
    donate_text_field = '//*[@id="donation-ways"]'
    single_donation = '(//*[contains(text(), "Single Donation")])[1]'
    monthly_donation = '(//*[contains(text(), "Monthly Donation")])[1]'

    membership_1 = '((//*[contains(text(), "Membership")])[1]//..//h3)[1]//a'
    membership_2 = '((//*[contains(text(), "Membership")])[1]//..//h3)[2]//a'

    get_involved_1 = '((//*[contains(text(), "Get Involved")])[1]//..//h3)[1]//a'
    get_involved_2 = '((//*[contains(text(), "Get Involved")])[1]//..//h3)[2]//a'

    more_ways_to_give_1 = '((//*[contains(text(), "More Ways to Give")])[1]//..//h3)[1]//a'
    more_ways_to_give_2 = '((//*[contains(text(), "More Ways to Give")])[1]//..//h3)[2]//a'
    more_ways_to_give_3 = '((//*[contains(text(), "More Ways to Give")])[1]//..//h3)[3]//a'
    more_ways_to_give_4 = '((//*[contains(text(), "More Ways to Give")])[1]//..//h3)[4]//a'
    more_ways_to_give_5 = '((//*[contains(text(), "More Ways to Give")])[1]//..//h3)[5]//a'

    learn_about_corporate_1 = '((//*[contains(text(), "Learn About")])[1]//..//h3)[1]//a'
    learn_about_corporate_2 = '((//*[contains(text(), "Learn About")])[1]//..//h3)[2]//a'
    learn_about_corporate_3 = '((//*[contains(text(), "Learn About")])[1]//..//h3)[3]//a'

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
