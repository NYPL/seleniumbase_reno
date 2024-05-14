from seleniumbase import BaseCase


class PressPage(BaseCase):
    home = '(//*[contains(text(), "Home")])[1]'

    home_title = 'Press Releases | The New York Public Library'

    page_link_amount = '(//*[@id="press-releases"]//h3//a)'
    pagination_amount = '//*[@id="undefined-list"]/li'
    previous_button = '//*[@id="undefined-Previous"]'

    def open_press_page(self):
        prod_url = "https://www.nypl.org/press"
        qa_url = "https://qa-www.nypl.org/press"

        if self.env == "qa":
            print("Running on QA Env")
            self.open(qa_url)

        else:
            print("Running on Production Env")
            self.open(prod_url)
