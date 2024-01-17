from seleniumbase import BaseCase


class FooterPage(BaseCase):
    accessibility = '(//*[contains(text(), "Accessibility")])'
    press = '(//*[contains(text(), "Press")])'
    careers = '(//*[contains(text(), "Careers")])'
    space_rental = '(//*[contains(text(), "Space Rental")])'

    privacy_policy = '(//*[contains(text(), "Privacy Policy")])'
    other_policies = '(//*[contains(text(), "Other Policies")])'
    terms_conditions = '(//*[contains(text(), "Terms & Conditions")])'
    governance = '(//*[contains(text(), "Governance")])'

    rules_regulations = '(//*[contains(text(), "Rules & Regulations")])'
    about_nypl = '(//*[contains(text(), "About NYPL")])'
    language = '(//*[contains(text(), "Language")])'

    facebook = '//*[contains(text(), "NYPL on Facebook")]/..'
    twitter = '//*[contains(text(), "NYPL on Twitter")]/..'
    instagram = '//*[contains(text(), "NYPL on Instagram")]/..'
    youtube = '//*[contains(text(), "NYPL on Youtube")]/..'

    # footer is using same page as page_home
    """
    def open_home_page(self):
        # self.open("https://www.nypl.org/")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/")
    """
