from seleniumbase import BaseCase


class LocationsPage(BaseCase):
    home = '(//*[contains(text(), "Home")])[1]'
    locations = '(//*[contains(text(), "Locations")])[2]'  # breadcrumb, not the top header navigation one.
    locations_page_link = 'https://www.nypl.org/locations'

    search_bar = '//*[@id="search-form__search-input"]'
    search_button = '//*[@id="search-form__submit"]'
    first_result = '(//*[@id="locations-list"]//h2)[1]'

    open_now_check_box = '//*[@id="checkbox-open-now"]'
    clear_all_search = '(//*[contains(text(), "Clear all search terms")])'

    library_amount = '(//*[@id="locations-list"])//li'  # total library amount

    library_info = '(//*[@id="locations-list"]//li)'  # library info on the /locations page
    location_info = '//*[@id="block-entityviewcontent"]'  # library info on the library's individual page
    library_link = '((//*[@id="locations-list"]//li)//h2//a)'  # retrieves the h2 for Library names

    all_libraries = '//*[@id="locations-list"]//li'
    open_libraries = '//*[@id="locations-list"]//li'

    borough = '(//*[contains(text(), "Borough")])[1]'
    apply_boro = '(//*[contains(text(), "Apply Filters")])[1]'
    clear_boro = '(//*[contains(text(), "Clear")])[1]'
    bronx = '(//*[contains(text(), "Bronx")])[2]'
    manhattan = '(//*[contains(text(), "Manhattan")])[2]'
    richmond = '(//*[contains(text(), "Staten")])[2]'

    # random libraries for 3 boroughs
    random_bronx_library = "(//*[contains(@class, 'address')])[' + str(randrange(1, 35)) + ']"
    random_manhattan_library = "(//*[contains(@class, 'address')])[' + str(randrange(1, 76)) + ']"
    random_staten_library = "(//*[contains(@class, 'address')])[' + str(randrange(1, 14)) + ']"

    # accessibility filters locator
    library_h2_links = '(//*[@id="locations-list"]//li//h2//a)'  # library h2 URLs

    accessibility = '(//*[contains(text(), "Accessibility")])[1]'
    apply_access = '(//*[contains(text(), "Apply Filters")])[2]'
    full_access = '(//*[contains(text(), "Fully accessible")])[1]'
    partial_access = '(//*[contains(text(), "Partially accessible")])[1]'
    not_access = '(//*[contains(text(), "Not accessible")])[1]'

    amenities = '(//*[contains(text(), "Amenities")])[1]'
    amenities_filters = "(//*[contains(text(), 'Amenities')])[1]/..//..//li"

    subject_specialties = '(//*[contains(text(), "Subject Specialties")])[1]'
    apply_specialties = '(//*[contains(text(), "Apply Filters")])[4]'
    art = '(//*[contains(text(), "Art")])[1]'
    history = '//*[text()="History"]'
    social_sciences = '//*[text()="Social Sciences"]'

    media_types_filters = "(//*[contains(text(), 'Media Types')])[1]/..//..//li"

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
