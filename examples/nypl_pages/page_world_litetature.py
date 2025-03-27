from seleniumbase import BaseCase


class WorldLiteraturePage(BaseCase):
    home = '(//*[contains(text(), "Home")])[1]'
    spotlight = '(//*[contains(text(), "Spotlight")])[1]'

    world_literature_title = "NYPL's World Literature & Arts Festival | The New York Public Library"

    hero = '//*[@id="block-content-hero-header"]'

    all_links = '((//*[@id="block-nypl-emulsify-content"]//li)//a)'  # all links locator for 'Emulsify'

    def open_world_literature_page(self):
        # self.open("https://www.nypl.org/spotlight/world-literature-festival")

        prod = "https://www.nypl.org/spotlight/world-literature-festival"
        qa = "https://qa-www.nypl.org/spotlight/world-literature-festival"

        if self.env == "qa":
            print("Running on QA Env")
            self.open(qa)

        else:
            print("Running on Production Env")
            self.open(prod)
