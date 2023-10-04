from seleniumbase import BaseCase


class EducationPage(BaseCase):
    home_button = '(//*[contains(text(), "Home")])[1]'
    title = "Education | The New York Public Library"

    learning_opportunities_1 = '(//*[@id="link_card_list-e4b83c72-1f82-4775-8a10-ee5fd2041f2c"]//a)[1]'
    learning_opportunities_2 = '(//*[@id="link_card_list-e4b83c72-1f82-4775-8a10-ee5fd2041f2c"]//a)[2]'
    learning_opportunities_3 = '(//*[@id="link_card_list-e4b83c72-1f82-4775-8a10-ee5fd2041f2c"]//a)[3]'
    learning_opportunities_4 = '(//*[@id="link_card_list-e4b83c72-1f82-4775-8a10-ee5fd2041f2c"]//a)[4]'

    center_for_educators = '//*[@id="link_card_list-79ecaf00-7414-4e45-92c0-3ebe9fd97835"]//a'
    multilingual_resources = '//*[@id="link_card_list-7077f704-dc25-4732-8de7-ce4f703d34dc"]//a'

    more_for_babies_1 = '(//*[@id="link_card_list-2e55793e-f684-4481-9cba-db31319eede7"]//a)[1]'
    more_for_babies_2 = '(//*[@id="link_card_list-2e55793e-f684-4481-9cba-db31319eede7"]//a)[2]'
    more_for_babies_3 = '(//*[@id="link_card_list-2e55793e-f684-4481-9cba-db31319eede7"]//a)[3]'
    more_for_babies_4 = '(//*[@id="link_card_list-2e55793e-f684-4481-9cba-db31319eede7"]//a)[4]'

    more_for_kids_1 = '(//*[@id="link_card_list-447740c4-83d8-4ac8-b549-288d886168e2"]//a)[1]'
    more_for_kids_2 = '(//*[@id="link_card_list-447740c4-83d8-4ac8-b549-288d886168e2"]//a)[2]'
    more_for_kids_3 = '(//*[@id="link_card_list-447740c4-83d8-4ac8-b549-288d886168e2"]//a)[3]'
    more_for_kids_4 = '(//*[@id="link_card_list-447740c4-83d8-4ac8-b549-288d886168e2"]//a)[4]'

    more_for_teens_1 = '(//*[@id="link_card_list-2a966580-6f2e-4a87-9f7c-96385217d5ca"]//a)[1]'
    more_for_teens_2 = '(//*[@id="link_card_list-2a966580-6f2e-4a87-9f7c-96385217d5ca"]//a)[2]'
    more_for_teens_3 = '(//*[@id="link_card_list-2a966580-6f2e-4a87-9f7c-96385217d5ca"]//a)[3]'
    more_for_teens_4 = '(//*[@id="link_card_list-2a966580-6f2e-4a87-9f7c-96385217d5ca"]//a)[4]'

    more_for_adults_1 = '(//*[@id="link_card_list-29ac1695-587e-47d0-b942-56d217586091"]//a)[1]'
    more_for_adults_2 = '(//*[@id="link_card_list-29ac1695-587e-47d0-b942-56d217586091"]//a)[2]'
    more_for_adults_3 = '(//*[@id="link_card_list-29ac1695-587e-47d0-b942-56d217586091"]//a)[3]'
    more_for_adults_4 = '(//*[@id="link_card_list-29ac1695-587e-47d0-b942-56d217586091"]//a)[4]'

    more_for_educators_1 = '(//*[@id="link_card_list-15eaef79-5674-4580-a9ab-f8140606a89e"]//a)[1]'
    more_for_educators_2 = '(//*[@id="link_card_list-15eaef79-5674-4580-a9ab-f8140606a89e"]//a)[2]'
    more_for_educators_3 = '(//*[@id="link_card_list-15eaef79-5674-4580-a9ab-f8140606a89e"]//a)[3]'
    more_for_educators_4 = '(//*[@id="link_card_list-15eaef79-5674-4580-a9ab-f8140606a89e"]//a)[4]'

    def open_education_page(self):
        # self.open("https://www.nypl.org/education")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/education")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/education")
