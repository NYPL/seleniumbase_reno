from seleniumbase import BaseCase


class SnflPage(BaseCase):
    home = '//*[@id="block-nypl-emulsify-breadcrumbs"]/nav/ul/li[1]/a'
    locations = '//*[@id="block-nypl-emulsify-breadcrumbs"]/nav/ul/li[2]/a'

    visit = '//*[@id="audience-navigation--"]/li[1]/a'
    explore = '//*[@id="audience-navigation--"]/li[2]/a'
    read = '//*[@id="audience-navigation--"]/li[3]/a'

    directions = '//*[@id="block-entityviewcontent"]/div/div/div/a'
    holiday_closings = '//*[@id="block-entityviewcontent"]/div/div/div/div[5]/a'
    address = '//*[@id="location-info--455-fifth-avenue<br>new-york-ny-10016"]'
    give = '//*[@id="block-entityviewcontent"]/div/div/div/div[6]/a'
    social_media = '//*[@id="block-entityviewcontent"]/div/div/div/div[8]'

    learn_more_1 = '//*[@id="block-nypl-emulsify-content"]/div/div/div[1]/div/p[2]/a'
    learn_more_2 = '//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/div[2]/p/a'
    daily_guided_tours = '//*[@id="block-nypl-emulsify-content"]/div/div/div[3]/div[2]/p/a'

    in_the_spotlight_1 = "//*[contains(text(), 'In the Spotlight')]//parent::*//parent::*//following-sibling::ul//li[1]"
    in_the_spotlight_2 = "//*[contains(text(), 'In the Spotlight')]//parent::*//parent::*//following-sibling::ul//li[2]"
    in_the_spotlight_3 = "//*[contains(text(), 'In the Spotlight')]//parent::*//parent::*//following-sibling::ul//li[3]"
    in_the_spotlight_4 = "//*[contains(text(), 'In the Spotlight')]//parent::*//parent::*//following-sibling::ul//li[4]"
    in_the_spotlight_5 = "//*[contains(text(), 'In the Spotlight')]//parent::*//parent::*//following-sibling::ul//li[5]"

    kids_see_all = "//*[@id='block-nypl-emulsify-content']//*[contains(text(), 'For Kids')]/following-sibling::a[1]"
    teens_see_all = "//*[@id='block-nypl-emulsify-content']//*[contains(text(), 'For Teens')]/following-sibling::a[1]"
    adults_see_all = "//*[@id='block-nypl-emulsify-content']//*[contains(text(), 'For Adults')]/following-sibling::a[1]"

    remote_resources_1 = "//*[contains(text(), 'Remote Resources')]//parent::*//parent::*//following-sibling::ul//li[1]"
    remote_resources_2 = "//*[contains(text(), 'Remote Resources')]//parent::*//parent::*//following-sibling::ul//li[2]"
    remote_resources_3 = "//*[contains(text(), 'Remote Resources')]//parent::*//parent::*//following-sibling::ul//li[3]"
    remote_resources_4 = "//*[contains(text(), 'Remote Resources')]//parent::*//parent::*//following-sibling::ul//li[4]"

    about_the_snfl = "//*[contains(text(), 'About the Stavros')]"

    # "Explore" tab locators
    centers = '//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/div/div/ul/li'
    more_resources = '//*[@id="block-nypl-emulsify-content"]/div/div/div[3]/ul/li'

    # "Read" tab locators
    top_checkouts = '//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/ul/li'
    shelf_help = '//*[@id="block-nypl-emulsify-content"]/div/div/div[3]'

    def open_snfl_page(self):
        # self.open("https://www.nypl.org/locations/snfl")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/locations/snfl")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/locations/snfl")
