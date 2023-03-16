from examples.nypl_pages.page_schwarzman import SchwarzmanPage
from examples.nypl_utility.utility import NyplUtils

import requests
import urllib3
import pytest
from requests.exceptions import MissingSchema, InvalidSchema, InvalidURL
from selenium import webdriver
from selenium.webdriver.common.by import By


class Schwarzman(NyplUtils):

    # https://www.nypl.org/locations/schwarzman

    def setUp(self):
        super().setUp()
        print("=================================")
        print("\nRUNNING BEFORE EACH TEST")

        # open blog page
        self.open_schwarzman_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_schwarzman(self):
        # https://www.nypl.org/locations/schwarzman
        print("test_schwarzman()\n")

        # assert breadcrumbs and hero
        self.assert_element(SchwarzmanPage.home)
        self.assert_element(SchwarzmanPage.locations)
        self.assert_element(SchwarzmanPage.hero)

        # assert 'Visit' and 'Research' tabs
        self.assert_element(SchwarzmanPage.visit)
        self.assert_element(SchwarzmanPage.research)
        # asserting title
        self.assert_title("Stephen A. Schwarzman Building | The New York Public Library")

        # assert that clicking on 'directions' and '202x holiday hours' will open the correct pages
        # using 'link_assertion' method from utility.py
        self.link_assertion(SchwarzmanPage.directions, "google.com/maps")
        self.link_assertion(SchwarzmanPage.holiday_closings, "nypl.org/help/closings")
        self.link_assertion(SchwarzmanPage.research, "nypl.org/locations/schwarzman/research")
        self.link_assertion(SchwarzmanPage.learn_more_1, "nypl.org/locations/schwarzman/research")
        self.link_assertion(SchwarzmanPage.learn_more_2, "nypl.org/spotlight/treasures")
        self.link_assertion(SchwarzmanPage.daily_guided_tours, "nypl.org/events/tours/schwarzman")

        # next spotlight and featured h3 content don't change often, therefore, full endpoints being asserted
        self.link_assertion(SchwarzmanPage.in_the_spotlight_1, "nypl.org/appointments/schwarzman")
        self.link_assertion(SchwarzmanPage.in_the_spotlight_2, "databases")

        self.link_assertion(SchwarzmanPage.featured_at_sasb_1, "nypl.org/locations/schwarzman/research")
        self.link_assertion(SchwarzmanPage.featured_at_sasb_2, "nypl.org/about/locations/schwarzman/shop-cafe")
        self.link_assertion(SchwarzmanPage.featured_at_sasb_3, "www.nypl.org/blog")

        # Exhibitions assertions are for dynamic content, hence, only base URL '/events/exhibitions' used for assertion

        # write an addition to the utility. It will take the length of the list with
        # '//*[@id="block-nypl-emulsify-content"]/div/div/div[6]/div[1]/div/div/div[2]/ul/li'
        # and then use this in a loop with a range and loop over the below statements.

        self.link_assertion(SchwarzmanPage.current_exhibitions_1, "nypl.org/events/exhibitions")
        self.link_assertion(SchwarzmanPage.current_exhibitions_2, "nypl.org/events/exhibitions")
        self.link_assertion(SchwarzmanPage.current_exhibitions_3, "nypl.org/events/exhibitions")
        self.link_assertion(SchwarzmanPage.current_exhibitions_4, "nypl.org/events/exhibitions")

        # asserting 'Events - See All' web element
        self.assert_element(SchwarzmanPage.events_see_all)
        # asserting 'Events' with a for loop by clicking every event and asserting the title
        # getting the length of the events h3 to use it in the for loop
        h3_length = len(
            self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/div[6]/div[2]/div/div/ul/li'))
        # for loop to go over every event
        for x in range(1, h3_length + 1):
            # getting the link text and assert if it is in the page title
            h3_link_text = self.get_text(
                f'//*[@id="block-nypl-emulsify-content"]/div/div/div[6]/div[2]/div/div/ul/li[{x}]/div[2]/h3/a')
            print("\n1: " + h3_link_text)
            self.click(f'//*[@id="block-nypl-emulsify-content"]/div/div/div[6]/div[2]/div/div/ul/li[{x}]/div[2]/h3')

            # getting the page title element
            h1_title = self.get_text('//*[@id="page-title"]')
            print("2: " + h1_title)
            # asserting h3 link text to the page title
            self.assert_true(h3_link_text in h1_title)

            self.go_back()  # go to the previous page for the next loop

        # asserting 'About the Stephen A. ....'
        self.assert_true(self.get_text(SchwarzmanPage.about_the_sasb) == "About the Stephen A. Schwarzman Building")

    def test_sample21(self):

        self.open("https://the-internet.herokuapp.com/broken_images")

        self.image_assertion()

    def test_sample_links(self):

        # current exhibition list length to use in the for loop, this is dynamic, range from 1-4
        link_amount = len(self.find_elements(self.current_exhibitions_list))

        # current exhibition links to be asserted, depending on the link_amount above
        link_elements = [SchwarzmanPage.current_exhibitions_1, SchwarzmanPage.current_exhibitions_2,
                         SchwarzmanPage.current_exhibitions_3, SchwarzmanPage.current_exhibitions_4]

        print(link_amount)  # optional print of the exhibition amount

        for i in range(link_amount):
            link = link_elements[i]
            self.link_assertion(link, "nypl.org/events/exhibitions")
