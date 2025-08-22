from seleniumbase import BaseCase


class ExhibitionsPage(BaseCase):
    # main page elements
    home = '//a[contains(@href, "/")]//span[contains(., "Home")]'
    events = '//a[contains(@href, "/events")]//span[contains(., "Events")]'
    exhibitions_h1 = '//a[contains(@href, "/events/exhibitions")]//span[contains(., "Exhibitions")]'

    all_links = '((//*[@id="page-container--content-primary"]//li)//a)'

    current_exhibitions = '(//*[contains(text(), "Current Exhibitions")])[1]'
    see_all = '(//*[contains(text(), "See All")])'

    # /upcoming elements
    exhibitions = '(//*[contains(text(), "Exhibitions")])[2]'
    upcoming_1 = '(//*[contains(text(), "Upcoming Exhibitions")])[2]'
    next_page = '(//*[contains(text(), "Next page")])'

    pagination_list = '(//*[contains(text(), "Pagination")]//..//li//a)'

    # /past exhibitions
    past_exhibitions_h1 = '(//*[contains(text(), "Past Exhibitions")])[2]'

    # /archived-exhibition-resources
    archived_h1 = '(//*[contains(text(), "Archived Exhibition Resources")])[2]'
    archived_h2 = '//*[@id="44-archived-exhibition-resources-a-to-z"]'

    # /community-showcases
    community_h1 = '(//*[contains(text(), "Community Showcases")])[2]'
    no_community_showcase = '(//*[contains(text(), "No Community Showcases")])'  # use this, delete above one

    # /online
    online_h1 = '(//*[contains(text(), "Online Exhibitions")])[2]'

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
