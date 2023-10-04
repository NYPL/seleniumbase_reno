from seleniumbase import BaseCase


class EducatorsPage(BaseCase):
    home_button = '(//*[contains(text(), "Home")])[1]'
    education = '(//*[contains(text(), "Education")])[2]'
    title = "Center for Educators & Schools | The New York Public Library"

    our_mission_read_more = '//*[@id="nypl-link"]'

    back_to_school_1 = '(//*[@id="link_card_list-febc3fa2-202f-4752-abd6-539610468c12"]//a)[1]'
    back_to_school_2 = '(//*[@id="link_card_list-febc3fa2-202f-4752-abd6-539610468c12"]//a)[2]'
    back_to_school_3 = '(//*[@id="link_card_list-febc3fa2-202f-4752-abd6-539610468c12"]//a)[3]'

    attend_events_1 = '(//*[@id="link_card_list-ebb3d2fa-47e8-4be7-a94a-ec5d988671a3"]//a)[1]'
    attend_events_2 = '(//*[@id="link_card_list-ebb3d2fa-47e8-4be7-a94a-ec5d988671a3"]//a)[2]'

    watch = '//*[@id="link_card_list-fa13eaf1-387e-412b-9c69-84856bafc233"]//a'

    teach_with_nypl = '(//*[@id="link_card_list-b1a25317-bf8b-41cf-b15c-42a9dd5be791"]//a)[1]'
    teach_with_nypl_1 = '(//*[@id="link_card_list-a0a6c44a-9d0c-4684-b3bd-00600270784f"]//a)[1]'
    teach_with_nypl_2 = '(//*[@id="link_card_list-a0a6c44a-9d0c-4684-b3bd-00600270784f"]//a)[2]'
    teach_with_nypl_3 = '(//*[@id="link_card_list-a0a6c44a-9d0c-4684-b3bd-00600270784f"]//a)[3]'
    teach_with_nypl_4 = '(//*[@id="link_card_list-a0a6c44a-9d0c-4684-b3bd-00600270784f"]//a)[4]'

    explore_resources_1 = '(//*[@id="link_card_list-2e1140c3-e65f-4b8a-b663-def2f59665ac"]//a)[1]'
    explore_resources_2 = '(//*[@id="link_card_list-2e1140c3-e65f-4b8a-b663-def2f59665ac"]//a)[2]'
    explore_resources_3 = '(//*[@id="link_card_list-2e1140c3-e65f-4b8a-b663-def2f59665ac"]//a)[3]'

    plan_in_class_1 = '(//*[@id="link_card_list-e9c7edf4-b2bd-4678-ba18-d5ebb312fe60"]//a)[1]'
    plan_in_class_2 = '(//*[@id="link_card_list-e9c7edf4-b2bd-4678-ba18-d5ebb312fe60"]//a)[2]'
    plan_in_class_3 = '(//*[@id="link_card_list-e9c7edf4-b2bd-4678-ba18-d5ebb312fe60"]//a)[3]'

    discover_books_lists = '(//*[@id="link_card_list-d0af11e2-e4c0-4e70-b5a4-0b4e4b4cfe78"]//a)[1]'

    apply_for_fellowship = '(//*[@id="link_card_list-4cc84649-6dd6-4fc0-b904-69a5f3cfdee9"]//a)[1]'

    find_additional_resources_1 = '(//*[@id="link_card_list-9caf400a-5b7d-4b5e-a1c2-6cbc68a45aec"]//a)[1]'
    find_additional_resources_2 = '(//*[@id="link_card_list-9caf400a-5b7d-4b5e-a1c2-6cbc68a45aec"]//a)[2]'
    find_additional_resources_3 = '(//*[@id="link_card_list-9caf400a-5b7d-4b5e-a1c2-6cbc68a45aec"]//a)[3]'
    find_additional_resources_4 = '(//*[@id="link_card_list-9caf400a-5b7d-4b5e-a1c2-6cbc68a45aec"]//a)[4]'

    connect_with_us_twitter = '(//*[@id="social-media-block-a5bd3bc4-5c62-47f0-96ac-fabf0f688fed"]//a)[1]'
    connect_with_us_instagram = '(//*[@id="social-media-block-a5bd3bc4-5c62-47f0-96ac-fabf0f688fed"]//a)[2]'
    connect_with_us_facebook = '(//*[@id="social-media-block-a5bd3bc4-5c62-47f0-96ac-fabf0f688fed"]//a)[3]'

    def open_educators_page(self):
        # self.open("https://www.nypl.org/education/educators")

        prod = "https://www.nypl.org/education/educators"
        qa = "https://qa-www.nypl.org/education/educators"

        if self.env == "qa":
            print("Running on QA Env")
            self.open(qa)

        else:
            print("Running on Production Env")
            self.open(prod)
