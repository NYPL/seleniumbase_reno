from seleniumbase import BaseCase


class CampaignsPage(BaseCase):
    home = '//*[@id="block-nypl-emulsify-breadcrumbs"]/nav/ul/li/a'
    _125_years = '//*[@id="block-nypl-emulsify-breadcrumbs"]/nav/ul/li[2]/a'
    topcheckout_paragraphs = '//*[@id="block-nypl-emulsify-content"]/div/div/div[1]/div/div/p'
    timeline_h1 = '//*[@id="block-content-hero-header"]/div/div[2]/h1/span'
    checkouts_h1 = '//*[@id="block-content-hero-header"]/div/div[2]/h1/span'
    main_card = '//*[@id="block-content-hero-header"]/div/div[2]'
    second_card = '//*[@id="block-nypl-emulsify-content"]/div/div/div[1]'

    def open_campaigns_page(self):
        # self.open("https://www.nypl.org/125")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/125")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/125")
