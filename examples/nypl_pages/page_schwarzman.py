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

    in_the_spotlight = '(//*[contains(text(), "In the Spotlight")]/../../..//a)'

    featured_at_sasb = '(//*[contains(text(), "Featured at the ")]/../../..//a)'

    events_see_all = '((//*[contains(text(), "Events")])[2])/..//a'

    about_the_sasb = '(//*[contains(text(), "About the Stephen A.")])'

    explore_division_centers = '((//*[contains(text(), "Explore Divisions & Centers")])/../../..//h3)'
    further_resources = '((//*[contains(text(), "Further Resources")])/../../..//h3)'
    more_nypl_resources = '((//*[contains(text(), "More NYPL")])/../../..//h3)'

    def open_schwarzman_page(self):
        # self.open("https://www.nypl.org/locations/schwarzman")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/locations/schwarzman")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/locations/schwarzman")
