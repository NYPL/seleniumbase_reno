from seleniumbase import BaseCase


class ResearchPage(BaseCase):
    home = '(//*[contains(text(), "Home")])[1]'
    research = '(//*[contains(text(), "Research")])[3]'
    h1 = '//*[@id="main-content"]//h1'

    search_the_research_catalog = '(//*[contains(text(), "Search the Research Catalog")])[1]'
    search_bar = '//*[@id="external-search-form-input"]'
    search_button = '//*[@id="external-search-form-button"]'

    start_your_research = '(//*[contains(text(), "Start Your Research")])[1]//..//li'
    visit_the_library_research_center = '(//*[contains(text(), "Visit the Library’s Research Centers")])[1]//..//li'
    other_centers = '((//*[contains(text(), "Visit the Library’s Research Centers")])[1]/../following-sibling::*)[1]//li'
    explore_exhibitions_events = '(//*[contains(text(), "Explore Exhibitions")])[1]//..//li'
    find_fellowships = '(//*[contains(text(), "Find Fellowships")])[1]//..//li'
    get_research_support = '(//*[contains(text(), "Get Research")])[1]//..//li'

    email_subscription = '(//*[contains(text(), "Sign Up for Our Newsletter")])[1]'
    email_subs_input = '//input[@name="email"]'
    submit_email = '(//*[contains(text(), "Submit")])[1]'
    subs_confirmation = '(//*[contains(text(), "Sign Up for Our Newsletter")]//..//*[contains(text(), "Thank you!")])[1]'

    def open_research_page(self):
        # self.open("https://www.nypl.org/research")

        qa = "https://www.nypl.org/research"
        prod = "https://www.nypl.org/research"

        if self.env == "qa":
            print("Running on QA Env")
            self.open(qa)

        else:
            print("Running on Production Env")
            self.open(prod)
