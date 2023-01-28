from seleniumbase import BaseCase


class LocationsPage(BaseCase):
    locations = '//*[@id="__next"]/div/div[2]/nav/ol/li[2]/span/span'
    welcome_text = '//*[@id="main-content"]/div[1]/div[1]/div/div[2]'
    find_your_library = '//*[@id="location-finder__title"]'
    search_text = '//*[@id="search-form__search-input-label"]'
    search = '//*[@id="search-form__submit"]'
    open_now = '//*[@id="search-form"]/div[2]/div[1]/label/span[2]'
    open_now_check_box = '//*[@id="checkbox-open-now"]'
    filters = '//*[@id="search-filters-group1__heading"]'
    research_filters = '//*[@id="search-filters-group2__heading"]'
    clear_all_search = '//*[@id="location-finder-search-results-details__clear"]'

    borough = '//*[@id="search-form"]/div[2]/div[2]/div[1]/div/div[1]/div/label'
    apply_boro = '//*[@id="button-save-filter-borough"]'
    clear_boro = '//*[@id="button-clear-filter-borough"]'
    bronx = '//*[@id="search-form"]/div[2]/div[2]/div[1]/div/div[1]/div/div/div[1]/ul/li[1]/div/label/span[2]'
    bronx_location = '//*[@id="locations-list"]/div[2]/ul/li[1]/div/div[1]'
    manhattan = '//*[@id="search-form"]/div[2]/div[2]/div[1]/div/div[1]/div/div/div[1]/ul/li[2]/div/label/span[2]'
    manhattan_location = '//*[@id="locations-list"]/div[2]/ul/li[1]/div/div[1]'
    richmond = '//*[@id="search-form"]/div[2]/div[2]/div[1]/div/div[1]/div/div/div[1]/ul/li[3]/div/label/span[2]'
    richmond_location = '//*[@id="locations-list"]/div[2]/ul/li[1]/div/div[1]'

    accessibility = '//*[@id="search-form"]/div[2]/div[2]/div[1]/div/div[2]/div/label'
    apply_access = '//*[@id="button-save-filter-accessibility"]'
    clear_access = '//*[@id="button-clear-filter-accessibility"]'
    full_access = '//*[@id="search-form"]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/ul/li[1]/div/label/span[2]'
    partial_access = '//*[@id="search-form"]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/ul/li[2]/div/label/span[2]'
    not_access = '//*[@id="search-form"]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/ul/li[3]/div/label/span[2]'

    amenities = '//*[@id="search-form"]/div[2]/div[2]/div[1]/div/div[3]/div/label'
    apply_amenities = '//*[@id="button-save-fa817186-d735-4a05-8b72-388d3b6c7a14"]'
    clear_amenities = '//*[@id="button-clear-fa817186-d735-4a05-8b72-388d3b6c7a14"]'

    subject_specialties = '//*[@id="search-form"]/div[2]/div[2]/div[2]/div/div[1]/div/label'
    apply_specialties = '//*[@id="button-save-9597730e-da47-4a4e-9f2d-5a4fc7b7fd41"]'
    clear_specialties = '//*[@id="button-clear-9597730e-da47-4a4e-9f2d-5a4fc7b7fd41"]'
    art = '//*[@id="search-form"]/div[2]/div[2]/div[2]/div/div[1]/div/div/div[1]/ul/li[1]/div/label/span[2]'
    history = '/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/form/div[2]/div[2]/div[2]/div/div[1]/div/div/div[1]/ul/li'
    social_sciences = '//*[@id="search-form"]/div[2]/div[2]/div[2]/div/div[1]/div/div/div[1]/ul/li[10]/div/label/span[2]'

    media_types = '//*[@id="search-form"]/div[2]/div[2]/div[2]/div/div[2]/div/label/span'
    apply_media = '//*[@id="button-save-4805f571-ec30-4901-912e-e88b41fb158e"]'
    clear_media = '//*[@id="button-clear-4805f571-ec30-4901-912e-e88b41fb158e"]'
    archives = '//*[@id="search-form"]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]/ul/li[1]/div/label/span[2]'

    def open_locations_page(self):
        # self.open("https://www.nypl.org/locations")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/locations")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/locations")

