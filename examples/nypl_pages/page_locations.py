from seleniumbase import BaseCase


class LocationsPage(BaseCase):
    home = '(//*[contains(text(), "Home")])[1]'
    locations = '(//*[contains(text(), "Locations")])[2]'  # breadcrumb, not the top header navigation one.
    homepage_link = 'https://www.nypl.org/locations'

    search_bar = '//*[@id="search-form__search-input"]'
    search_button = '//*[@id="search-form__submit"]'
    first_result = '(//*[@id="locations-list"]//h2)[1]'

    open_now_check_box = '//*[@id="checkbox-open-now"]'
    clear_all_search = '(//*[contains(text(), "Clear all search terms")])'

    filter_length = '//*[@id="locations-list"]//li'  # this locator is true for all sub-filters
    library_info = '(//*[@id="locations-list"]//li)'  # library info on the /locations page
    location_info = '//*[@id="block-entityviewcontent"]'  # library info on the library's individual page
    library_link = '((//*[@id="locations-list"]//li)//h2//a)'  # retrieves the h2 for Library names

    all_libraries = '//*[@id="locations-list"]//li'
    open_libraries = '//*[@id="locations-list"]//li'
    iframe = '//*[@id="locations-gmap"]//iframe'

    borough = '//*[@id="search-form"]/div[2]/div[2]/div[1]/div/div[1]/div/label'
    apply_boro = '//*[@id="button-save-filter-borough"]'
    clear_boro = '//*[@id="button-clear-filter-borough"]'
    bronx = '//*[@id="12060965-2125-4cf9-a724-b3560fdc3af6-wrapper"]/label/span[1]'
    bronx_location = '//*[@id="locations-list"]/div[2]/ul/li[1]/div/div[1]'
    manhattan = '//*[@id="a9405ac3-6d14-4e2b-b8fa-bede59d231b5-wrapper"]/label/span[1]'
    manhattan_location = '//*[@id="locations-list"]/div[2]/ul/li[1]/div/div[1]'
    richmond = '//*[@id="ecf1cc55-5591-45cc-adf1-6f72aa54f2ce-wrapper"]/label/span[1]'
    richmond_location = '//*[@id="locations-list"]/div[2]/ul/li[1]/div/div[1]'

    # random libraries for 3 boroughs
    random_bronx_library = "(//*[contains(@class, 'address')])[' + str(randrange(1, 35)) + ']"
    random_manhattan_library = "(//*[contains(@class, 'address')])[' + str(randrange(1, 76)) + ']"
    random_staten_library = "(//*[contains(@class, 'address')])[' + str(randrange(1, 14)) + ']"

    # accessibility filters locator
    accessibility_filter = '(//*[@id="locations-list"])//li'
    non_accessible_links = '(//*[@id="locations-list"]//li//h2//a)'

    accessibility = '//*[@id="search-form"]/div[2]/div[2]/div[1]/div/div[2]/div/label'
    apply_access = '//*[@id="button-save-filter-accessibility"]'
    clear_access = '//*[@id="button-clear-filter-accessibility"]'
    full_access = '//*[@id="search-form"]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/ul/li[1]/div'
    partial_access = '//*[@id="search-form"]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/ul/li[2]/div'
    not_access = '//*[@id="search-form"]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/ul/li[3]/div'

    amenities_filters = "(//*[contains(text(), 'Amenities')])[1]/..//..//li"
    apply_amenities = '//*[@id="button-save-fa817186-d735-4a05-8b72-388d3b6c7a14"]'
    clear_amenities = '//*[@id="button-clear-fa817186-d735-4a05-8b72-388d3b6c7a14"]'

    subject_specialties = '//*[@id="search-form"]/div[2]/div[2]/div[2]/div/div[1]/div/label'
    apply_specialties = '//*[@id="button-save-9597730e-da47-4a4e-9f2d-5a4fc7b7fd41"]'
    clear_specialties = '//*[@id="button-clear-9597730e-da47-4a4e-9f2d-5a4fc7b7fd41"]'
    art = '//*[@id="f4385e15-89de-46df-a698-772ff33d2e2b-wrapper"]/label/span[1]'
    history = '//*[@id="3b37bfde-ca35-4b83-a509-ee1a2d6594bf-wrapper"]/label/span[2]'
    social_sciences = '//*[@id="e99fad48-255b-4b5c-b557-dabfadb68aa2-wrapper"]/label/span[2]'

    media_types_filters = "(//*[contains(text(), 'Media Types')])[1]/..//..//li"
    apply_media = '//*[@id="button-save-4805f571-ec30-4901-912e-e88b41fb158e"]'
    clear_media = '//*[@id="button-clear-4805f571-ec30-4901-912e-e88b41fb158e"]'
    archives = '//*[@id="search-form"]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]/ul/li[1]/div'

    bottom_promo_1 = '(//*[@id="promo-left-section-title"]/following-sibling::*//a)[1]'  # SASB link
    bottom_promo_2 = '(//*[@id="promo-left-section-title"]/following-sibling::*//a)[2]'  # SNFL link
    bottom_promo_3 = '(//*[@id="promo-right-section-title"]/following-sibling::*//a)[1]'  # Brooklyn Lib. link
    bottom_promo_4 = '(//*[@id="promo-right-section-title"]/following-sibling::*//a)[2]'  # Queens Lib. link

    def open_locations_page(self, category=''):
        # self.open("https://www.nypl.org/locations")

        # Determine the base URLs
        base_url = "https://www.nypl.org/locations/"
        qa_base_url = "https://qa-www.nypl.org/locations/"

        url = f"{base_url}{category}"
        qa_url = f"{qa_base_url}{category}"

        # Open the appropriate URL based on the environment
        if self.env == "qa":
            print(f"Running on QA Env: Opening {category} page with URL: {qa_url}")
            self.open(qa_url)
        else:
            print(f"Running on Production Env: Opening {category} page with URL: {url}")
            self.open(url)
