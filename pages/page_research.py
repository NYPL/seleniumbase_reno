from seleniumbase import BaseCase


class ResearchPage(BaseCase):
    home = '(//*[contains(text(), "Home")])[1]'
    research = '//*[@data-testid="ds-breadcrumbs"]//*[contains(text(), "Research")]'
    h1 = '//*[@id="mainContent"]//h1'

    all_links = '((//*[@id="page-container--content-primary"]//li)//a)'  # locator for 'page-container'

    # the site header has a hidden "Search the Research Catalog" too, so target the page heading
    search_the_research_catalog = '//*[@data-testid="ds-heading" and contains(text(), "Search the Research Catalog")]'
    search_bar = '//*[@id="research-catalog-searchbar-textInput"]'
    search_button = '//*[@data-testid="ds-button"]/*[contains(text(), "Search")]'

    # newsletter signup locators
    email_subscription = '(//*[contains(text(), "Sign Up for Our Newsletter")])[1]'
    email_subs_input = '//*[@name="email"]'
    submit_email = '(//*[contains(text(), "Submit")])[1]'
    subs_confirmation = '(//*[contains(text(), "Sign Up for Our Newsletter")])[1]//..//..//*[contains(text(), "Thank you!")]'

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
