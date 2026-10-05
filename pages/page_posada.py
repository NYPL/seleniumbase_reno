from seleniumbase import BaseCase


class PosadaPage(BaseCase):
    home = '(//*[contains(text(), "Home")])[1]'
    events = '(//*[contains(text(), "Events")])[2]'
    exhibitions = '(//*[contains(text(), "Exhibitions")])[1]'

    posada_title = 'The Skeleton Caricatures of Posada | Las meras meras calaveras de Posada | The New York Public Library'

    hero = '(//*[@id="block-content-hero-header"])'

    all_links = '((//*[@id="block-nypl-emulsify-content"]//a))'  # locator for 'emulsify'

    previous_button_1 = '(//*[@title="Previous"])[1]'
    next_button_1 = '(//*[@title="Next"])[1]'
    slide_images_1 = '(//*[@class="slideshow"])[1]//img'

    previous_button_2 = '(//*[@title="Previous"])[2]'
    next_button_2 = '(//*[@title="Next"])[2]'
    slide_images_2 = '(//*[@class="slideshow"])[1]//img'

    def open_posada_page(self):
        prod_url = "https://www.nypl.org/events/exhibitions/posada"
        qa_url = "https://qa-www.nypl.org/events/exhibitions/posada"

        if self.env == "qa":
            print("Running on QA Env")
            self.open(qa_url)

        else:
            print("Running on Production Env")
            self.open(prod_url)
