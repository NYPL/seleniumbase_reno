from seleniumbase import BaseCase


class ExhibitionsPage(BaseCase):
    # main page elements
    home = '(//*[contains(text(), "Home")])[1]'
    events = '(//*[contains(text(), "Events")])[2]'
    exhibitions_h1 = '(//*[contains(text(), "Exhibitions")])[2]'

    h3_links_main = '(//*[@id="block-nypl-emulsify-content"]//h3//a)'
    h3_links_past_exhibitions = '(//*[@id="block-nypl-emulsify-content"]//a//h3)'
    current_exhibitions = '(//*[contains(text(), "Current Exhibitions")])[1]'
    see_all = '(//*[contains(text(), "See All")])'

    # /upcoming elements
    exhibitions = '(//*[contains(text(), "Exhibitions")])[2]'
    upcoming_1 = '(//*[contains(text(), "Upcoming Exhibitions")])[2]'
    next_page_1 = '(//*[contains(text(), "Next page")])'

    h3_links_upcoming = '(//*[@id="block-nypl-emulsify-content"]//h3//a)'
    pagination_list = '(//*[contains(text(), "Pagination")]//..//li//a)'

    # /past exhibitions
    past_exhibitions_h1 = '(//*[contains(text(), "Past Exhibitions")])[2]'
    next_page_2 = '(//*[contains(text(), "Next page")])'

    h3_links_past = '(//*[@id="block-nypl-emulsify-content"]//h3//a)'

    # /archived-exhibition-resources
    next_page_3 = '(//*[contains(text(), "Next page")])'
    archived_h1 = '(//*[contains(text(), "Archived Exhibition Resources")])[2]'
    archived_h2 = '//*[@id="44-archived-exhibition-resources-a-to-z"]'

    h3_links_archived = '(//*[@id="block-nypl-emulsify-content"]//h3//a)'

    # /community-showcases
    community_h1 = '(//*[contains(text(), "Community Showcases")])[2]'
    next_page_4 = '(//*[contains(text(), "Next page")])'

    no_community_showcase_1 = '/html/body/div[1]/div/main/div[2]/div/div/div/div/p'
    no_community_showcase_2 = '(//*[contains(text(), "No Community Showcases")])'  # use this, delete above one

    h3_links_community = '(//*[@id="block-nypl-emulsify-content"]//h3//a)'

    # /online
    online_h1 = '(//*[contains(text(), "Online Exhibitions")])[2]'
    h3_links_online = '(//*[@id="block-nypl-emulsify-content"]//h3//a)'

    def open_exhibitions_page(self, category=''):
        # self.open("https://www.nypl.org/events/exhibitions")

        # Determine the base URLs
        base_url = "https://www.nypl.org/events/exhibitions/"
        qa_base_url = "https://qa-www.nypl.org/events/exhibitions/"

        url = f"{base_url}{category}"
        qa_url = f"{qa_base_url}{category}"

        # Open the appropriate URL based on the environment
        if self.env == "qa":
            print(f"Running on QA Env: Opening {category} page with URL: {qa_url}")
            self.open(qa_url)
        else:
            print(f"Running on Production Env: Opening {category} page with URL: {url}")
            self.open(url)
