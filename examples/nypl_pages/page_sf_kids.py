from seleniumbase import BaseCase


class EducationKidsPage(BaseCase):
    home_button = '(//*[contains(text(), "Home")])[1]'
    education = '(//*[contains(text(), "Education")])[2]'
    title = "Kids | The New York Public Library"

    total_h2 = '(//*[@id="mainContent"]//h2)'
    email_subscription = '(//*[contains(text(), "Connect with Us")])[1]'

    def open_education_kids_page(self):
        # self.open("https://www.nypl.org/education/kids")

        prod = "https://www.nypl.org/education/kids"
        qa = "https://www.nypl.org/education/kids"

        if self.env == "qa":
            print("Running on QA Env")
            self.open(qa)

        else:
            print("Running on Production Env")
            self.open(prod)
