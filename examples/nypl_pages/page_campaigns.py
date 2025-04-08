from seleniumbase import BaseCase


class CampaignsPage(BaseCase):
    home = '(//*[contains(text(), "Home")])[1]'  # breadcrumb for all paths
    timeline_h1 = '(//*[contains(text(), "The New York Public Library Through the Years")])[2]'  # /timeline h1

    all_links = '((//*[@id="page-container--content-primary"])//a)'

    # /125 locators
    slide_images = '((//*[@id="slideshow-4cba29de-8c1c-4623-8375-7dfba10ad990"]//img))'  # list XPaths for the /125 slideshow

    # /timeline
    _125_years = '(//*[contains(text(), "125 Years of The")])[1]'  # breadcrumb for /timeline and /topcheckouts paths
    h2_cards = '((//*[@id="page-container--content-primary"]//h2))'  # h2 cards on the page
    main_h2 = '//*[@id="5af88053-71d0-4f19-83d5-702001d087e8"]'  # first h2 of the page, 'Celebrating 125 Years of' ...

    # /topcheckouts
    checkouts_h1 = '(//*[contains(text(), "Top 10 Checkouts of All Time")])[2]'  # /checkouts path h1
    honorable_mention = '//*[contains(text(), "Honorable Mention")]'
    top10_books = '(//*[contains(text(), "Request Book")])'

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
