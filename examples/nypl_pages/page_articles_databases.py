from seleniumbase import BaseCase


class ArticlesDatabasesPage(BaseCase):
    home = '(//*[contains(text(), "Home")])[1]'
    research = '(//*[contains(text(), "Research")])[2]'
    collections = '(//*[contains(text(), "Collections")])[1]'
    articles_databases = '(//*[contains(text(), "Articles & Databases")])[2]'
    h1_heading = '(//*[contains(text(), "Articles & Databases")])[3]'
    h1_paragraph = '(//*[contains(text(), "Articles & Databases")])[3]/..//p'

    articles_databases_title = "Articles & Databases | The New York Public Library"

    apply_subject = '//*[@id="multiselect-button-save-subject"]'
    clear_subject = '//*[@id="multiselect-button-clear-subject"]'

    search_bar = '//*[@id="search-form__search-input"]'
    submit_button = '//*[@id="search-form__submit"]'
    first_result_h3 = '(//*[@id="search-results"]//h3)[1]'
    clear_search = '//*[@id="search-results-details__button"]'

    search_result = '//*[@id="search-results-details"]'

    subjects_button = '//*[@id="multiselect-subject"]'

    audience_button = '//*[@id="multiselect-audience_by_age"]'
    apply_audience = '//*[@id="multiselect-button-save-audience_by_age"]'
    clear_audience = '//*[@id="multiselect-button-clear-audience_by_age"]'

    availability_button = '//*[@id="multiselect-availability"]'
    clear_availability = '//*[@id="multiselect-button-clear-availability"]'
    apply_availability = '//*[@id="multiselect-button-save-availability"]'

    featured_resources = '//*[@id="featured-resources"]'
    featured_resources_list = '//*[contains(text(), "Featured Resources")]//..//li'
    most_popular_list = '//*[contains(text(), "Most Popular")]//..//li'
    most_popular = '//*[@id="most-popular"]'
    a_z_database = '//*[@id="alphabet-filter-id-wrapper"]//h2'
    alphabet_pagination = '//*[@id="alphabet-filter-id-wrapper"]//button'

    more_research = '//*[@id="more-research-tools"]'

    def open_articles_databases_page(self):

        qa = 'https://qa-www.nypl.org/research/collections/articles-databases'
        prod = 'https://www.nypl.org/research/collections/articles-databases'

        if self.env == "qa":
            print("Running on QA Env")
            self.open(qa)
        else:
            print("Running on Production Env")
            self.open(prod)
