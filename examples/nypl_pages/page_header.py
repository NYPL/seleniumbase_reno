from seleniumbase import BaseCase


class HeaderPage(BaseCase):
    lion_logo = '//*[contains(text(), "NYPL Header Logo")]'

    login_button = '//*[@id="loginButton"]'
    login_catalog = '//*[contains(text(), "Go To The Catalog")]'
    login_research_catalog = '//*[contains(text(), "Go To The Research Catalog")]'

    username = '//*[@id="code"]'
    password = '//*[@id="pin"]'
    submit = '//*[contains(@value, "Submit")]'

    catalog_searchbar = '//*[@aria-label="search"]'
    catalog_login = '//*[@id="user-login-button"]'
    catalog_logout = '//*[contains(text(), "Sign out")]'

    research_catalog_logout = '//*[contains(text(), "Log Out")]'
    research_catalog_searchbar = '//*[@id="searchbar-textinput-mainContent"]'
    h2_display_result = '//*[@id="mainContent"]//*[@data-testid="search-results-heading"]'

    my_bookshelf = '//*[@id="bookshelf-title"]'
    my_account_research_catalog = '//*[@id="my-account-profile-header-heading"]'

    locations = '//*[@id="header-nav-upper"]/li//a[contains(text(), "Locations")]'
    get_a_library_card = '//*[@id="header-nav-upper"]/li//a[contains(text(), "Get A Library Card")]'
    get_email_updates = '//*[@id="header-nav-upper"]/li//a[contains(text(), "Get Email Updates")]'
    donate = '//*[@id="nypl-header"]//*[contains(text(), "Donate")]'
    shop = '//*[@id="header-nav-upper"]/li//a[contains(text(), "Shop")]'

    books_music_movies = '//*[contains(text(), "Books/Music/Movies")]'
    research = '(//*[contains(text(), "Research")])[1]'
    education = '//*[contains(text(), "Education")]'
    events = '(//*[contains(text(), "Events")])[1]'
    connect = '(//*[contains(text(), "Connect")])[1]'
    give = '(//*[contains(text(), "Give")])[1]'
    get_help = '(//*[contains(text(), "Get Help")])[1]'
    search_button = '(//*[contains(text(), "Search")])[1]'

    search_tab = '//*[@id="__next"]//*[contains(text(), "Search")]'
    subject_heading_explorer_tab = '//*[@id="__next"]//*[contains(text(), "Subject Heading Explorer")]'
    my_account_tab = '(//*[@id="__next"]//*[contains(text(), "My Account")])[1]'
    log_out_tab = '(//*[@id="__next"]//*[contains(text(), "Log Out")])'

    checkouts_tab = '(//*[@id="__next"]//*[contains(text(), "Checkouts")])'
    requests_tab = '(//*[@id="__next"]//*[contains(text(), "Requests")])'
    account_settings_tab = '(//*[@id="__next"]//*[contains(text(), "Account settings")])'

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