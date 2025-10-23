from seleniumbase import BaseCase


class ArticlesDatabasesPage(BaseCase):

    # breadcrumb locators
    home = '(//*[contains(text(), "Home")])[1]'
    research = '(//*[contains(text(), "Research")])[2]'
    collections = '(//*[contains(text(), "Online Resources & Databases")])[2]'

    articles_databases_title = "Online Resources & Databases | The New York Public Library"  # title

    all_links = '((//*[@id="page-container--content-primary"]//li)//a)'  # locator for 'page-container'

    # search locators
    search_bar = '//*[@id="external-search-form-input"]'
    submit_button = '//*[@id="external-search-form-button"]'

    # newsletter signup locators
    email_subscription = '(//*[contains(text(), "Sign Up for Our Newsletter")])[1]'
    email_subs_input = '//*[@name="email"]'
    submit_email = '(//*[contains(text(), "Submit")])[1]'
    subs_confirmation = '(//*[contains(text(), "Sign Up for Our Newsletter")])[1]//..//..//*[contains(text(), "Thank you!")]'

    def open_articles_databases_page(self):

        qa = 'https://qa-www.nypl.org/research/collections/online-resources-databases'
        prod = 'https://www.nypl.org/research/collections/online-resources-databases'

        if self.env == "qa":
            print("Running on QA Env")
            self.open(qa)
        else:
            print("Running on Production Env")
            self.open(prod)
