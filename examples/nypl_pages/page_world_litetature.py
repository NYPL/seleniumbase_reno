from seleniumbase import BaseCase


class WorldLiteraturePage(BaseCase):
    home = '//*[@id="block-nypl-emulsify-breadcrumbs"]/nav/ul/li[1]/a'
    spotlight = '//*[@id="block-nypl-emulsify-breadcrumbs"]/nav/ul/li[2]/a'

    world_literature_title = "NYPL's World Literature Festival | The New York Public Library"

    hero = '//*[@id="block-content-hero-header"]/div/div[2]'

    authors_in_conversation_links = "//*[contains(text(), 'Authors in Conversation')]//following-sibling::div//a"
    panel_events__links = "//*[contains(text(), 'Panel Events')]//following-sibling::div//a"
    live_from_nypl_links = "//*[contains(text(), 'LIVE from NYPL')]//following-sibling::div//a"
    explore_all_events = "//*[contains(text(), 'Explore All Events')]"
    reading_recommendations = "//*[contains(text(), 'Reading Recommendations')]"
    multilingual_resources = "//*[contains(text(), 'Multilingual')]//parent::h2//following-sibling::div//a"
    recommended_literature = "//*[contains(text(), 'Recommended: Literature')]"
    top_checkouts = "//*[contains(text(), 'Top Checkouts')]"
    learn_a_language = "//*[contains(text(), 'Learn a Language')]//following-sibling::div//a"
    highlights_from = "//*[contains(text(), 'Highlights from')]"
    get_a_digital_lib_card = "//*[contains(text(), 'Get a Digital')]"
    download_the_nypl_app = "//*[contains(text(), 'Download the NYPL App')]"
    get_started_with_simplyE = "//*[contains(text(), 'Get Started with SimplyE')]"
    get_help = "(//*[contains(text(), 'Get Help')])[2]"
    connect_with_the_library = "//*[contains(text(), 'Connect with the Library')]//following-sibling::div//a"
    help_us_support = "//*[contains(text(), 'Help Us Support')]"


    def open_world_literature_page(self):
        # self.open("https://www.nypl.org/spotlight/world-literature-festival")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/spotlight/world-literature-festival")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/spotlight/world-literature-festival")
