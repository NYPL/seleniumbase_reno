from seleniumbase import BaseCase


class ArticlesDatabasesPage(BaseCase):
    home = '(//*[contains(text(), "Home")])[1]'
    research = '(//*[contains(text(), "Research")])[2]'
    collections = '(//*[contains(text(), "Collections")])[1]'
    articles_databases = '(//*[contains(text(), "Articles & Databases")])[2]'
    h1_heading = '//*[@id="main-content"]/div[1]/div[1]/div/h1'
    h1_paragraph = '//*[@id="main-content"]/div[1]/div[1]/div/p'

    articles_databases_title = "Articles & Databases | The New York Public Library"

    apply_subject = '//*[@id="multiselect-button-save-subject"]'
    clear_subject = '//*[@id="multiselect-button-clear-subject"]'

    search_bar = '//*[@id="search-form__search-input"]'
    submit_button = '//*[@id="search-form__submit"]'
    first_result_h3 = '//*[@id="search-results"]/div//div//div//h3'
    clear_search = '//*[@id="search-results-details__button"]'

    search_text = '//*[@id="search-form__search-input-label"]'
    search_button = '//*[@id="search-form__submit"]'
    search_results = '//*[@id="search-results-details__heading"]'
    search_result = '//*[@id="search-results-details"]'
    search_tab = '//*[@id="__next"]/div/div[2]/nav/ol/li[5]/span/span'

    h2_filter_by = '//*[@id="search-filters--heading"]'
    subjects_button = '//*[@id="multiselect-subject"]'

    audience_button = '//*[@id="multiselect-audience_by_age"]'
    adults = '//*[@id="multiselect-audience_by_age"]/div/ul/li[1]/label/span[2]'
    kids = '//*[@id="multiselect-audience_by_age"]/div/ul/li[2]/label/span[2]'
    teens = '//*[@id="multiselect-audience_by_age"]/div/ul/li[3]/label/span[2]'
    apply_audience = '//*[@id="multiselect-button-save-audience_by_age"]'
    clear_audience = '//*[@id="multiselect-button-clear-audience_by_age"]'

    availability_button = '//*[@id="multiselect-availability"]'
    available_everywhere = '//*[@id="multiselect-availability"]/div/ul/li[1]/label/span[2]'
    offsite_with = '//*[@id="multiselect-availability"]/div/ul/li[2]/label/span[2]'
    onsite_only = '//*[@id="multiselect-availability"]/div/ul/li[3]/label/span[2]'
    clear_availability = '//*[@id="multiselect-button-clear-availability"]'
    apply_availability = '//*[@id="multiselect-button-save-availability"]'

    featured_resources = '//*[@id="featured-resources"]'
    most_popular = '//*[@id="most-popular"]'
    a_z_database = '//*[@id="alphabet-filter-id-wrapper"]//h2'

    more_research = '//*[@id="more-research-tools"]'

    def open_articles_databases_page(self):
        # self.open("https://www.nypl.org/research/collections/articles-databases")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/research/collections/articles-databases")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/research/collections/articles-databases")
