from seleniumbase import BaseCase


class EducationTeensPage(BaseCase):
    home_button = '(//*[contains(text(), "Home")])[1]'
    education = '(//*[contains(text(), "Education")])[2]'
    title = "Teens | The New York Public Library"

    back_to_school_1 = '(//*[@id="link_card_list-680e1c91-409c-4df3-aa2a-8834a94efea1"]//a)[1]'
    back_to_school_2 = '(//*[@id="link_card_list-680e1c91-409c-4df3-aa2a-8834a94efea1"]//a)[2]'
    back_to_school_3 = '(//*[@id="link_card_list-680e1c91-409c-4df3-aa2a-8834a94efea1"]//a)[3]'
    back_to_school_4 = '(//*[@id="link_card_list-680e1c91-409c-4df3-aa2a-8834a94efea1"]//a)[4]'

    opportunities_1 = '(//*[@id="link_card_list-4d7481ec-8a24-4387-a1e5-7cf10979cb25"]//a)[1]'
    opportunities_2 = '(//*[@id="link_card_list-4d7481ec-8a24-4387-a1e5-7cf10979cb25"]//a)[2]'
    opportunities_3 = '(//*[@id="link_card_list-4d7481ec-8a24-4387-a1e5-7cf10979cb25"]//a)[3]'

    teen_voices_1 = '(//*[@id="link_card_list-2e3c28c0-0c1e-45e1-a337-65fc29e5e940"]//a)[1]'
    teen_voices_2 = '(//*[@id="link_card_list-2e3c28c0-0c1e-45e1-a337-65fc29e5e940"]//a)[2]'
    teen_voices_3 = '(//*[@id="link_card_list-2e3c28c0-0c1e-45e1-a337-65fc29e5e940"]//a)[3]'

    academic_resources_1 = '(//*[@id="link_card_list-dd31cb8e-673f-4f37-b3a3-9f1ba4c3c3f3"]//a)[1]'
    academic_resources_2 = '(//*[@id="link_card_list-dd31cb8e-673f-4f37-b3a3-9f1ba4c3c3f3"]//a)[2]'

    books_ebooks_1 = '(//*[@id="link_card_list-6af30796-66dd-407b-bc5b-5790ad940d28"]//a)[1]'
    books_ebooks_2 = '(//*[@id="link_card_list-6af30796-66dd-407b-bc5b-5790ad940d28"]//a)[2]'
    books_ebooks_3 = '(//*[@id="link_card_list-6af30796-66dd-407b-bc5b-5790ad940d28"]//a)[3]'
    books_ebooks_4 = '(//*[@id="link_card_list-6af30796-66dd-407b-bc5b-5790ad940d28"]//a)[4]'

    teens_360 = '(//*[@id="link_card_list-bb9e8685-7a70-4385-9b6d-68c2c203e7b8"]//a)[1]'

    more_from_nypl_1 = '(//*[@id="link_card_list-ba3dae5f-9a8c-4796-8338-07fd02a27296"]//a)[1]'
    more_from_nypl_2 = '(//*[@id="link_card_list-ba3dae5f-9a8c-4796-8338-07fd02a27296"]//a)[2]'
    more_from_nypl_3 = '(//*[@id="link_card_list-ba3dae5f-9a8c-4796-8338-07fd02a27296"]//a)[3]'

    follow_nypl_teens_instagram = '(//*[@id="social-media-block-f905fbdd-8d5b-4c07-b027-76d120a2a95d"]//a)[1]'
    follow_nypl_teens_facebook = '(//*[@id="social-media-block-f905fbdd-8d5b-4c07-b027-76d120a2a95d"]//a)[2]'
    follow_nypl_teens_3_twitter = '(//*[@id="social-media-block-f905fbdd-8d5b-4c07-b027-76d120a2a95d"]//a)[3]'

    def open_education_teens_page(self):
        # self.open("https://www.nypl.org/education/teens")

        prod = "https://www.nypl.org/education/teens"
        qa = "https://qa-www.nypl.org/education/teens"

        if self.env == "qa":
            print("Running on QA Env")
            self.open(qa)

        else:
            print("Running on Production Env")
            self.open(prod)
