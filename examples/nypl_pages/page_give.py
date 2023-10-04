from seleniumbase import BaseCase


class GivePage(BaseCase):

    home = '(//*[contains(text(), "Home")])[1]'
    h1 = '//*[@id="main-content"]//h1'
    donate = '(//*[contains(text(), "Donate")])[2]'

    donation_form = '//*[@id="donation-form"]'
    donate_text_field = '//*[@id="donation-ways"]'
    single_donation = '//*[@id="donation-form"]/div[2]/a[1]'
    monthly_donation = '//*[@id="donation-form"]/div[2]/a[2]'

    membership_1 = '(//*[@id="link_card_list-7e9110de-42ae-432f-a544-362d5e206683"]//h3//a)[1]'
    membership_2 = '(//*[@id="link_card_list-7e9110de-42ae-432f-a544-362d5e206683"]//h3//a)[2]'

    get_involved_1 = '(//*[@id="link_card_list-dc8b55c3-1a49-4600-9b44-73e1b156f4b9"]//h3//a)[1]'
    get_involved_2 = '(//*[@id="link_card_list-dc8b55c3-1a49-4600-9b44-73e1b156f4b9"]//h3//a)[2]'

    more_ways_to_give_1 = '(//*[@id="link_card_list-038b9d4a-032d-41ca-9198-91dc4d41b4f7"]//h3//a)[1]'
    more_ways_to_give_2 = '(//*[@id="link_card_list-038b9d4a-032d-41ca-9198-91dc4d41b4f7"]//h3//a)[2]'
    more_ways_to_give_3 = '(//*[@id="link_card_list-038b9d4a-032d-41ca-9198-91dc4d41b4f7"]//h3//a)[3]'
    more_ways_to_give_4 = '(//*[@id="link_card_list-038b9d4a-032d-41ca-9198-91dc4d41b4f7"]//h3//a)[4]'
    more_ways_to_give_5 = '(//*[@id="link_card_list-038b9d4a-032d-41ca-9198-91dc4d41b4f7"]//h3//a)[5]'

    learn_about_corporate_1 = '(//*[@id="link_card_list-0087b62f-ad7f-4070-9069-d272f6ac6f6d"]//h3//a)[1]'
    learn_about_corporate_2 = '(//*[@id="link_card_list-0087b62f-ad7f-4070-9069-d272f6ac6f6d"]//h3//a)[2]'
    learn_about_corporate_3 = '(//*[@id="link_card_list-0087b62f-ad7f-4070-9069-d272f6ac6f6d"]//h3//a)[3]'

    def open_give_page(self):
        # self.open("https://www.nypl.org/give")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/give")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/give")
