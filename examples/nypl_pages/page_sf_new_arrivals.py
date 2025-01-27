from seleniumbase import BaseCase


class NewArrivalsPage(BaseCase):
    side_bar_bmm = '//a[contains(text(), "BOOKS/MUSIC/MOVIES")]'  # sidebar 'books/music/movies' arrow/link

    toggle_display = '//*[@class="toggleDisplay"]'  # toggle display item bar

    switch_display = '//*[@class="switch"]'  # toggle display item for 'new arrivals/on order'
    new_arrivals = '//*[@id="label-newArrivals"]'  # 'new arrivals' button
    on_order = '//*[@id="label-onOrder"]'  # 'on order' button

    switch_view = '//*[@class="switch viewType"]'  # switch type item for 'list/grid' views
    list_view = '//*[@id="label-list"]'  # switch type item for 'list/grid' views
    grid_view = '//*[@id="label-grid"]'  # switch type item for 'list/grid' views

    filter_button = '//*[@class="PillButton filterButton true"]'
    filter_book = '//*[@id="label-BOOK/TEXT"]'  # 'book' filter
    filter_adult = '//*[@id="label-Adult"]'  # 'adult' filter
    filter_english = '//*[@id="label-English"]'  # 'english' filter
    filter_fiction = '//*[@id="label-fiction"]'  # 'all fiction' filter
    button_apply = '//*[@class="PillButton apply"]'  # 'apply' button
    selected_filters = '//*[@class="selectedFilters"]'  # selected filters

    load_more_button = '//*[@id="page-button-list-number"]'  # 'Load More' button at the end of the page

    def open_new_arrivals_page(self, category=''):
        # Determine the base URLs
        base_url = "https://www.nypl.org/books-music-movies/new-arrivals"
        qa_base_url = "https://qa-www.nypl.org/books-music-movies/new-arrivals"

        url = f"{base_url}{category}"
        qa_url = f"{qa_base_url}{category}"

        # Open the appropriate URL based on the environment
        if self.env == "qa":
            print(f"Running on QA Env: Opening {category} page with URL: {qa_url}")
            self.open(qa_url)
        else:
            print(f"Running on Production Env: Opening {category} page with URL: {url}")
            self.open(url)
