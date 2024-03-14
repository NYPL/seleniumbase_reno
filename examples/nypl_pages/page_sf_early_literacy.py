from seleniumbase import BaseCase


class EarlyLiteracyPage(BaseCase):

    # todo: locators need to be updated
    home_button = '(//*[contains(text(), "Home")])[1]'
    education = '(//*[contains(text(), "Education")])[2]'
    title = "Early Literacy | The New York Public Library"

    visit_library_1 = '(//*[@id="link_card_list-88cb5b61-79f1-4c41-a417-c28fc546aead"]//a)[1]'
    visit_library_2 = '(//*[@id="link_card_list-88cb5b61-79f1-4c41-a417-c28fc546aead"]//a)[2]'
    visit_library_3 = '(//*[@id="link_card_list-88cb5b61-79f1-4c41-a417-c28fc546aead"]//a)[3]'

    staten_island = '//*[@id="link_card_list-4dc89417-ab92-4b32-85b2-48f43016df35"]//a'

    activities_for_learners_1 = '(//*[@id="link_card_list-acbbbbf6-410e-4beb-9bcb-4f6878107f0c"]//a)[1]'
    activities_for_learners_2 = '(//*[@id="link_card_list-acbbbbf6-410e-4beb-9bcb-4f6878107f0c"]//a)[2]'
    activities_for_learners_3 = '(//*[@id="link_card_list-acbbbbf6-410e-4beb-9bcb-4f6878107f0c"]//a)[3]'
    activities_for_learners_4 = '(//*[@id="link_card_list-acbbbbf6-410e-4beb-9bcb-4f6878107f0c"]//a)[4]'

    early_literacy_spanish = '//*[@id="link_card_list-c12a83d0-c35a-43eb-8838-847c2320eb6e"]//a'
    early_literacy_chinese = '//*[@id="link_card_list-166b08d1-c7ab-4e1c-bde4-32b82ecb2f7e"]//a'

    def open_early_literacy_page(self):
        # self.open("https://www.nypl.org/education/early-literacy")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/education/early-literacy")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/education/early-literacy")
