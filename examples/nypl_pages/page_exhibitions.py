from seleniumbase import BaseCase


class ExhibitionsPage(BaseCase):
    # main page elements
    home = '//*[@id="block-nypl-emulsify-breadcrumbs"]/nav/ul/li[1]/a'
    events = '//*[@id="block-nypl-emulsify-breadcrumbs"]/nav/ul/li[2]/a'
    exhibitions_h1 = '//*[@id="block-nypl-emulsify-page-title"]/div/div/h1/span'
    main_paragraph = '//*[@id="block-nypl-emulsify-content"]/div/div/div[1]/div/p'
    current_exhibitions = '//*[@id="9-current-exhibitions"]'
    coming_soon = '//*[@id="45-coming-soon"]'
    coming_soon_content = '//*[@id="block-nypl-emulsify-content"]/div/div/div[3]/div[2]/div/div/div/ul/li/h3/a/span'
    community_showcase = '//*[@id="1150-community-showcases"]'
    online_exhibitions = '//*[@id="7132-online-exhibitions"]'
    past_exhibitions = '//*[@id="46-past-exhibitions"]'

    no_community_showcase = '/html/body/div[1]/div/main/div[2]/div/div/div/div/p'

    # /upcoming elements
    exhibitions = '//*[@id="block-nypl-emulsify-breadcrumbs"]/nav/ul/li[3]/a'
    upcoming_exhibitions_h1 = '//*[@id="block-pagetitle"]/div/div/h1'
    header_paragraph = '//*[@id="block-nypl-emulsify-content"]/div/div/header/p'
    right_icon = '//*[@id="block-nypl-emulsify-content"]/div/div/nav/ul/li[11]/a'
    ellipsis_2 = '//*[@id="block-nypl-emulsify-content"]/div/div/nav/ul/li[10]'

    # /past exhibitions
    past_exhibitions_h1 = '//*[@id="block-pagetitle"]/div/div/h1'
    archived_parag = '//*[@id="block-nypl-emulsify-content"]/div/div/div[1]/div/p'
    right_icon_2 = '//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/div[2]/div/div/nav/ul/li[8]/a'
    archived_h2 = '//*[@id="44-archived-exhibition-resources-a-to-z"]'

    # /archived-exhibition-resources
    right_icon_3 = '//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/div[2]/div/div/nav/ul/li[8]/a/span[2]'

    # /archived-exhibition-resources
    archived_h1 = '//*[@id="block-nypl-emulsify-page-title"]/div/div/h1/span'

    # /community-showcases
    community_h1 = '//*[@id="block-nypl-emulsify-page-title"]/div/div/h1/span'
    community_parag = '//*[@id="block-nypl-emulsify-content"]/div/div/div[1]/div/p'
    right_icon_4 = '//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/div/div/div/nav/ul/li[3]/a/span[2]'

    # /online
    online_h1 = '//*[@id="block-nypl-emulsify-page-title"]/div/div/h1/span'
    online_only_xpath = '//*[@id="block-nypl-emulsify-content"]/div/div/div/div/div/div/div/ul/li[1]/div/div[2]/div[1]/div'

    def open_exhibitions_page(self):
        # self.open("https://www.nypl.org/events/exhibitions")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/events/exhibitions")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/events/exhibitions")
