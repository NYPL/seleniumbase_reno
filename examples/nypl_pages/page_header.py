from seleniumbase import BaseCase


class HeaderPage(BaseCase):
    lion_logo = '//*[contains(text(), "NYPL Header Logo")]'

    login_button = '//*[@id="loginButton"]'
    login_catalog = '//*[contains(text(), "Go To The Catalog")]'
    login_research_catalog = '//*[contains(text(), "Go To The Research Catalog")]'

    username = '//*[@id="code"]'
    password = '//*[@id="pin"]'
    submit = '//*[@id="fm1"]/div[3]/input'

    search_research_catalog = '//*[@id="searchbar-button-mainContent"]'
    catalog_search_bar = '//*[@aria-label="search"]'
    catalog_login = '//*[@id="user-login-button"]'
    catalog_logout = '//*[contains(text(), "Sign out")]'
    research_catalog_search_bar = '//*[@id="searchbar-textinput-mainContent"]'
    h2_display_result = '//*[@id="results-description"]'
    next_button = '//*[@id="SccContainer-content-primary"]/div[3]/nav/a'
    previous_button = '//*[@id="SccContainer-content-primary"]/div[3]/nav/a[1]'

    my_bookshelf = '//*[@id="bookshelf-title"]'
    logout = '//*[@id="Insert_2"]'
    login_back = '//*[@id="Insert_0"]'

    my_account_research_catalog = '//*[@id="2"]'
    advanced_search_research = '//*[@id="advanced-search-link-container"]/a'
    advanced_search_research_submit = '//*[@id="advancedSearchSubmit"]'
    submit_warning = '//*[@id="advancedSearchAside"]'

    locations = '//*[@id="header-nav-upper"]/li//a[contains(text(), "Locations")]'
    get_a_library_card = '//*[@id="header-nav-upper"]/li//a[contains(text(), "Get A Library Card")]'
    get_email_updates = '//*[@id="header-nav-upper"]/li//a[contains(text(), "Get Email Updates")]'
    get_email_updates_page_title = 'Subscription Center | The New York Public Library'
    donate = '//*[@id="header-nav-upper"]/li//a[contains(text(), "Donate")]'
    donate_page_title = 'Make Your Tax-Deductible Gift Today - New York Public Library'
    shop = '//*[@id="header-nav-upper"]/li//a[contains(text(), "Shop")]'
    shop_page_title = 'The New York Public Library Shop'

    books_music_movies = '//*[contains(text(), "Books/Music/Movies")]'
    books_music_movies_title = 'Books/Music/Movies | The New York Public Library'
    research = '(//*[contains(text(), "Research")])[1]'
    research_title = 'Research | The New York Public Library'
    education = '//*[contains(text(), "Education")]'
    education_title = 'Education | The New York Public Library'
    events = '(//*[contains(text(), "Events")])[1]'
    events_title = 'Events | The New York Public Library'
    connect = '(//*[contains(text(), "Connect")])[1]'
    connect_title = 'Connect | The New York Public Library'
    give = '(//*[contains(text(), "Give")])[1]'
    give_title = 'Give | The New York Public Library'
    get_help = '(//*[contains(text(), "Get Help")])[1]'
    get_help_title = 'Get Help | The New York Public Library'
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