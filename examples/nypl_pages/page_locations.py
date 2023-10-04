from seleniumbase import BaseCase


class LocationsPage(BaseCase):
    home = '(//*[contains(text(), "Home")])[1]'
    locations = '(//*[contains(text(), "Locations")])[1]'

    welcome_text = '//*[@id="main-content"]/div[1]/div[1]/div/div[2]'
    find_your_library = '//*[@id="location-finder__title"]'
    search_text = '//*[@id="search-form__search-input-label"]'
    search_bar = '//*[@id="search-form__search-input"]'
    search = '//*[@id="search-form__submit"]'
    open_now = '//*[@id="search-form"]/div[2]/div[1]'
    open_now_check_box = '//*[@id="checkbox-open-now"]'
    filters = '//*[@id="search-filters-group1__heading"]'
    research_filters = '//*[@id="search-filters-group2__heading"]'
    clear_all_search = '//*[@id="location-finder-search-results-details__clear"]'
    clear_all_search_2 = '//*[@id="button-clear-filter-borough"]'

    filter_length = '//*[@id="locations-list"]//li'  # this locator is true for all sub-filters

    borough = '//*[@id="search-form"]/div[2]/div[2]/div[1]/div/div[1]/div/label'
    apply_boro = '//*[@id="button-save-filter-borough"]'
    clear_boro = '//*[@id="button-clear-filter-borough"]'
    bronx = '//*[@id="12060965-2125-4cf9-a724-b3560fdc3af6-wrapper"]/label/span[1]'
    bronx_location = '//*[@id="locations-list"]/div[2]/ul/li[1]/div/div[1]'
    manhattan = '//*[@id="a9405ac3-6d14-4e2b-b8fa-bede59d231b5-wrapper"]/label/span[1]'
    manhattan_location = '//*[@id="locations-list"]/div[2]/ul/li[1]/div/div[1]'
    richmond = '//*[@id="ecf1cc55-5591-45cc-adf1-6f72aa54f2ce-wrapper"]/label/span[1]'
    richmond_location = '//*[@id="locations-list"]/div[2]/ul/li[1]/div/div[1]'

    accessibility = '//*[@id="search-form"]/div[2]/div[2]/div[1]/div/div[2]/div/label'
    apply_access = '//*[@id="button-save-filter-accessibility"]'
    clear_access = '//*[@id="button-clear-filter-accessibility"]'
    full_access = '//*[@id="search-form"]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/ul/li[1]/div'
    partial_access = '//*[@id="search-form"]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/ul/li[2]/div'
    not_access = '//*[@id="search-form"]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/ul/li[3]/div'

    amenities = '//*[@id="search-form"]/div[2]/div[2]/div[1]/div/div[3]/div/label'
    apply_amenities = '//*[@id="button-save-fa817186-d735-4a05-8b72-388d3b6c7a14"]'
    clear_amenities = '//*[@id="button-clear-fa817186-d735-4a05-8b72-388d3b6c7a14"]'

    subject_specialties = '//*[@id="search-form"]/div[2]/div[2]/div[2]/div/div[1]/div/label'
    apply_specialties = '//*[@id="button-save-9597730e-da47-4a4e-9f2d-5a4fc7b7fd41"]'
    clear_specialties = '//*[@id="button-clear-9597730e-da47-4a4e-9f2d-5a4fc7b7fd41"]'
    art = '//*[@id="f4385e15-89de-46df-a698-772ff33d2e2b-wrapper"]/label/span[1]'
    history = '//*[@id="3b37bfde-ca35-4b83-a509-ee1a2d6594bf-wrapper"]/label/span[2]'
    social_sciences = '//*[@id="e99fad48-255b-4b5c-b557-dabfadb68aa2-wrapper"]/label/span[2]'

    media_types = '//*[@id="search-form"]/div[2]/div[2]/div[2]/div/div[2]/div/label/span'
    apply_media = '//*[@id="button-save-4805f571-ec30-4901-912e-e88b41fb158e"]'
    clear_media = '//*[@id="button-clear-4805f571-ec30-4901-912e-e88b41fb158e"]'
    archives = '//*[@id="search-form"]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]/ul/li[1]/div'

    bottom_1 = '/html/body/div[1]/div/div[2]/main/div[2]/div[2]/div[1]/div/div[1]/div/div[1]'
    bottom_2 = '/html/body/div[1]/div/div[2]/main/div[2]/div[2]/div[1]/div/div[1]/div/div[2]'
    bottom_3 = '//*[@id="main-content"]/div[2]/div[2]/div[1]/div/div[2]'

    def open_locations_page(self):
        # self.open("https://www.nypl.org/locations")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/locations")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/locations")

