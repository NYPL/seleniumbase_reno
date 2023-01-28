from seleniumbase import BaseCase


class BookListsPage(BaseCase):
    home = '//*[@id="block-nypl-emulsify-breadcrumbs"]/nav/ul/li[1]/a'
    books_and_more = '//*[@id="block-nypl-emulsify-breadcrumbs"]/nav/ul/li[2]/a'
    recommendations = '//*[@id="block-nypl-emulsify-breadcrumbs"]/nav/ul/li[3]/a'

    hero_header_h1 = '//*[@id="block-views-block-search-book-list-header-block-default"]/div/div/div/div/div[2]/h1'

    adults = '//*[@id="audience-navigation--"]/li[1]/a'
    teens = '//*[@id="audience-navigation--"]/li[2]/a'
    kids = '//*[@id="audience-navigation--"]/li[3]/a'

    h2_heading_year = '//*[@id="views-exposed-form-search-book-list-page-book-list-grid"]/div/h2'
    submit = '//*[@id="views-exposed-form-search-book-list-page-book-list-grid"]/div/div/button'
    selected_year = '//*[@id="year"]/option[1]'

    filter_results_below = "//*[@id='block-booklistsappealterms']//h3"
    additional_info = '//*[@id="block-nypl-emulsify-content"]/div/div/footer/div/div/div/div/h3'
    learn_more = '//*[@id="block-nypl-emulsify-content"]/div/div/footer/div/div/div/div/p/a'
    explore_this_year = '//*[@id="block-nypl-emulsify-content"]/div/div/footer/div/div/div/div/p[1]'
    about_best_books = ''

    def open_book_lists_page(self):
        # self.open("https://www.nypl.org/books-more/recommendations/125/adults")

        # https://www.nypl.org/books-more/recommendations/125/adults
        # https://www.nypl.org/books-more/recommendations/best-books/adults
        # https://www.nypl.org/books-more/recommendations/staff-picks/adults

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/books-more/recommendations/125/adults")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/books-more/recommendations/125/adults")
