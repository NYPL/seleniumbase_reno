from seleniumbase import BaseCase


class EducationTeensPage(BaseCase):
    home_button = '(//*[contains(text(), "Home")])[1]'
    education = '(//*[contains(text(), "Education")])[2]'
    title = "Teens | The New York Public Library"

    all_links = '((//*[@id="page-container--content-primary"]//li)//a)'  # locator for 'page-container'

    # social media locators
    connect_with_us_instagram = "//a[@href='https://www.instagram.com/nyplteens/']"
    connect_with_us_facebook = "//a[@href='https://www.facebook.com/nyplteens']"
    connect_with_us_twitter = "//a[@href='https://twitter.com/nypl_teens']"

    def open_education_teens_page(self):
        # self.open("https://www.nypl.org/education/teens")

        prod = "https://www.nypl.org/education/teens"
        qa = "https://qa-www.nypl.org/education/teens"

        if self.env == "qa":
            print("Running on QA Env")
            self.open(qa)

        else:
            print("Running on Production Env")
            self.open(prod)
