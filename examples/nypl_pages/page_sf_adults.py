from seleniumbase import BaseCase


class EducationAdultsPage(BaseCase):
    home_button = '(//*[contains(text(), "Home")])[1]'
    education = '(//*[contains(text(), "Education")])[2]'
    title = "Adults | The New York Public Library"

    total_h2 = '(//*[@id="mainContent"]//h2)'
    email_subscription = '(//*[contains(text(), "Sign Up for Our Newsletter")])[1]'

    def open_education_adults_page(self):
        # self.open("https://www.nypl.org/education/adults")

        prod = "https://www.nypl.org/education/adults"
        qa = "https://qa-www.nypl.org/education/adults"

        if self.env == "qa":
            print("Running on QA Env")
            self.open(qa)

        else:
            print("Running on Production Env")
            self.open(prod)
