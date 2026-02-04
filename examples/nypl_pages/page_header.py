from seleniumbase import BaseCase


class HeaderPage(BaseCase):
    lion_logo = '//*[contains(text(), "NYPL Header Logo")]'

    # below locators are called from NYPL utility file
    login_button = '//*[@id="loginButton"]'
    # login_catalog = '//*[contains(text(), "Go To The Catalog")]'
    # login_research_catalog = '//*[contains(text(), "Go To The Research Catalog")]'

    username = '//*[@id="code"]'
    password = '//*[@id="pin"]'
    submit = '//*[contains(@value, "Submit")]'

    # search bar
    search_tab = '//*[@id="searchButton"]'
    search_bar = '//*[@id="searchInput"]'
    search_submit_button = '//*[@id="search-btn"]'

    circulating_catalog = '//*[@id="circulatingCatalogSearch-wrapper"]'
    research_catalog = '//*[@id="researchcatalogSearch-wrapper"]'
    website_search = '//*[@id="websiteSearch-wrapper"]'
    search_result_rc_1 = '//*[@id="search-results-list"]//a'  # Search the Research Catalog locator 1- anchor links
    search_result_rc_2 = '//*[@data-testid="search-results-heading"]'  # Search the Research Catalog locator 1- total
    search_result_slw_1 = '//*[@id="gs-results"]//a'  # search the library website locator 1- anchor links
    search_result_slw_2 = '//*[@id="search-results-summary"]'  # search the library website locator 2- total


    # catalog/vega
    catalog_searchbar = '//*[@id="input-search-value"]'
    catalog_login = '//*[@id="user-login-button"]'
    catalog_logout = '//*[@data-automation-id="sign-out-button"]'

    overview_tab = '//*[@aria-label="Overview"]'
    my_account_research_catalog = '//*[@id="my-account-profile-header-heading"]'

    # top navigation
    locations = '//*[@id="header-nav-upper"]/li//a[contains(text(), "Locations")]'
    get_a_library_card = '//*[@id="header-nav-upper"]/li//a[contains(text(), "Get A Library Card")]'
    get_email_updates = '//*[@id="header-nav-upper"]/li//a[contains(text(), "Get Email Updates")]'
    donate = '(//*[contains(text(), "Donate")])[1]'
    shop = '//*[@id="header-nav-upper"]/li//a[contains(text(), "Shop")]'

    # section fronts
    books_music_movies = '//*[@id="header-nav-lower"]//*[contains(text(), "Books/Music/Movies")][1]'
    research = '//*[@id="header-nav-lower"]//*[contains(text(), "Research")][1]'
    education = '//*[@id="header-nav-lower"]//*[contains(text(), "Education")][1]'
    events = '//*[@id="header-nav-lower"]//*[contains(text(), "Events")][1]'
    connect = '//*[@id="header-nav-lower"]//*[contains(text(), "Connect")][1]'
    give = '//*[@id="header-nav-lower"]//*[contains(text(), "Give")][1]'
    get_help = '//*[@id="header-nav-lower"]//*[contains(text(), "Get Help")][1]'
    search_button = '//*[@id="header-nav-lower"]//*[contains(text(), "Search")][1]'

    # header is using same page as page_home
    """
    def open_home_page(self):
        # self.open("https://www.nypl.org/")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/")
    """