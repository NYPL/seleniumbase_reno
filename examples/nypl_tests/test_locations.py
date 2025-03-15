from selenium.common import InvalidSessionIdException, NoSuchElementException

from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_locations import LocationsPage

import pytest
from random import randrange
import time
import requests
import re

from seleniumbase.common.exceptions import TextNotVisibleException, NoSuchElementException


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

    @pytest.mark.smoke
    def test_locations_main(self):
        # https://www.nypl.org/locations
        print("test_locations_main()\n")
        self.open_locations_page(category='')

        # asserting the images on the page
        self.image_assertion()

        # assert breadcrumbs
        self.assert_element(LocationsPage.home)
        self.assert_element(LocationsPage.locations)

        # assert all links on the page
        self.assert_links_valid(LocationsPage.all_links)

        # lower page elements
        # asserting 3 bottom elements. 2 midtown locations assertion and BK and Queens web-elements.
        self.assert_element(LocationsPage.bottom_promo_1)  # Stephen A. Schwarzman Building link
        self.assert_element(LocationsPage.bottom_promo_2)  # Stavros Niarchos Foundation Library (SNFL) link
        self.assert_element(LocationsPage.bottom_promo_3)  # Brooklyn Public Library link
        self.assert_element(LocationsPage.bottom_promo_4)  # Queens Public Library link

    @pytest.mark.smoke
    def test_locations_filters(self):

        # page elements
        self.assert_element(LocationsPage.search_button)
        self.assert_element(LocationsPage.open_now_check_box)

        # asserting 'Clear all search terms' Web-element
        self.click(LocationsPage.borough)
        self.click(LocationsPage.bronx)
        self.click(LocationsPage.apply_boro)
        self.click(LocationsPage.borough)
        self.click(LocationsPage.clear_boro)

        # assert if the 'Open now' check box works by...
        # ...comparing the total number of libraries >= open libraries
        total_library_number = len(self.find_elements(LocationsPage.all_libraries))
        self.click(LocationsPage.open_now_check_box)
        self.wait(1)
        open_library_number = len(self.find_elements(LocationsPage.open_libraries))

        print("total library number = " + str(total_library_number),
              "open library number = " + str(open_library_number))
        self.assert_true(total_library_number >= open_library_number)

        # clear all search terms
        self.click(LocationsPage.clear_all_search)
        # self.check_if_unchecked(LocationsPage.open_now_check_box)  # throws ElementClickInterceptedException
        self.assert_true(total_library_number >= open_library_number)

    @pytest.mark.smoke
    @pytest.mark.skip(reason="RENO-3468 needs to be fixed")
    def test_locations_search_functionality(self):
        print("test_locations_search_functionalities()\n")

        # asserting the search functionality by the data it returns
        self.send_keys(LocationsPage.search_bar, "Performing arts")
        self.click(LocationsPage.search_button)

        # text of first result
        search_result_text = self.get_text(LocationsPage.first_result)
        # print(search_result_text)  # optional print

        expected_text = "The New York Public Library for the Performing Arts"

        # assertion
        self.assert_true(expected_text in search_result_text,
                         'Expected result = "' + expected_text + '" vs Actual result = "' + search_result_text + '"')

    def test_locations_borough(self, wait_time=2):
        print("test_borough()\n")

        # assert 'Borough' Filter web element
        self.assert_element(LocationsPage.borough)

        # assert 'Bronx' text from a random(randrange(1, 35)) Bronx location
        self.click(LocationsPage.borough)
        self.click(LocationsPage.bronx)
        self.click(LocationsPage.apply_boro)
        try:
            bronx_library_info = self.get_text(LocationsPage.random_bronx_library)
        except Exception:
            print("Fetching the Bronx Library info failed on first attempt. Retrying...")
            self.wait(wait_time)
            bronx_library_info = self.get_text(LocationsPage.random_bronx_library)
        print(bronx_library_info)
        self.assert_true("Bronx" in bronx_library_info)
        self.click(LocationsPage.clear_all_search)

        # assert 'Manhattan' text from a random(randrange(1, 76)) Manhattan location
        print("\n===========================")
        self.click(LocationsPage.borough)
        self.click(LocationsPage.manhattan)
        self.click(LocationsPage.apply_boro)
        try:
            manhattan_library_info = self.get_text(LocationsPage.random_manhattan_library)
        except Exception:
            print("Fetching the Manhattan Library info failed on first attempt. Retrying...")
            self.wait(wait_time)
            manhattan_library_info = self.get_text(LocationsPage.random_manhattan_library)
        print(manhattan_library_info)
        self.assert_true("New York" in manhattan_library_info)
        self.click(LocationsPage.clear_all_search)

        # assert 'Staten Island' text from a random(randrange(1, 14)) 'Staten Island' location
        print("\n===========================")
        self.click(LocationsPage.borough)
        self.click(LocationsPage.richmond)
        self.click(LocationsPage.apply_boro)
        try:
            richmond_library_info = self.get_text(LocationsPage.random_staten_library)
        except Exception:
            print("Fetching the Staten Island Library info failed on first attempt. Retrying...")
            self.wait(wait_time)
            richmond_library_info = self.get_text(LocationsPage.random_staten_library)
        print(richmond_library_info)
        self.assert_true("Staten" in richmond_library_info)

    def test_accessibility_full(self):
        print("test_accessibility_full()\n")

        # assert  'Accessibility' filter
        self.click(LocationsPage.accessibility)  # click 'accessibility' filter
        self.click(LocationsPage.full_access)  # click 'full accessible' sub-filter
        self.click(LocationsPage.apply_access)  # click 'apply filters'
        self.wait(2)

        # total number of libraries with full accessibility
        total_lib = len(self.find_elements(LocationsPage.library_amount))
        print(str(total_lib) + " libraries with Full Accessibility")

        # assertion for libraries that don't have 'full accessibility' but listen on the 'fully accessible'
        count = 0  # counter for the libraries that don't have full accessibility but listed on 'fully accessible'
        for x in range(1, total_lib + 1):
            text = self.get_text(LocationsPage.library_amount + '[' + str(x) + ']')
            if 'Fully Accessible' in text:
                continue
            else:
                print(str(x) + "- " + self.get_text(LocationsPage.library_h2_links + '[' + str(x) + ']'))
                # print(text)
                count += 1

        if count >= 1:
            print("\nAbove " + str(
                count) + " libraries don't have full access yet listed on the 'Fully Accessible' filter")
        self.assert_true(count < 1)

    def test_accessibility_partial(self):
        print("test_partial_accessibility()\n")

        # assert 'partial access'
        self.click(LocationsPage.accessibility)  # click 'accessibility' filter
        self.click(LocationsPage.partial_access)  # click 'partially accessible' sub-filter
        self.click(LocationsPage.apply_access)  # click 'apply filters'
        self.wait(2)

        # total number of libraries with partial accessibility
        total_partial_lib = len(self.find_elements(LocationsPage.library_amount))
        # print(str(total_partial_lib) + " total partial accessible libraries:\n")

        # for loop to assert locations have "partially accessible" text
        count = 0
        for x in range(1, total_partial_lib + 1):
            text = self.get_text(LocationsPage.library_amount + '[' + str(x) + ']')
            # print(text)
            self.assert_true("Partially Accessible" in text)
            count += 1
            # print("===============")
        print(str(count) + " libraries with Partial Accessibility")

    # @pytest.mark.skip(reason="RENO-2961 and RENO-3711 needed to be fixed")
    def test_accessibility_non(self):
        print("test_not_accessible()\n")

        # assert 'not accessible' filter
        self.click(LocationsPage.accessibility)  # click 'accessibility' filter
        self.click(LocationsPage.not_access)  # click 'not accessible' filter
        self.click(LocationsPage.apply_access)  # click 'apply filters'
        self.wait(2)

        # total number of libraries without accessibility
        total_no_access_lib = len(self.find_elements(LocationsPage.library_amount))
        print(str(total_no_access_lib) + " libraries with No Accessibility")

        # TODO: update below script after below ticket fixed - IN PROGRESS
        # https://jira.nypl.org/browse/RENO-3711
        # for loop to assert locations have "not accessible" text
        count = 0
        """"
        for x in range(1, total_no_access_lib + 1):
            # currently there is no 'not accessible' text beneath the listed locations, unlike partially and fully.
            # if in future it is added, update the below TODO, with the new locator
            text = self.get_text('//TODO: put locator here if there is a 'not accessible' status text added ')
            print(text)
            self.assert_true("Not Accessible" in text)
            count += 1
        print(str(count) + " libraries with No Accessibility")
        """

    def test_amenities(self):
        print("test_amenities()\n")

        # assert 'amenities' filter
        self.assert_element(LocationsPage.amenities)

        # assert 'amenities' filter length >= 1, which is 42 as of June 2022
        amenities_filter_len = len(self.find_elements(LocationsPage.amenities_filters))
        print("Amenities filter length: " + str(amenities_filter_len))  # optional print of the amenities length

        self.assert_true(amenities_filter_len > 1, "amenities filter smaller than expected")

    def test_subject_specialties(self):
        print("test_subject_specialties()\n")

        # assert subject_specialties filter  web element
        self.assert_true(LocationsPage.subject_specialties)

        # ========================================================================================

        # assert 'art' filter
        self.click(LocationsPage.subject_specialties)  # click 'subject specialties' filter
        self.click(LocationsPage.art)  # click 'art' sub-filter
        self.click(LocationsPage.apply_specialties)  # click apply

        # length of the filter == 10 as of June 2022
        art_filter_len = len(self.find_elements(LocationsPage.library_amount))
        print("art filter length: " + str(art_filter_len))

        # assert art filter length is more than 8
        if art_filter_len == 0:
            print("if clause: filter is 0, will wait a few seconds")
            self.wait(3)
            art_filter_len = len(self.find_elements(LocationsPage.library_amount))
            self.assert_true(art_filter_len > 1)
            print("New art filter length: " + str(art_filter_len))
        else:
            print("else clause: filter was visible on first try without waits")
            self.assert_true(art_filter_len > 1)

        self.click(LocationsPage.clear_all_search)

        # ========================================================================================

        # assert history filter
        self.click(LocationsPage.subject_specialties)  # click 'subject specialties' filter
        self.click(LocationsPage.history)  # click 'history' sub-filter
        self.click(LocationsPage.apply_specialties)  # click apply

        history_filter_len = len(self.find_elements(LocationsPage.library_amount))
        print("\nhistory filter length: " + str(history_filter_len))

        # assert history filter length greater than 8, currently 11 as of June 2022
        if history_filter_len == 0:
            print("if clause: filter is 0, will wait a few seconds")
            self.wait(3)
            history_filter_len = len(self.find_elements(LocationsPage.library_amount))
            self.assert_true(history_filter_len > 1)
            print("new history filter length: " + str(history_filter_len))
        else:
            print("else clause: filter was visible on first try without waits")
            self.assert_true(history_filter_len > 1)

        self.click(LocationsPage.clear_all_search)

        # ========================================================================================

        # assert social sciences filter
        self.click(LocationsPage.subject_specialties)  # click 'subject specialties' filter
        self.click(LocationsPage.social_sciences)  # click 'social sciences' sub-filter
        self.click(LocationsPage.apply_specialties)  # click apply

        social_sciences_len = len(self.find_elements(LocationsPage.library_amount))
        print("\nsocial filter length: " + str(social_sciences_len))

        # assert social sciences filter length greater than 8, which is 10, as of June 2022
        if social_sciences_len == 0:
            print("if clause: filter is 0, will wait a few seconds")
            self.wait(3)
            social_sciences_len = len(self.find_elements(LocationsPage.library_amount))
            self.assert_true(social_sciences_len > 1)
            print("new social filter length: " + str(social_sciences_len))
        else:
            print("else clause: filter was visible on first try without waits")
            self.assert_true(social_sciences_len > 1)

        self.click(LocationsPage.clear_all_search)

    def test_media_types(self):
        print("test_media_types()\n")

        # assert 'media types' filter
        self.assert_true(LocationsPage.media_types_filters)

        # assert 'media types' filter length >= 1, which is 13 as of Feb 2024
        media_types_len = len(self.find_elements(LocationsPage.media_types_filters))
        print("Media Types filter length: " + str(media_types_len))  # optional print of the media types length

        self.assert_true(media_types_len > 1, "media types filter smaller than expected")

    @pytest.mark.skip(reason="These tests are divided into 3 parts to save time")
    @pytest.mark.smoke
    def test_open_hours_1(self):
        print("test_open_hours_1()\n")

        # this test runs the whole libraries from 1st to last (131st) in 1 run. below tests are divided into 3 parts

        failure_messages = []
        library_amount = len(self.find_elements(LocationsPage.library_info))

        # todo: test takes too long. consider using API for this test

        open_text = "today's hours"
        total_count = 0
        open_count = 0
        closed_count = 0
        neither_count = 0

        # assert each location's OPEN/CLOSED status on Location Finder vs Individual Page
        for x in range(1, library_amount + 1):  # Adjust range as needed
            library = LocationsPage.library_link + '[' + str(x) + ']'

            # Try-except block to handle NoSuchElementException and retry after a short delay
            try:
                library_name = self.get_text(library)
            except NoSuchElementException:
                print(f"Element {library} not found. Retrying after 4 seconds...")
                self.wait(4)  # Sleep for 4 seconds before retrying
                library_name = self.get_text(library)  # Retry the action

            library_info = self.get_text(LocationsPage.library_info + "[" + str(x) + "]").lower()

            if "closed" in library_info:
                print("\n\n================================================")
                print("CLOSED - " + library_name + " (" + str(x) + ")")

                self.click(library)
                location_info_text = self.find_element(LocationsPage.location_info).text.lower()

                if not ("temporarily closed" in location_info_text or "closed today" in location_info_text):
                    failure_messages.append(
                        f"{library_name} does not display 'Temporarily Closed' or 'Closed Today' status")

                print("================================================\n\n")
                closed_count += 1
            elif open_text in library_info:
                print("\nOPEN - " + library_name + " (" + str(x) + ")" + "\n")
                open_count += 1

                self.click(library)
                location_info_text = self.get_text(LocationsPage.location_info).lower()

                if "open today" not in location_info_text:
                    failure_messages.append(f"{library_name} does not display Open today status")
            else:
                print("\n\n================================================")
                print("NEITHER OPEN OR CLOSED - " + library_name + " (" + str(x) + ")")
                print(library_info)
                print("================================================\n\n")
                neither_count += 1

            total_count += 1
            self.goto(LocationsPage.locations_page_link)  # go back to locations page

        print("\nTotal Libraries: " + str(library_amount))
        print("Total OPEN = " + str(open_count))
        print("Total CLOSED = " + str(closed_count))
        print("Total NEITHER = " + str(neither_count))
        print("Total gone thru: " + str(total_count))

        # Check for any accumulated errors
        if failure_messages:
            raise AssertionError("\n".join(failure_messages))

        # Optional: assert on total counts
        self.assert_true(total_count == open_count + closed_count + neither_count, "Library counts don't add up")

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_open_hours_2(self):
        # this test runs between 1-40 libraries

        print("test_open_hours_2()\n")

        failure_messages = []
        library_amount = len(self.find_elements(LocationsPage.library_info))

        open_text = "today's hours"
        total_count = 0
        open_count = 0
        closed_count = 0
        neither_count = 0

        for x in range(1, 40):  # Adjust range as needed
            library = LocationsPage.library_link + '[' + str(x) + ']'

            # Try-except block to handle NoSuchElementException and retry after a short delay
            try:
                library_name = self.get_text(library)
            except NoSuchElementException:
                print(f"Element {library} not found. Retrying after 4 seconds...")
                self.wait(4)  # Sleep for 4 seconds before retrying
                library_name = self.get_text(library)  # Retry the action

            library_info = self.get_text(LocationsPage.library_info + "[" + str(x) + "]").lower()

            if "closed" in library_info:
                print("\n\n================================================")
                print("CLOSED - " + library_name + " (" + str(x) + ")")

                self.click(library)
                location_info_text = self.find_element(LocationsPage.location_info).text.lower()

                if not ("temporarily closed" in location_info_text or "closed today" in location_info_text):
                    failure_messages.append(
                        f"{library_name} does not display 'Temporarily Closed' or 'Closed Today' status")

                print("================================================\n\n")
                closed_count += 1
            elif open_text in library_info:
                print("\nOPEN - " + library_name + " (" + str(x) + ")" + "\n")
                open_count += 1

                self.click(library)
                location_info_text = self.get_text(LocationsPage.location_info).lower()

                if "open today" not in location_info_text:
                    failure_messages.append(f"{library_name} does not display Open today status")
            else:
                print("\n\n================================================")
                print("NEITHER OPEN OR CLOSED - " + library_name + " (" + str(x) + ")")
                print(library_info)
                print("================================================\n\n")
                neither_count += 1

            total_count += 1
            self.goto(LocationsPage.locations_page_link)  # go back to locations page

        print("\nTotal Libraries: " + str(library_amount))
        print("Total OPEN = " + str(open_count))
        print("Total CLOSED = " + str(closed_count))
        print("Total NEITHER = " + str(neither_count))
        print("Total gone thru: " + str(total_count))

        # Check for any accumulated errors
        if failure_messages:
            raise AssertionError("\n".join(failure_messages))

        # Optional: assert on total counts
        self.assert_true(total_count == open_count + closed_count + neither_count, "Library counts don't add up")

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_open_hours_3(self):
        # this test runs between 40-80 libraries

        print("test_open_hours_3()\n")

        failure_messages = []
        library_amount = len(self.find_elements(LocationsPage.library_info))

        open_text = "today's hours"
        total_count = 0
        open_count = 0
        closed_count = 0
        neither_count = 0

        for x in range(40, 80):  # Adjust range as needed
            library = LocationsPage.library_link + '[' + str(x) + ']'

            # Try-except block to handle NoSuchElementException and retry after a short delay
            try:
                library_name = self.get_text(library)
            except NoSuchElementException:
                print(f"Element {library} not found. Retrying after 4 seconds...")
                self.wait(4)  # Sleep for 4 seconds before retrying
                library_name = self.get_text(library)  # Retry the action

            library_info = self.get_text(LocationsPage.library_info + "[" + str(x) + "]").lower()

            if "closed" in library_info:
                print("\n\n================================================")
                print("CLOSED - " + library_name + " (" + str(x) + ")")

                self.click(library)
                location_info_text = self.find_element(LocationsPage.location_info).text.lower()

                if not ("temporarily closed" in location_info_text or "closed today" in location_info_text):
                    failure_messages.append(
                        f"{library_name} does not display 'Temporarily Closed' or 'Closed Today' status")

                print("================================================\n\n")
                closed_count += 1
            elif open_text in library_info:
                print("\nOPEN - " + library_name + " (" + str(x) + ")" + "\n")
                open_count += 1

                self.click(library)
                location_info_text = self.get_text(LocationsPage.location_info).lower()

                if "open today" not in location_info_text:
                    failure_messages.append(f"{library_name} does not display Open today status")
            else:
                print("\n\n================================================")
                print("NEITHER OPEN OR CLOSED - " + library_name + " (" + str(x) + ")")
                print(library_info)
                print("================================================\n\n")
                neither_count += 1

            total_count += 1
            self.goto(LocationsPage.locations_page_link)  # go back to locations page

        print("\nTotal Libraries: " + str(library_amount))
        print("Total OPEN = " + str(open_count))
        print("Total CLOSED = " + str(closed_count))
        print("Total NEITHER = " + str(neither_count))
        print("Total gone thru: " + str(total_count))

        # Check for any accumulated errors
        if failure_messages:
            raise AssertionError("\n".join(failure_messages))

        # Optional: assert on total counts
        self.assert_true(total_count == open_count + closed_count + neither_count, "Library counts don't add up")

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_open_hours_4(self):
        # this test runs between 80-last libraries

        print("test_open_hours_4()\n")

        failure_messages = []
        library_amount = len(self.find_elements(LocationsPage.library_info))

        open_text = "today's hours"
        total_count = 0
        open_count = 0
        closed_count = 0
        neither_count = 0

        for x in range(80, library_amount + 1):  # Adjust range as needed
            library = LocationsPage.library_link + '[' + str(x) + ']'

            # Try-except block to handle NoSuchElementException and retry after a short delay
            try:
                library_name = self.get_text(library)
            except NoSuchElementException:
                print(f"Element {library} not found. Retrying after 4 seconds...")
                self.wait(4)  # Sleep for 4 seconds before retrying
                library_name = self.get_text(library)  # Retry the action

            library_info = self.get_text(LocationsPage.library_info + "[" + str(x) + "]").lower()

            if "closed" in library_info:
                print("\n\n================================================")
                print("CLOSED - " + library_name + " (" + str(x) + ")")

                self.click(library)
                location_info_text = self.find_element(LocationsPage.location_info).text.lower()

                if not ("temporarily closed" in location_info_text or "closed today" in location_info_text):
                    failure_messages.append(
                        f"{library_name} does not display 'Temporarily Closed' or 'Closed Today' status")

                print("================================================\n\n")
                closed_count += 1
            elif open_text in library_info:
                print("\nOPEN - " + library_name + " (" + str(x) + ")" + "\n")
                open_count += 1

                self.click(library)
                location_info_text = self.get_text(LocationsPage.location_info).lower()

                if "open today" not in location_info_text:
                    failure_messages.append(f"{library_name} does not display Open today status")
            else:
                print("\n\n================================================")
                print("NEITHER OPEN OR CLOSED - " + library_name + " (" + str(x) + ")")
                print(library_info)
                print("================================================\n\n")
                neither_count += 1

            total_count += 1
            self.goto(LocationsPage.locations_page_link)  # go back to locations page

        print("\nTotal Libraries: " + str(library_amount))
        print("Total OPEN = " + str(open_count))
        print("Total CLOSED = " + str(closed_count))
        print("Total NEITHER = " + str(neither_count))
        print("Total gone thru: " + str(total_count))

        # Check for any accumulated errors
        if failure_messages:
            raise AssertionError("\n".join(failure_messages))

        # Optional: assert on total counts
        self.assert_true(total_count == open_count + closed_count + neither_count, "Library counts don't add up")
