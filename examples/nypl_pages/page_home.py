from seleniumbase import BaseCase


class HomePage(BaseCase):
    hero = '(//*[@id[contains(., "hero")]])//h1'
    home_title = 'The New York Public Library'

    h2_heading = '(//*[@id="content-primary"]//h2)'
    see_more = '(//a[contains(text(), "See More")])'

    section_spotlight = '//*[@id="content-primary"]//*[self::h2 and contains(., "Spotlight")]'
    section_whats_on = '//*[@id="content-primary"]//*[self::h2 and contains(., "What")]'
    section_discover = '//*[@id="content-primary"]//*[self::h2 and contains(., "Discover")]'
    section_staff_picks = '//*[@id="content-primary"]//*[self::h2 and contains(., "Staff Picks")]'
    section_in_collection = '//*[@id="content-primary"]//*[self::h2 and contains(., "In the Collection")]'
    section_blog = '//*[@id="content-primary"]//*[self::h2 and contains(., "Blog")]'
    section_explore = '//*[@id="content-primary"]//*[self::h2 and contains(., "Explore")]'

    slide_next = '//*[@id="slideshow-next-button"]'
    slide_prev = '//*[@id="slideshow-prev-button"]'
    new_noteworthy_slide = '//*[@id="content-primary"]//*[self::h2 and contains(., "In the Collection")]/../../..//li'

    all_links = '((//*[@id="mainContent"]//h3)//a)'  # locator for all links on the page

    def open_home_page(self):
        # self.open("https://www.nypl.org/")

        base_url = "https://www.nypl.org/"
        qa_base_url = "https://qa-www.nypl.org/"

        url = f"{base_url}"
        qa_url = f"{qa_base_url}"

        # Open the appropriate URL based on the environment
        if self.env == "qa":
            print(f"Running on QA Env: Opening : {qa_url}")
            self.open(qa_url)
        else:
            print(f"Running on Production Env: Opening : {url}")
            self.open(url)
