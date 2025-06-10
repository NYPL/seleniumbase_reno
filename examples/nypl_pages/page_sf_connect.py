from seleniumbase import BaseCase


class ConnectPage(BaseCase):

    # breadcrumbs
    home = '//*[contains(@class, "breadcrumb-label") and contains(text(), "Home")]'
    connect = '//*[contains(@class, "breadcrumb-label") and contains(text(), "Connect")]'
    h1 = '//*[@id="mainContent"]//h1'

    connect_title = 'Connect | The New York Public Library'  # title

    all_links = '((//*[@id="page-container--content-primary"]//li)//a)'  # locator for 'page-container'

    # social media locators
    follow_us_twitter = "//a[@href='https://www.twitter.com/nypl/']"  # does not consist as of 6/10/2025
    follow_us_instagram = "//a[@href='https://instagram.com/nypl']"
    follow_us_facebook = "//a[@href='https://www.facebook.com/nypl']"

    # newsletter signup locators
    email_subscription = '(//*[contains(text(), "Get the Best of NYPL in Your Inbox")])[1]'
    email_subs_input = '//*[@id="email-input"]'
    # submit_email = '(//*[contains(text(), "Submit")])[1]'
    subs_confirmation = '(//*[contains(text(), "Get the Best of NYPL in Your Inbox")])[1]//..//..//*[contains(text(), "Thank you!")]'


    def open_connect_page(self):
        # self.open("https://www.nypl.org/connect")

        base_url = "https://www.nypl.org/connect"
        qa_base_url = "https://qa-www.nypl.org/connect"

        url = f"{base_url}"
        qa_url = f"{qa_base_url}"

        # Open the appropriate URL based on the environment
        if self.env == "qa":
            print(f"Running on QA Env: Opening : {qa_url}")
            self.open(qa_url)
        else:
            print(f"Running on Production Env: Opening : {url}")
            self.open(url)
