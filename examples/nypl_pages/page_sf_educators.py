from seleniumbase import BaseCase


class EducatorsPage(BaseCase):
    home_button = '(//*[contains(text(), "Home")])[1]'
    education = '(//*[contains(text(), "Education")])[2]'
    title = "Center for Educators & Schools | The New York Public Library"

    our_mission_read_more = '//*[@id="nypl-link"]'

    all_links = '((//*[@id="page-container--content-primary"]//li)//a)'  # locator for 'page-container'

    # social media locators
    connect_with_us_twitter = "//a[@href='https://www.instagram.com/nypleducators/']"
    connect_with_us_instagram = "//a[@href='https://twitter.com/NYPLEducators']"
    connect_with_us_facebook = "//a[@href='https://www.facebook.com/NYPLEducators']"

    # newsletter signup locators
    email_subscription = '(//*[contains(text(), "Sign Up for the CES Newsletter")])[1]'
    email_subs_input = '//*[@name="email"]'
    # submit_email = '(//*[contains(text(), "Submit")])[1]'
    subs_confirmation = '(//*[contains(text(), "Sign Up for the CES Newsletter")])[1]//..//..//*[contains(text(), "Thank you!")]'

    def open_educators_page(self):
        # self.open("https://www.nypl.org/education/educators")

        prod = "https://www.nypl.org/education/educators"
        qa = "https://qa-www.nypl.org/education/educators"

        if self.env == "qa":
            print("Running on QA Env")
            self.open(qa)

        else:
            print("Running on Production Env")
            self.open(prod)
