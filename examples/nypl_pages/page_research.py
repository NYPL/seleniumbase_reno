from seleniumbase import BaseCase


class ResearchPage(BaseCase):
    home = '(//*[contains(text(), "Home")])[1]'
    research = '(//*[contains(text(), "Research")])[3]'
    h1 = '//*[@id="main-content"]//h1'

    search_the_research_catalog = '//*[@id="external-search-a3f839cc-758d-4ff6-bb1f-fb0a2724a061"]'
    search_bar = '//*[@id="external-search-form-input"]'
    search_button = '//*[@id="external-search-form-button"]'

    start_your_research = '//*[@id="link_card_list-40d437f9-287c-4430-a4eb-d2de380ebb62"]/ul/li'
    visit_the_library_research_center = '//*[@id="link_card_list-5033bd3a-7b96-4a3a-80ee-1a9c4f03740e"]/ul/li'
    additional_research_centers = '//*[@id="link_card_list-b0f93c17-af3b-44d5-9480-2c633f9bb151"]/ul/li'
    explore_exhibitions_events = '//*[@id="link_card_list-e75820ee-f6a5-4509-8927-09b40f28d92a"]/ul/li'
    find_fellowships = '//*[@id="link_card_list-21b39f30-58f7-4940-840b-ee770d1cdf06"]/ul/li'
    get_research_support = '//*[@id="link_card_list-ff674813-45f5-4233-afc8-55c6e7736591"]/ul/li'

    email_subscription = '//*[@id="email-subscription-wrapper-0172da91-eb0e-4eaf-81c5-e77d58f54a05"]'
    email_subs_input = '//*[@id="email-input-0172da91-eb0e-4eaf-81c5-e77d58f54a05"]'
    submit_email = '//*[@id="email-submit-button-0172da91-eb0e-4eaf-81c5-e77d58f54a05"]'
    subs_confirmation = '//*[@id="email-subscription-confirmation-0172da91-eb0e-4eaf-81c5-e77d58f54a05"]/div/text()'

    def open_research_page(self):
        # self.open("https://www.nypl.org/research")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://www.nypl.org/research")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/research")
