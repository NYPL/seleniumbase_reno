from seleniumbase import BaseCase


class FooterPage(BaseCase):
    accessibility = '//*[@id="nypl-footer"]//*[contains(text(), "Accessibility")]'
    press = '//*[@id="nypl-footer"]//*[contains(text(), "Press")]'
    careers = '//*[@id="nypl-footer"]//*[contains(text(), "Careers")]'
    space_rental = '//*[@id="nypl-footer"]//*[contains(text(), "Space Rental")]'

    privacy_policy = '//*[@id="nypl-footer"]//*[contains(text(), "Privacy Policy")]'
    other_policies = '//*[@id="nypl-footer"]//*[contains(text(), "Other Policies")]'
    terms_conditions = '//*[@id="nypl-footer"]//*[contains(text(), "Terms & Conditions")]'
    governance = '//*[@id="nypl-footer"]//*[contains(text(), "Governance")]'

    rules_regulations = '//*[@id="nypl-footer"]//*[contains(text(), "Rules & Regulations")]'
    about_nypl = '//*[@id="nypl-footer"]//*[contains(text(), "About NYPL")]'
    language = '//*[@id="nypl-footer"]//*[contains(text(), "Language")]'

    facebook = '//*[@id="nypl-footer"]//*[contains(text(), "NYPL on Facebook")]/..'
    twitter = '//*[@id="nypl-footer"]//*[contains(text(), "NYPL on Twitter")]/..'
    instagram = '//*[@id="nypl-footer"]//*[contains(text(), "NYPL on Instagram")]/..'
    youtube = '//*[@id="nypl-footer"]//*[contains(text(), "NYPL on Youtube")]/..'

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
