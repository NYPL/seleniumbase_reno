from seleniumbase import BaseCase


class GetHelpPage(BaseCase):
    home_button = '(//*[contains(text(), "Home")])[1]'
    get_help = '(//*[contains(text(), "Get Help")])[3]'
    title = "Get Help | The New York Public Library"

    all_links = '((//*[@id="page-container--content-primary"]//li)//a)'  # locator for 'page-container'

    def open_get_help_page(self):
        # self.open("https://www.nypl.org/get-help")

        prod = "https://www.nypl.org/get-help"
        qa = "https://qa-www.nypl.org/get-help"

        if self.env == "qa":
            print("Running on QA Env")
            self.open(qa)

        else:
            print("Running on Production Env")
            self.open(prod)
