from seleniumbase import BaseCase


class PressPage(BaseCase):
    home = '(//*[contains(text(), "Home")])[1]'

    home_title = 'Press Releases | The New York Public Library'

    all_links = '((//*[@id="page-container--content-primary"]//li)//a)'  # locator for 'page-container'

    page_link_amount = '(//*[@id="press-releases"]//h3//a)'
    pagination_amount = '//*[@data-testid="ds-pagination"]//li'
    previous_button = '//*[@data-testid="ds-list"]//*[contains(text(), "Previous")]'

    def open_press_page(self):
        prod_url = "https://www.nypl.org/press"
        qa_url = "https://qa-www.nypl.org/press"

        if self.env == "qa":
            print("Running on QA Env")
            self.open(qa_url)

        else:
            print("Running on Production Env")
            self.open(prod_url)
