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
    h2_display_result = '//*[@id="results-description"]'

    my_bookshelf = '//*[@id="bookshelf-title"]'
    my_account_research_catalog = '//*[@id="2"]'

    locations = '//*[@id="header-nav-upper"]/li//a[contains(text(), "Locations")]'
    get_a_library_card = '//*[@id="header-nav-upper"]/li//a[contains(text(), "Get A Library Card")]'
    get_email_updates = '//*[@id="header-nav-upper"]/li//a[contains(text(), "Get Email Updates")]'
    donate = '(//*[contains(text(), "Donate")])[1]'
    shop = '//*[@id="header-nav-upper"]/li//a[contains(text(), "Shop")]'

    books_music_movies = '//*[contains(text(), "Books/Music/Movies")]'
    research = '(//*[contains(text(), "Research")])[1]'
    education = '//*[contains(text(), "Education")]'
    events = '(//*[contains(text(), "Events")])[1]'
    connect = '(//*[contains(text(), "Connect")])[1]'
    give = '(//*[contains(text(), "Give")])[1]'
    get_help = '(//*[contains(text(), "Get Help")])[1]'
    search = '(//*[contains(text(), "Search")])[1]'

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