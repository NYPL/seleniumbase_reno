from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_locations import LocationsPage

import pytest
from random import randrange
import time


class Locations(NyplUtils):
    # https://www.nypl.org/locations

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open locations page
        self.open_locations_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_locations_main_page_elements(self):
        print("test_main_page_elements()\n")

        # asserting the images on the page
        self.image_assertion()

        # assert breadcrumbs and page elements
        self.assert_element(LocationsPage.home)
        self.assert_element(LocationsPage.locations)
        self.assert_element(LocationsPage.welcome_text)
        self.assert_element(LocationsPage.find_your_library)
        self.assert_element(LocationsPage.search_text)
        self.assert_element(LocationsPage.search)
        self.assert_element(LocationsPage.open_now_check_box)
        self.assert_element(LocationsPage.filters)
        self.assert_element(LocationsPage.research_filters)

        # asserting 'Clear all search terms' Web-element
        self.click(LocationsPage.borough)
        self.click(LocationsPage.bronx)
        self.click(LocationsPage.apply_boro)
        self.click(LocationsPage.borough)
        self.click(LocationsPage.clear_boro)

        # assert if the 'Open now' check box works by...
        # ...comparing the total number of libraries vs open libraries
        total_library_number = len(self.find_elements(LocationsPage.all_libraries))
        self.click(LocationsPage.open_now_check_box)
        self.wait(1)
        open_library_number = len(self.find_elements(LocationsPage.open_libraries))

        print("total library number = " + str(total_library_number),
              "open library number = " + str(open_library_number))
        self.assert_true(total_library_number > open_library_number)

        # clear all search terms
        self.click(LocationsPage.clear_all_search)
        # self.check_if_unchecked(LocationsPage.open_now_check_box)  # throws ElementClickInterceptedException
        self.assert_true(total_library_number > open_library_number)

        # map iframe, switch to iframe
        self.switch_to_frame(LocationsPage.iframe)  # iframe xpath may be dynamic
        self.switch_to_default_content()

        # lower page elements
        # asserting 3 bottom elements. 2 midtown locations assertion and BK and Queens web-elements.
        self.assert_element(LocationsPage.bottom_promo_1)  # Stephen A. Schwarzman Building link
        self.assert_element(LocationsPage.bottom_promo_2)  # Stavros Niarchos Foundation Library (SNFL) link
        self.assert_element(LocationsPage.bottom_promo_3)  # Brooklyn Public Library link
        self.assert_element(LocationsPage.bottom_promo_4)  # Queens Public Library link

    def test_locations_search_functionality(self):
        print("test_locations_search_functionalities()\n")

        # TODO update this test after below (RENO-3468) ticket is fixed - IN PROGRESS
        # https://jira.nypl.org/browse/RENO-3468

        # asserting the search functionality, if it returns related data
        self.send_keys(LocationsPage.search_bar, "Performing arts")
        self.click(LocationsPage.search)

        # text of first result
        search_result_text = self.get_text(LocationsPage.first_result)
        # print(search_result_text)  # optional print

        expected_text = "The New York Public Library for the Performing Arts"

        # assertion
        self.assert_true(expected_text in search_result_text,
                         'Expected result = "' + expected_text + '" vs Actual result = "' + search_result_text + '"')

    def test_borough(self):
        print("test_borough()\n")

        # assert 'Borough' Filter web element
        self.assert_element(LocationsPage.borough)

        # assert 'Bronx' text from a random(randrange(1, 35)) Bronx location
        self.click(LocationsPage.borough)
        self.click(LocationsPage.bronx)
        self.click(LocationsPage.apply_boro)
        print(self.get_text('//*[@id="locations-list"]/div[2]/ul/li[' + str(randrange(1, 35)) + ']/div/div[1]'))
        self.assert_true("Bronx" in self.get_text(LocationsPage.bronx_location))
        self.click(LocationsPage.borough)
        self.click(LocationsPage.clear_boro)

        # assert 'Manhattan' text from a random(randrange(1, 76)) Manhattan location
        self.click(LocationsPage.borough)
        self.click(LocationsPage.manhattan)
        self.click(LocationsPage.apply_boro)
        print(self.get_text('//*[@id="locations-list"]/div[2]/ul/li[' + str(randrange(1, 76)) + ']/div/div[1]'))
        self.assert_true("New York" in self.get_text(LocationsPage.manhattan_location))
        self.click(LocationsPage.borough)
        self.click(LocationsPage.clear_boro)

        # assert 'Staten Island' text from a random(randrange(1, 14)) 'Staten Island' location
        self.click(LocationsPage.borough)
        self.click(LocationsPage.richmond)
        self.click(LocationsPage.apply_boro)
        print(self.get_text('//*[@id="locations-list"]/div[2]/ul/li[' + str(randrange(1, 14)) + ']/div/div[1]'))
        self.assert_true("Staten" in self.get_text(LocationsPage.richmond_location))
        self.click(LocationsPage.borough)
        self.click(LocationsPage.clear_boro)

    def test_accessibility_full(self):
        print("test_accessibility_full()\n")

        # assert  'Accessibility' filter
        self.click(LocationsPage.accessibility)  # click 'Accessible' filter web element
        self.click(LocationsPage.full_access)  # click full accessibility sub-filter
        self.click(LocationsPage.apply_access)  # apply filters
        time.sleep(2)

        # total number of libraries with full accessibility
        total_lib = len(self.find_elements('//*[@id="locations-list"]/div[2]/ul/li'))
        print(str(total_lib) + " libraries with Full Accessibility")

        count = 0  # counter for the libraries that don't have full accessibility
        for x in range(1, total_lib + 1):
            text = self.get_text(f'//*[@id="locations-list"]/div[2]/ul/li[{x}]')
            if 'Fully Accessible' in text:
                continue
            else:
                print(str(x) + "- " + self.get_text(f'(//*[@id="locations-list"]/div[2]/ul/li//h2//a)[{x}]'))
                # print(text)
                count += 1

        if count >= 1:
            print("\nAbove " + str(
                count) + " libraries don't have full access yet listed on the 'Fully Accessible' filter")
        self.assert_(count < 1)

    def test_accessibility_partial(self):
        print("test_partial_accessibility()\n")

        # assert 'partial access'
        self.click(LocationsPage.accessibility)  # click 'accessibility' filter
        self.click(LocationsPage.partial_access)  # click 'partial access' sub-filter
        self.click(LocationsPage.apply_access)  # click 'apply'
        time.sleep(1)

        # total number of libraries with partial accessibility
        total_partial_lib = len(self.find_elements('//*[@id="locations-list"]/div[2]/ul/li'))
        # print(str(total_partial_lib) + " total partial accessible libraries:\n")

        # for loop to assert locations have "partially accessible" text
        count = 0
        for x in range(1, total_partial_lib + 1):
            text = self.get_text('//*[@id="locations-list"]/div[2]/ul/li[' + str(x) + ']/div/div[3]/div[2]')
            # print(self.get_text(f'//*[@id="locations-list"]/div[2]/ul/li[{x}]/div/div[1]'))
            # print(text)
            self.assert_("Partially Accessible" in text)
            count += 1
            # print("===============")
        print(str(count) + " libraries with Partial Accessibility")

    # @pytest.mark.skip(reason="RENO-2961 needed to be fixed")
    def test_accessibility_non(self):
        print("test_not_accessible()\n")

        # TODO: update this after the bug fixed for the related 2 tickets below - DONE
        # https://jira.nypl.org/browse/RENO-2961
        # https://jira.nypl.org/browse/RENO-3673
        # above bugs fixed

        # assert 'not accessible' filter
        self.click(LocationsPage.accessibility)  # click 'accessibility'
        self.click(LocationsPage.not_access)  # click 'not accessible' filter
        self.click(LocationsPage.apply_access)  # click 'apply access'
        self.wait(2)

        # total libraries without accessibility
        total_no_access_lib = len(self.find_elements('//*[@id="locations-list"]/div[2]/ul/li'))
        print(str(total_no_access_lib) + " libraries with No Accessibility")

        # TODO: update below script after below ticket fixed - IN PROGRESS
        # https://jira.nypl.org/browse/RENO-3711
        # for loop to assert locations have "not accessible" text
        count = 0
        """"
        for x in range(1, total_no_access_lib + 1):
            # currently there is no 'not accessible' text beneath the listed locations, unlike partially and fully.
            # if in future it is added, update the below TODO, with the new locator
            text = self.get_text('//TODO: put locator here if there is a 'not accessible' text added ')
            print(text)
            self.assert_("Not Accessible" in text)
            count += 1
        print(str(count) + " libraries with No Accessibility")
        """

    def test_amenities(self):
        print("test_amenities()\n")

        # assert 'amenities' filter
        self.assert_(LocationsPage.amenities)

        # assert 'amenities' filter length, which is 42 as of June 2022
        amenities_len = len(self.find_elements("(//*[contains(text(), 'Amenities')])[1]/..//..//li"))
        print(amenities_len)  # optional print of the amenities length

        self.assert_true(amenities_len > 10, "amenities filter smaller than expected")

    def test_subject_specialties(self):
        print("test_subject_specialties()\n")

        # assert subject_specialties
        self.assert_(LocationsPage.subject_specialties)

        # assert 'art' filter number
        self.click(LocationsPage.subject_specialties)
        self.click(LocationsPage.art)
        self.click(LocationsPage.apply_specialties)

        # length of the filter == 10 as of June 2022
        art_filter_len = len(self.find_elements(LocationsPage.filter_length))
        print("art filter length: " + str(art_filter_len))

        # assert art filter length is larger than 8
        if art_filter_len == 0:
            print("if clause: filter is 0, will wait a few seconds")
            self.wait(3)
            art_filter_len = len(self.find_elements(LocationsPage.filter_length))
            self.assert_true(art_filter_len > 1)
            print(art_filter_len)
        else:
            print("else clause: filter was visible on first try without waits")
            self.assert_true(art_filter_len > 1)

        self.click(LocationsPage.subject_specialties)
        self.click(LocationsPage.clear_specialties)

        # ========================================================================================

        # assert history filter
        self.click(LocationsPage.subject_specialties)
        self.click(LocationsPage.history)
        self.click(LocationsPage.apply_specialties)

        history_filter_len = len(self.find_elements(LocationsPage.filter_length))
        print("\nhistory filter length: " + str(history_filter_len))

        # assert history filter length greater than 8, currently 11 as of June 2022
        if history_filter_len == 0:
            print("if clause: filter is 0, will wait a few seconds")
            self.wait(3)
            history_filter_len = len(self.find_elements(LocationsPage.filter_length))
            self.assert_true(history_filter_len > 1)
            print("history filter length: " + str(history_filter_len))
        else:
            print("else clause: filter was visible on first try without waits")
            self.assert_true(history_filter_len > 1)

        self.click(LocationsPage.subject_specialties)
        self.click(LocationsPage.clear_specialties)

        # ========================================================================================

        # assert social sciences filter
        self.click(LocationsPage.subject_specialties)
        self.assert_(LocationsPage.social_sciences)

        social_sciences_len = len(self.find_elements(LocationsPage.filter_length))
        print("\nsocial filter length: " + str(social_sciences_len))

        # assert social sciences filter length greater than 8, which is 10, as of June 2022
        if social_sciences_len == 0:
            print("if clause: filter is 0, will wait a few seconds")
            self.wait(3)
            social_sciences_len = len(self.find_elements(LocationsPage.filter_length))
            self.assert_true(social_sciences_len > 1)
            print("social filter length: " + str(social_sciences_len))
        else:
            print("else clause: filter was visible on first try without waits")
            self.assert_true(social_sciences_len > 1)

        self.click(LocationsPage.clear_specialties)

    def test_media_types(self):
        print("test_media_types()\n")

        # assert media types button
        self.assert_(LocationsPage.media_types)

        # assert 'Manuscripts and Archives Division' is listed after 'Archives' clicked
        self.click(LocationsPage.media_types)
        self.click(LocationsPage.archives)
        self.click(LocationsPage.apply_media)
        self.assert_element('//*[@id="lid-manuscripts-division"]/a')

        # assert 'media types' filter length, as of June 2022 it is 13
        self.click(LocationsPage.media_types)
        media_types_len = len(self.find_elements('//*[@id="search-form"]/div[2]/div[2]/div[2]/div/div[2]/div/div/div['
                                                 '1]/ul/li'))
        print("Media types length is " + str(media_types_len))
        self.assert_true(media_types_len > 10)
        self.click(LocationsPage.clear_media)

    @pytest.mark.skip(reason="1-Not priority, 2-wait for developer input on how to test")
    def test_open_hours(self):
        print("test_open_hours()\n")
        # TODO ask developer where/how to get the "open hours" of the library, e.g.

        """
        https://d8.nypl.org/node/41/edit?destination=/admin/content/locations

        "John: They are affected by closings entered here. Math is done to subtract closed hours from open hours.
        https://d8.nypl.org/admin/content/callout-manager

        I don't think it would be worth your while to parse it. I'd maybe check it using regular expressions
        just to check if there is something valid there. it should be either "CLOSED" or "* AM–* PM" (edited)"
        :return:
        """
