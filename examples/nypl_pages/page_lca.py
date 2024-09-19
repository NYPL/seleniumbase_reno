from seleniumbase import BaseCase


class LibraryCardPage(BaseCase):
    x = ''

    def open_library_card_page(self, category=''):
        # self.open("https://www.nypl.org/library-card/new")

        base_url = "https://www.nypl.org/library-card/new"
        qa_base_url = "https://qa-www.nypl.org/library-card/new"

        url = f"{base_url}{category}"
        qa_url = f"{qa_base_url}{category}"

        # Open the appropriate URL based on the environment
        if self.env == "qa":
            print(f"Running on QA Env: Opening {category} page with URL: {qa_url}")
            self.open(qa_url)
        else:
            print(f"Running on Production Env: Opening {category} page with URL: {url}")
            self.open(url)
