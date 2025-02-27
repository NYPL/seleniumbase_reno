from seleniumbase import BaseCase
import datetime


class StaffPicksPage(BaseCase):
    home = '(//*[contains(text(), "Home")])[1]'
    books_and_more = '(//*[contains(text(), "Books & More")])[1]'
    recommendations = '(//*[contains(text(), "Recommendations")])[1]'

    adults_tab = '(//*[contains(text(), "Adults")])[2]'
    teens_tab = '(//*[contains(text(), "Teens")])[1]'
    kids_tab = '(//*[contains(text(), "Kids")])[1]'

    all_links = '((//*[@class="basic-page-section"])//a)'  # locator for 'basic-page'

    h2_heading_staff_picks_adults = '(//*[contains(text(), "Picks for")])[2]'
    h2_heading_staff_picks_teens = '(//*[contains(text(), "Picks for")])[2]'
    h2_heading_staff_picks_kids = '(//*[contains(text(), "Picks for")])[2]'
    # h2_heading_best_books = '(//*[contains(text(), "Best Books for")])[2]'
    submit = '(//*[contains(text(), "Submit")])[1]'
    # selected_year = '//*[@id="year"]/option[@selected=""]'
    season_dropdown = '//*[@id="season"]'
    error_locator = '//*[@aria-label="Error message"]'

    clear_all_filters = '(//*[contains(text(), "Clear All Filters")])[1]'
    left_side_filter = "(//*[contains(text(), 'Filter Results Below')]/following-sibling::nav//li//label/span)"
    filter_results = '//*[contains(text(), "Filtered by")]'
    h3_book_results = '(//*[@id="block-nypl-emulsify-content"]//h3)[1]'

    total_books_found = '//*[@id="block-nypl-emulsify-content"]//li'

    def open_staff_picks_page(self, category='adults'):
        # https://www.nypl.org/books-more/recommendations/staff-picks/adults
        # https://www.nypl.org/books-more/recommendations/staff-picks/teens
        # https://www.nypl.org/books-more/recommendations/staff-picks/kids

        # Determine the base URLs
        base_url = "https://www.nypl.org/books-more/recommendations/staff-picks/"
        qa_base_url = "https://qa-www.nypl.org/books-more/recommendations/staff-picks/"

        url = f"{base_url}{category}"
        qa_url = f"{qa_base_url}{category}"

        # Open the appropriate URL based on the environment
        if self.env == "qa":
            print(f"Running on QA Env: Opening {category} page with URL: {qa_url}")
            self.open(qa_url)
        else:
            print(f"Running on Production Env: Opening {category} page with URL: {url}")
            self.open(url)
