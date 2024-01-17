from seleniumbase import BaseCase


class CampaignsPage(BaseCase):
    home = '(//*[contains(text(), "Home")])[1]'  # breadcrumb for all paths
    timeline_h1 = '(//*[contains(text(), "The New York Public Library Through the Years")])[2]'  # /timeline h1

    # /125 locators
    h2_links = '(//*[@id="block-nypl-emulsify-content"]//h2//a)'  # all h2 links on the base path /125
    slide_images = '(//*[@class="slideshow"]//li//img)'  # list XPaths for the /125 slideshow

    # /timeline
    _125_years = '(//*[contains(text(), "125 Years of The")])[1]'  # breadcrumb for /timeline and /topcheckouts paths
    h2_cards = '(//*[@id="block-nypl-emulsify-content"]//h2)'  # h2 cards on the page
    main_h2 = '//*[@id="featured-card--heading--1579"]'  # first h2 of the page, 'Celebrating 125 Years of' ...

    # /topcheckouts
    checkouts_h1 = '(//*[contains(text(), "Top 10 Checkouts of All Time")])[2]'  # /checkouts path h1
    topcheckouts_links = '(//*[@id="block-nypl-emulsify-content"]//a)'  # all links on the /topcheckouts page
    honorable_mention = '//*[contains(text(), "Honorable Mention")]'
    honorable_mention_book_links = '(//*[contains(text(), "Honorable Mention")]//..//..//a)'  # book link amount
    top10_books = '((//*[@class= "top-checkouts"])[1]//li)'

    def open_campaigns_page(self, category=''):
        # self.open("https://www.nypl.org/125")

        # Determine the base URLs
        base_url = "https://www.nypl.org/125/"
        qa_base_url = "https://qa-www.nypl.org/125/"

        url = f"{base_url}{category}"
        qa_url = f"{qa_base_url}{category}"

        # Open the appropriate URL based on the environment
        if self.env == "qa":
            print(f"Running on QA Env: Opening {category} page with URL: {qa_url}")
            self.open(qa_url)
        else:
            print(f"Running on Production Env: Opening {category} page with URL: {url}")
            self.open(url)
