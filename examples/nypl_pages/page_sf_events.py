from seleniumbase import BaseCase


class EventsPage(BaseCase):
    home_button = '(//*[contains(text(), "Home")])[1]'
    events = '(//*[contains(text(), "Events")])[3]'
    title = "Events | The New York Public Library"

    all_links = '((//*[@id="page-container--content-primary"]//li)//a)'  # locator for 'page-container'

    # newsletter signup locators
    email_subscription = '(//*[contains(text(), "Sign Up for Our Newsletter")])[1]'
    email_subs_input = '//*[@name="email"]'
    submit_email = '(//*[contains(text(), "Submit")])[1]'
    subs_confirmation = '(//*[contains(text(), "Sign Up for Our Newsletter")])[1]//..//..//*[contains(text(), "Thank you!")]'

    def open_events_page(self):
        # self.open("https://www.nypl.org/events")

        prod = "https://www.nypl.org/events"
        qa = "https://qa-www.nypl.org/events"

        if self.env == "qa":
            print("Running on QA Env")
            self.open(qa)

        else:
            print("Running on Production Env")
            self.open(prod)
