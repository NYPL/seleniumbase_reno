from seleniumbase import BaseCase


class SchwarzmanPage(BaseCase):
    home = '(//*[contains(text(), "Home")])[1]'
    hero = '(//*[@id[contains(., "hero")]])//h1'

    visit = '(//*[contains(text(), "Research")])[2]//..//..//*[contains(text(), "Visit")][1]'
    research = '(//*[contains(text(), "Visit")][1]//..//..//*[contains(text(), "Research")])[1]'

    sidebar = '//*[@id="block-entityviewcontent"]'
    holiday_closings = '(//*[contains(text(), "Holiday Closings")])[1]'
    address = '//*[@id="location-info--fifth-avenue-and-42nd-street<br>new-york-ny-10018"]'

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
