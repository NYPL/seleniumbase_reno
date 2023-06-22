from seleniumbase import BaseCase


class PosadaPage(BaseCase):
    home = '//*[@id="block-nypl-emulsify-breadcrumbs"]/nav/ul/li[1]/a'
    events = '//*[@id="block-nypl-emulsify-breadcrumbs"]/nav/ul/li[2]/a'
    exhibitions = '//*[@id="block-nypl-emulsify-breadcrumbs"]/nav/ul/li[3]/a'

    posada_title = 'The Skeleton Caricatures of Posada | Las meras meras calaveras de Posada | The New York Public Library'

    hero = '//*[@id="block-content-hero-header"]/div/div[2]/div[1]/h1/span'

    def open_posada_page(self):
        # self.open("https://www.nypl.org/events/exhibitions/posada")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/events/exhibitions/posada")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/events/exhibitions/posada")
