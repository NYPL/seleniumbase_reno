from seleniumbase import BaseCase


class FooterPage(BaseCase):
    accessibility = '//*[@id="nypl-footer"]//a[contains(text(), "Accessibility")]'
    press = '//*[@id="nypl-footer"]//a[contains(text(), "Press")]'
    careers = '//*[@id="nypl-footer"]//a[contains(text(), "Careers")]'
    space_rental = '//*[@id="nypl-footer"]//a[contains(text(), "Space Rental")]'

    privacy_policy = '//*[@id="nypl-footer"]//a[contains(text(), "Privacy Policy")]'
    other_policies = '//*[@id="nypl-footer"]//a[contains(text(), "Other Policies")]'
    terms_conditions = '//*[@id="nypl-footer"]//a[contains(text(), "Terms & Conditions")]'
    governance = '//*[@id="nypl-footer"]//a[contains(text(), "Governance")]'

    rules_regulations = '//*[@id="nypl-footer"]//a[contains(text(), "Rules & Regulations")]'
    about_nypl = '//*[@id="nypl-footer"]//a[contains(text(), "About NYPL")]'
    language = '//*[@id="nypl-footer"]//a[contains(text(), "Language")]'

    facebook = '(//*[@data-testid="social-media-links"]//li)[1]//a'
    twitter = '(//*[@data-testid="social-media-links"]//li)[2]//a'
    instagram = '(//*[@data-testid="social-media-links"]//li)[3]//a'
    youtube = '(//*[@data-testid="social-media-links"]//li)[4]//a'

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
