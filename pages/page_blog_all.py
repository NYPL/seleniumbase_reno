from seleniumbase import BaseCase


class BlogAllPage(BaseCase):
    all_links = '((//*[@id="page-container--content-primary"]//li)//a)'  # locator for 'page-container'

    explore_by = '//*[@id="search-filters--heading"]'
    filter_results = '//*[@id="search-results-details"]'

    # clear_all_search_terms = '//*[@id="search-results-details__button"]'

    sub_filters = '//*[@id="blogs__filter-bar"]//li'

    channels = '//*[@id="multiselect-channel"]/button'
    apply_channel = '//*[@id="multiselect-button-save-channel"]'

    subjects = '//*[@id="multiselect-subject"]'
    apply_subject = '//*[@id="multiselect-button-save-subject"]'

    libraries = '//*[@id="multiselect-library"]'
    apply_library = '//*[@id="multiselect-button-save-library"]'

    divisions = '//*[@id="multiselect-division"]'
    apply_division = '//*[@id="multiselect-button-save-division"]'

    audience = '//*[@id="multiselect-audience_by_age"]'
    apply_audience = '//*[@id="multiselect-button-save-audience_by_age"]'

    adults = '//*[@id="multiselect-audience_by_age"]//*[text()="Adults"]'
    kids = '//*[@id="multiselect-audience_by_age"]//*[text()="Kids"]'
    teens = '//*[@id="multiselect-audience_by_age"]//*[text()="Teens"]'

    def open_blog_page_all(self):

        qa = "https://qa-www.nypl.org/blog/all"
        prod = "https://www.nypl.org/blog/all"

        if self.env == "qa":
            print("Running on QA Env")
            self.open(qa)

        else:
            print("Running on Production Env")
            self.open(prod)

