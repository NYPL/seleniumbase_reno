from seleniumbase import BaseCase


class ContactUsPage(BaseCase):

    # breadcrumbs
    home = '(//*[contains(text(), "Home")])[1]'
    get_help = '(//*[contains(text(), "Get Help")])[2]'
    h1 = '//*[@id="mainContent"]//h1'

    contact_us_title = 'Contact Us | The New York Public Library'  # title

    all_links = '((//*[@id="page-container--content-primary"]//li)//a)'  # locator for 'page-container'

    def open_contact_us_page(self):
        # self.open("https://www.nypl.org/get-help/contact-us")

        base_url = "https://www.nypl.org/get-help/contact-us"
        qa_base_url = "https://qa-www.nypl.org/get-help/contact-us"

        url = f"{base_url}"
        qa_url = f"{qa_base_url}"

        # Open the appropriate URL based on the environment
        if self.env == "qa":
            print(f"Running on QA Env: Opening : {qa_url}")
            self.open(qa_url)
        else:
            print(f"Running on Production Env: Opening : {url}")
            self.open(url)
