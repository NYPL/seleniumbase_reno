from seleniumbase import BaseCase


class ResearchSupportPage(BaseCase):
    home = '(//*[contains(text(), "Home")])[1]'
    research = '(//*[contains(text(), "Research")])[2]'
    support_services = '(//*[contains(text(), "Support and Services")])[2]'
    h1 = '//*[@id="mainContent"]/div[1]/div'

    how_to_start_your_search = '//*[@id="link_card_list-23c628f7-1089-4725-98ea-ce65821110a9"]/ul/li'
    additional_info_section = '//*[@id="link_card_list-01d7423d-6c7c-427b-ab93-1bfc111f2a7e"]/ul/li'
    specialized_support = '//*[@id="link_card_list-b1a0ede0-1cdc-4a29-8e55-d99e60eefc83"]/ul/li'
    additional_research_services = '//*[@id="link_card_list-802d863c-dc92-4608-b19a-d9872672aaff"]/ul/li'
    find_fellowship = '//*[@id="link_card_list-69dc2275-f165-42ec-b36a-9a8fe958c864"]/ul/li'
    additional_fellowships = '//*[@id="link_card_list-c335acdc-ebd4-4ef0-8d3a-a09f7766af27"]/ul/li'

    email_subscription = '//*[@id="email-subscription-wrapper-4da4692e-0741-4f72-b1a1-2803a7981e9b"]'
    email_subs_input = '//*[@id="email-input-4da4692e-0741-4f72-b1a1-2803a7981e9b"]'
    submit_email = '//*[@id="email-submit-button-4da4692e-0741-4f72-b1a1-2803a7981e9b"]'
    subs_confirmation = '//*[@id="email-subscription-confirmation-4da4692e-0741-4f72-b1a1-2803a7981e9b"]/div'

    def open_research_support_page(self):
        # self.open("https://www.nypl.org/research/support")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://www.nypl.org/research/support")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/research/support")
