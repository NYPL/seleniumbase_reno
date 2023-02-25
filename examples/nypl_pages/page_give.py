from seleniumbase import BaseCase


class GivePage(BaseCase):

    home = '//*[@id="__next"]/div/div[2]/nav/ol/li[1]/a/span'
    h1 = '//*[@id="main-content"]/div[1]/div[1]/div/h1'
    donate = '//*[@id="overlay"]/div/div[1]/h2'

    donation_form = '//*[@id="donation-form"]'
    donate_text_field = '//*[@id="donation-ways"]'
    single_donation = '//*[@id="donation-form"]/div[2]/a[1]'
    monthly_donation = '//*[@id="donation-form"]/div[2]/a[2]'

    def open_give_page(self):
        # self.open("https://www.nypl.org/give")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/give")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/give")
