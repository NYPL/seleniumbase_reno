from seleniumbase import BaseCase


class OnlineResourcesPage(BaseCase):
    home = '//*[@id="__next"]/div/div[2]/nav/ol/li[1]/a/span'
    research = '//*[@id="__next"]/div/div[2]/nav/ol/li[2]/a/span'
    collections = '//*[@id="__next"]/div/div[2]/nav/ol/li[3]/a/span'
    articles_databases = '//*[@id="__next"]/div/div[2]/nav/ol/li[4]'
    h1_heading = '//*[@id="main-content"]/div[1]/div[1]/div/h1'
    h1_paragraph = '//*[@id="main-content"]/div[1]/div[1]/div/p'

    apply_subject = '//*[@id="multiselect-button-save-subject"]'
    clear_subject = '//*[@id="multiselect-button-clear-subject"]'

    search_text = '//*[@id="search-form__search-input-label"]'
    search_bar = '//*[@id="search-form__search-input"]'
    search_button = '//*[@id="search-form__submit"]'
    search_results = '//*[@id="search-results-details__heading"]'
    search_tab = '//*[@id="__next"]/div/div[2]/nav/ol/li[5]/span/span'
    clear_search = '//*[@id="search-results-details__button"]'

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
    a_z_database = '//*[@id="A-Z Articles & Databases"]'

    more_research = '//*[@id="more-research-tools"]'

    def open_online_resources_page(self):
        # self.open("https://www.nypl.org/research/collections/articles-databases")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/research/collections/articles-databases")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/research/collections/articles-databases")
