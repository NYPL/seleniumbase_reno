from seleniumbase import BaseCase


class SchwarzmanPage(BaseCase):
    home = '//*[@id="block-nypl-emulsify-breadcrumbs"]/nav/ul/li[1]/a'
    locations = '//*[@id="block-nypl-emulsify-breadcrumbs"]/nav/ul/li[2]/a'
    hero = '//*[@id="block-content-hero-header"]/div/div[2]/h1/span'

    visit = '//*[@id="audience-navigation--"]/li[1]/a'
    research = '//*[@id="audience-navigation--"]/li[2]/a'

    directions = '//*[@id="block-entityviewcontent"]/div/div/div/a'
    holiday_closings = '//*[@id="block-entityviewcontent"]/div/div/div/div[5]/a'
    address = '//*[@id="location-info--fifth-avenue-and-42nd-street<br>new-york-ny-10018"]'

    learn_more_1 = '//*[@id="block-nypl-emulsify-content"]/div/div/div[1]/div/p[2]/a'
    learn_more_2 = '//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/div[2]/p/a'
    daily_guided_tours = '//*[@id="block-nypl-emulsify-content"]/div/div/div[3]/div[2]/p/a'

    in_the_spotlight_1 = '//*[@id="block-nypl-emulsify-content"]/div/div/div[4]/ul/li[1]/div[1]/h3/a'
    in_the_spotlight_2 = '//*[@id="block-nypl-emulsify-content"]/div/div/div[4]/ul/li[2]/div[1]/h3/a'
    in_the_spotlight_3 = '//*[@id="block-nypl-emulsify-content"]/div/div/div[4]/ul/li[3]/div[1]/h3/a'
    in_the_spotlight_4 = '//*[@id="block-nypl-emulsify-content"]/div/div/div[4]/ul/li[4]/div[1]/h3/a'
    in_the_spotlight_5 = '//*[@id="block-nypl-emulsify-content"]/div/div/div[4]/ul/li[5]/div[1]/h3/a'

    featured_at_sasb_1 = '//*[@id="block-nypl-emulsify-content"]/div/div/div[5]/ul/li[1]/div[1]/h3/a'
    featured_at_sasb_2 = '//*[@id="block-nypl-emulsify-content"]/div/div/div[5]/ul/li[2]/div[1]/h3/a'
    featured_at_sasb_3 = '//*[@id="block-nypl-emulsify-content"]/div/div/div[5]/ul/li[3]/div[1]/h3/a'

    events_see_all = '//*[@id="block-nypl-emulsify-content"]/div/div/div[6]/div[2]/div/div/div/div/a'

    about_the_sasb = '//*[@id="block-nypl-emulsify-content"]/div/div/div[6]/div[3]/h2'

    research_main_paragraph = '//*[@id="block-nypl-emulsify-content"]/div/div/div[1]'
    explore_division_centers = '//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/div/div/ul/li'
    further_resources = '//*[@id="block-nypl-emulsify-content"]/div/div/div[3]/ul/li'
    more_nypl_resources = '//*[@id="block-nypl-emulsify-content"]/div/div/div[4]/ul/li'

    def open_schwarzman_page(self):
        # self.open("https://www.nypl.org/locations/schwarzman")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/locations/schwarzman")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/locations/schwarzman")
