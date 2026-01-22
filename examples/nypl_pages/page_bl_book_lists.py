from seleniumbase import BaseCase


class BookListsPage(BaseCase):
    home = '(//*[contains(text(), "Home")])[1]'
    books_and_more = '(//*[contains(text(), "Books & More")])[1]'
    recommendations = '(//*[contains(text(), "Recommendations")])[1]'

    adults_tab_adults = '(//*[contains(text(), "Adults")])[2]'
    teens_tab_adults = '(//*[contains(text(), "Teens")])[1]'
    teens_tab_teens = '(//*[contains(text(), "Teens")])[2]'
    kids_tab_adults = '(//*[contains(text(), "Kids")])[1]'
    kids_tab_kids = '(//*[contains(text(), "Kids")])[2]'

    hero_125 = '(//*[contains(text(), "Books We Love")])[2]'
    submit = '(//*[contains(text(), "Submit")])[1]'

    clear_all_filters = '(//*[contains(text(), "Clear All Filters")])[1]'
    filter_results_below = '(//*[contains(text(), "Filter Results Below")])[1]'
    left_side_filter = '(//*[@id="block-booklistsappealterms"]//nav)[1]//a[@class="js-facets-link"]'
    additional_info = '(//*[contains(text(), "Additional Info")])[1]'
    filter_results = '//*[contains(text(), "Filtered by")]'

    error_locator = '//*[@aria-label="Error message"]'

    total_books_found = '//*[@id="block-nypl-emulsify-content"]//li'

    def open_book_lists_page(self, category='adults'):
        # self.open("https://www.nypl.org/books-more/recommendations/125/adults")

        base_url = "https://www.nypl.org/books-more/recommendations/125/"
        qa_base_url = "https://qa-www.nypl.org/books-more/recommendations/125/"

        # https://www.nypl.org/books-more/recommendations/125/adults
        # https://www.nypl.org/books-more/recommendations/125/teens
        # https://www.nypl.org/books-more/recommendations/125/kids

        url = f"{base_url}{category}"
        qa_url = f"{qa_base_url}{category}"

        # Open the appropriate URL based on the environment
        if self.env == "qa":
            print(f"Running on QA Env: Opening {category} page with URL: {qa_url}")
            self.open(qa_url)
        else:
            print(f"Running on Production Env: Opening {category} page with URL: {url}")
            self.open(url)
