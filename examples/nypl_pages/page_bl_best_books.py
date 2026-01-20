from seleniumbase import BaseCase
import datetime


class BestBooksPage(BaseCase):
    home = '(//*[contains(text(), "Home")])[1]'
    books_and_more = '(//*[contains(text(), "Books & More")])[1]'
    recommendations = '(//*[contains(text(), "Recommendations")])[1]'

    all_links = '((//*[@class="basic-page-section"])//a)'  # locator for 'basic-page'

    h1_heading = '//*[@id="block-views-block-search-book-list-header-block-default"]//h1'

    adults_tab = '(//*[contains(text(), "Adults")])[2]'
    teens_tab = '(//*[contains(text(), "Teens")])[2]'
    kids_tab = '(//*[contains(text(), "Kids")])[2]'

    h2_heading_best_books = '(//*[contains(text(), "Best Books for")])[2]'
    submit = '(//*[contains(text(), "Submit")])[1]'
    selected_year = '//*[@id="year"]/option[@selected=""]'

    clear_all_filters = '(//*[contains(text(), "Clear All Filters")])[1]'
    filter_results_below = '(//*[contains(text(), "Filter Results Below")])[1]'
    left_side_filter = '//*[@id="block-booklistsappealterms"]'
    additional_info_h3 = '(//*[contains(text(), "Additional Info")])[1]'
    additional_info_links = '(//*[contains(text(), "Additional Information")]//..//a)'
    filter_results = '//*[contains(text(), "Filtered by")]'
    book_results = '(//*[@id="block-nypl-emulsify-content"]//h3)[1]'

    error_locator = '//*[@aria-label="Error message"]'

    def open_best_books_page(self, category='adults'):
        # Determine the base URLs
        base_url = "https://www.nypl.org/books-more/recommendations/best-books/"
        qa_base_url = "https://qa-www.nypl.org/books-more/recommendations/best-books/"

        # Get the current date
        current_date = datetime.datetime.now()
        # Define the date to switch the URL
        switch_date = datetime.datetime(2024, 1, 1)
        # todo: delete the above datetime lines by 2024 Jan- or update the function for 2025

        # Construct URL based on the category and the current date
        if current_date < switch_date:
            url = f"{base_url}{category}?year=2022"
            qa_url = f"{qa_base_url}{category}?year=2022"
        else:
            url = f"{base_url}{category}"
            qa_url = f"{qa_base_url}{category}"

        # Open the appropriate URL based on the environment
        if self.env == "qa":
            print(f"Running on QA Env: Opening {category} page with URL: {qa_url}\n")
            self.open(qa_url)
        else:
            print(f"Running on Production Env: Opening {category} page with URL: {url}\n")
            self.open(url)
