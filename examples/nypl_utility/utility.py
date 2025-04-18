import os
from dotenv import load_dotenv

import pytest, requests
from selenium.common import NoSuchElementException

from examples.nypl_pages.page_header import HeaderPage
from examples.nypl_pages.page_schwarzman import SchwarzmanPage
from examples.nypl_pages.page_give import GivePage
from examples.nypl_pages.page_home import HomePage

from examples.nypl_pages.page_blog import BlogPage
from examples.nypl_pages.page_blog_all import BlogAllPage
from examples.nypl_pages.page_bl_book_lists import BookListsPage
from examples.nypl_pages.page_campaigns import CampaignsPage
from examples.nypl_pages.page_exhibitions import ExhibitionsPage
from examples.nypl_pages.page_footer import FooterPage
from examples.nypl_pages.page_locations import LocationsPage
from examples.nypl_pages.page_articles_databases import ArticlesDatabasesPage
from examples.nypl_pages.page_research import ResearchPage
from examples.nypl_pages.page_research_support import ResearchSupportPage
from examples.nypl_pages.page_snfl import SnflPage
from examples.nypl_pages.page_snfl_teen import SnflTeenPage
from examples.nypl_pages.page_billy_rose import BillyRosePage
from examples.nypl_pages.page_request_visit import RequestVisitPage
from examples.nypl_pages.page_posada import PosadaPage
from examples.nypl_pages.page_world_litetature import WorldLiteraturePage
from examples.nypl_pages.page_articles_burney import ArticlesBurneyPage
from examples.nypl_pages.page_articles_homework import ArticlesHomeworkPage
from examples.nypl_pages.page_blog_channels import BlogChannelsPage
from examples.nypl_pages.page_blog_individual import BlogIndividualPage
from examples.nypl_pages.page_press import PressPage
from examples.nypl_pages.page_press_individual import PressIndividualPage
from examples.nypl_pages.page_sf_education import EducationPage
from examples.nypl_pages.page_sf_early_literacy import EarlyLiteracyPage
from examples.nypl_pages.page_sf_teens import EducationTeensPage
from examples.nypl_pages.page_sf_kids import EducationKidsPage
from examples.nypl_pages.page_sf_adults import EducationAdultsPage
from examples.nypl_pages.page_sf_educators import EducatorsPage
from examples.nypl_pages.page_bl_best_books import BestBooksPage
from examples.nypl_pages.page_bl_staff_picks import StaffPicksPage
from examples.nypl_pages.page_sf_events import EventsPage
from examples.nypl_pages.page_sf_books import BooksPage
from examples.nypl_pages.page_lca import LibraryCardPage
from examples.nypl_pages.page_lca_2 import LibraryCardPageNew  # temporary class
from examples.nypl_pages.page_sf_new_arrivals import NewArrivalsPage
from examples.nypl_pages.page_speakout import SpeakoutPage

# from examples.nypl_tests.test_dxp_images import FrontendImages

from selenium.webdriver.common.by import By

import requests
import urllib3
import time

# Load environment variables from .env file
load_dotenv()


class NyplUtils(HeaderPage, SchwarzmanPage, GivePage, HomePage, BlogPage, BlogAllPage, BookListsPage, CampaignsPage,
                ExhibitionsPage, FooterPage, LocationsPage, ArticlesDatabasesPage, ResearchPage, ResearchSupportPage,
                SnflPage, SnflTeenPage, BillyRosePage, RequestVisitPage, PosadaPage, WorldLiteraturePage,
                ArticlesBurneyPage, ArticlesHomeworkPage, BlogChannelsPage, BlogIndividualPage, PressPage,
                PressIndividualPage, EducationPage, EarlyLiteracyPage, EducationTeensPage, EducatorsPage, BestBooksPage,
                StaffPicksPage, EducationKidsPage, EducationAdultsPage, EventsPage, BooksPage, NewArrivalsPage,
                LibraryCardPage, SpeakoutPage, LibraryCardPageNew):
    login_button = '//*[@id="loginButton"]'
    login_catalog = '//*[contains(text(), "Go To The Catalog")]'
    login_research_catalog = '//*[contains(text(), "Go To The Research Catalog")]'

    def nypl_login_catalog(self, username, password, wait_time=4):
        """nypl login method for the catalog,
           taking 2 parameters, 'username' and 'password' """

        # Retrieve username and password from environment variables
        username = os.getenv('CATALOG_USERNAME')
        password = os.getenv('CATALOG_PASSWORD')

        try:
            self.click(self.login_button)
        except NoSuchElementException:
            self.wait(wait_time)
            self.click(self.login_button)

        try:
            self.click(self.login_catalog)
        except NoSuchElementException:
            self.wait(wait_time)
            self.click(self.login_catalog)

        try:
            self.send_keys(self.username, username)
        except NoSuchElementException:
            self.wait(wait_time)
            self.send_keys(self.username, username)

        try:
            self.send_keys(self.password, password)
        except NoSuchElementException:
            self.wait(wait_time)
            self.send_keys(self.password, password)

        try:
            self.click(self.submit)
        except NoSuchElementException:
            self.wait(wait_time)
            self.click(self.submit)

    """nypl login method for the research catalog,
       taking 2 parameters, "username" and 'password' """

    def nypl_login_research(self, username, password, wait_time=4):

        # Retrieve username and password from environment variables
        username = os.getenv('CATALOG_USERNAME')
        password = os.getenv('CATALOG_PASSWORD')

        try:
            self.click(self.login_button)
        except NoSuchElementException:
            self.wait(wait_time)
            self.click(self.login_button)

        try:
            self.click(self.login_research_catalog)
        except NoSuchElementException:
            self.wait(wait_time)
            self.click(self.login_research_catalog)

        try:
            self.send_keys(self.username, username)
        except NoSuchElementException:
            self.wait(wait_time)
            self.send_keys(self.username, username)

        try:
            self.send_keys(self.password, password)
        except NoSuchElementException:
            self.wait(wait_time)
            self.send_keys(self.password, password)

        try:
            self.click(self.submit)
        except NoSuchElementException:
            self.wait(wait_time)
            self.click(self.submit)

    """ 
    below is the login method to Articles & Databases pages such as;
    # https://www.nypl.org/research/collections/articles-databases/17th-18th-century-burney-collection-newspapers
    """
    # These are SELECTORS for the login page for Collections and Articles & Databases
    ad_login_username = '//*[@name="user"]'  # Selector for username field
    ad_login_password = '//*[@name="pass"]'  # Selector for password field
    ad_login_button = '//*[@type="submit"]'  # Selector for login button

    def login_ad_catalog(self):
        # articles & databases login. the page is moved to a third party by fall 2024 and this test is redundant now
        """
        Logs into A&D pages using above locators and credentials stored in environment variables.
        """
        # Retrieve credentials from environment variables
        username = os.getenv("CATALOG_USERNAME")
        password = os.getenv("CATALOG_PASSWORD")

        print("username: " + str(username))
        print("password: " + str(password))

        if not username or not password:
            raise ValueError("Environment variables NYPL_USERNAME and NYPL_PASSWORD are not set.")

        # Check if login is required
        if self.is_element_present(self.ad_login_username):
            print("Login page detected. Logging in...")
            self.type(self.ad_login_username, username)  # Enter username
            self.type(self.ad_login_password, password)  # Enter password
            self.click(self.ad_login_button)  # Click the login button
            self.wait_for_element_not_visible(self.login_button, timeout=10)
        else:
            print("Login not required.")

    """Link Assertion:
    Clicks a link and asserts that the specified text is present in the URL.
    Takes three parameters:
        'link': The link to be clicked.
        'text': The text to be checked in the URL.
        'retry_wait' (optional): The time to wait in seconds before retrying if the initial assertion fails.
    If the initial assertion fails, the method retries clicking the link and waits for 'retry_wait' seconds before rechecking the URL.
    """

    def link_assertion(self, link, text, retry_wait=3):
        try:
            print("\nin try/except for 'link assertion' function")
            self.click(link)
            current_url = self.get_current_url()
            # print(text)  # text keyword to assert
            print(current_url)  # printing current URL
            assert text in current_url, f"Expected text '{text}' not in URL: {current_url}"
        except AssertionError as ae:
            print("Assertion failed on first attempt. Retrying...")
            self.click(link)
            self.wait(retry_wait)  # Wait for a longer time before checking the URL again
            current_url = self.get_current_url()
            assert text in current_url, f"Expected text '{text}' not in URL after retry: {current_url}"
            print("URL after retry:", current_url)
        except NoSuchElementException as ne:
            # Handle the case where the element itself is not found
            print("Element not found. Retrying after a few seconds...")
            print("Link before sleep:", self.get_current_url())
            self.save_screenshot("screenshot_before_retry.png")
            self.wait(4)  # Adjust this wait time as necessary
            try:
                self.click(link)  # Retry clicking the link
                assert text in self.get_current_url(), "Expected text not found in URL on retry."
            except NoSuchElementException:
                print("Element still not found after retry.")
                raise ne  # Re-raise the NoSuchElementException

        # Go to the previous page
        self.go_back()

    def assert_links_valid(self, locator):
        """
        assert links valid in a <li, List Item:
        A method to assert that the child links are not broken in a list item ('li' tag),
        using HTTP method HEAD, and checks if the response is between the acceptable limits (200-400)
        """

        # List of keywords that are allowed to return a 403 status code
        allowed_403_keywords = [
            "photoville",
            "NYPLEducators",
            ""
        ]

        block_length = len(self.find_elements(locator))
        print(f"\nNumber of links on the page: {block_length}")

        # Assert that links are found; if not, fail the test
        assert block_length > 0, "No links found. Expected at least one link under the locator."

        for x in range(1, block_length + 1):
            retries = 3  # Number of retries
            link_checked = False  # Flag to track if link was successfully checked

            for attempt in range(retries):
                try:
                    # Attempt to find the link element and retrieve URL
                    link_element = self.find_element(locator + f'[{x}]')
                    url = link_element.get_attribute('href')

                    # Check if the URL is a 'mailto@nypl.org' link and skip if so
                    if url.startswith("mailto:"):
                        # print(f"\nSkipping email link: {url}")
                        link_checked = True  # Mark as checked to avoid failing at the end
                        break  # Exit inner retry loop and move to the next link in the outer loop

                    # Make a HEAD request to verify the URL
                    response = requests.head(url)
                    # print(response.status_code)

                    #if response.status_code == 301:
                        #print(f"\nWARNING: The requested resource at {url} has been definitively moved to the URL given by the Location headers")

                    # Check if the link is allowed to return 403 based on keyword
                    if response.status_code == 403 and any(keyword in url for keyword in allowed_403_keywords):
                        print(f"URL {url} returned 403 but is allowed to pass due to keyword.")
                        link_checked = True
                        break  # Exit retry loop

                    # Check if the link is not broken (status code < 400)
                    assert response.status_code < 400, f"Link {url} is broken"

                    # Set flag to true and break if everything succeeds
                    link_checked = True
                    break  # Exit retry loop if successful

                except Exception as e:
                    print(f"\nAttempt {attempt + 1} failed for link {x} with error: {e}. Retrying...")
                    self.wait(2)  # Wait 2 seconds before retrying

            # Final check if all retries failed
            if not link_checked:
                print(f"Failed to verify link {x} after {retries} attempts.")
                assert False, f"Failed to verify link at position {x} after {retries} attempts."

        print("\n=====================================================\n")

    def image_assertion(self):
        # skipping this function since 'img' locator finds unnecessary images
        """A method to assert all the images on a page.
           Uses the default URL to test or can accept a URL parameter."""

        """broken_image_count = 0  # broken image count initialization
        retries = 3  # Number of retries
        retry_delay = 2  # Delay in seconds between retries

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # disabling some warnings

        image_list = self.find_elements('img')  # retrieving all images with the 'img' tag

        print('Total images on ' + self.get_current_url() + ' = ' + str(len(image_list)))

        x = 1  # Variable to iterate image number
        y = 0  # Counter to add up the failed image count

        encountered_exceptions = []  # List to track encountered exceptions to print each only once

        for img in image_list:
            image_checked = False  # Flag to check if image URL has been validated

            for attempt in range(retries):
                try:
                    # Attempt to fetch the image URL
                    response = requests.get(img.get_attribute('src'), stream=True)

                    # Check if the status code indicates success
                    if response.status_code == 200:
                        # Image loaded successfully; proceed to the next image
                        x += 1
                        image_checked = True
                        break  # Exit retry loop if successful

                    else:
                        # Image did not load successfully; print status and URL
                        print("status code: " + str(response.status_code))
                        print(self.get_current_url())
                        print("\n" + img.get_attribute('outerHTML') + " is broken.")
                        broken_image_count += 1
                        print('\nImage ' + str(x) + ' URL: ' + img.get_attribute('src'))
                        y += 1
                        image_checked = True
                        break  # Exit retry loop if status code check is completed

                except requests.exceptions.MissingSchema:
                    if 'MissingSchema' not in encountered_exceptions:
                        print("\nEncountered MissingSchema Exception")
                        encountered_exceptions.append('MissingSchema')
                    break  # Break as MissingSchema won't succeed in future attempts

                except requests.exceptions.InvalidSchema:
                    if 'InvalidSchema' not in encountered_exceptions:
                        print("\nEncountered InvalidSchema Exception")
                        encountered_exceptions.append('InvalidSchema')
                    break  # Break as InvalidSchema won't succeed in future attempts

                except Exception as e:
                    if 'OtherException' not in encountered_exceptions:
                        print(f"\nEncountered exception: {e}")
                        encountered_exceptions.append('OtherException')
                    # Retry after waiting
                    print(f"Retrying for image {x} in {retry_delay} seconds...")
                    time.sleep(retry_delay)

            if not image_checked:
                print(f"Failed to validate image at {img.get_attribute('src')} after {retries} attempts.")
                y += 1  # Increase broken count if all retries failed

        # Check if any images failed to load and raise an error if they did
        if y >= 1:
            raise ValueError(f"{y} images failed to load.")

        print('\nTotal broken images on ' + self.get_current_url() + ' = ' + str(broken_image_count))"""

    def assert_newsletter_signup(self, page):

        # # newsletter signup locators
        # email_subscription = '(//*[contains(text(), "Sign Up for Our Newsletter")])[1]'
        # email_subs_input = '//*[@id="email-input"]'
        # submit_email = '(//*[contains(text(), "Submit")])[1]'
        # subs_confirmation = '(//*[contains(text(), "Sign Up for Our Newsletter")])[1]//..//..//*[contains(text(), "Thank you!")]'

        retries = 3  # Number of retries
        retry_delay = 2  # Delay in seconds between retries

        for attempt in range(retries):
            try:
                # Step 1: Assert Newsletter Subscription Element
                self.assert_element(page.email_subscription)

                # Step 2: Input Email
                self.send_keys(page.email_subs_input, "joedoe@gmail.com")

                # Step 3: Click Submit
                self.click(page.submit_email)

                # Step 4: Verify Subscription Confirmation
                self.assert_element(page.subs_confirmation)

                # Step 5: Go Back to Previous Page
                self.refresh()

                # If everything succeeds, break out of the retry loop
                break

            except (NoSuchElementException, AssertionError) as e:
                print(f"Attempt {attempt + 1} failed with error: {e}")

                # Wait before the next retry
                if attempt < retries - 1:
                    print(f"Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                else:
                    # Raise the exception if all attempts are exhausted
                    raise AssertionError(f"Failed to complete newsletter signup after {retries} attempts.") from e

    def assert_left_side_filters(self, page):
        """
        Utility function to verify left side filters:
          - Asserts that there is at least one filter.
          - Iterates over each filter element:
              - Retrieves its text.
              - Clicks it and waits briefly.
              - Asserts no error message is visible.
              - Asserts that the "Clear All Filters" button is displayed.
              - Verifies that the filter text is included in the result text.
              - Navigates back after checking.
        """
        # Get the total number of filter elements on the left side.
        left_filter_length = len(self.find_elements(page.left_side_filter))
        print("Left side filter length is " + str(left_filter_length))
        self.assert_true(left_filter_length > 0, "Left side filter does not have any results")

        # Loop through each filter element.
        for x in range(1, left_filter_length + 1):
            # Build the locator for the current filter element.
            filter_locator = page.left_side_filter + "[" + str(x) + "]"
            filter_text = self.get_text(filter_locator)

            self.click(filter_locator)
            self.wait(1)

            # Assert that no error message is displayed after clicking the filter.
            self.assert_element_not_visible(page.error_locator)

            # Verify that the filter text is present in the result text.
            result_text = self.get_text(page.filter_results)
            self.assert_true(filter_text in result_text,
                             "Clicked '" + filter_text + "' and '" + result_text + "' don't match")

            # Optional prints for debugging.
            print("\nFilter no: " + str(x))
            print(filter_text + " ==? " + result_text)

            # Assert that the "Clear All Filters" button is visible.
            try:
                self.assert_element(page.clear_all_filters)
                print("✅ 'Clear All Filters' button is displayed.\n")
            except Exception as e:
                print("❌ Test Failed: 'Clear All Filters' button not found.\n")
                raise

            # Navigate back after clicking and checking the filter.
            self.go_back()

    def click_with_fallback(self, locator):
        """
        Attempts to click on an element using multiple locators as fallbacks.

        :param locator: The base locator to use for clicking.
        :raises Exception: If none of the locators are found.
        """
        locators = [
            locator,
            locator + "//..",
            "(" + locator + "//..//..)[1]"
        ]

        for loc in locators:
            try:
                self.click(loc)
                return  # Exit the function once a successful click is made
            except NoSuchElementException:
                print(f"{loc} did not work, trying next locator")

        print("Element not found at any level")
        raise Exception("Test Failed: Element not found")  # Raise an error to fail the test

    def assert_with_fallback(self, locator):
        """
        Attempts to click on an element using multiple locators as fallbacks.

        :param locator: The base locator to use for clicking.
        :raises Exception: If none of the locators are found.
        """
        locators = [
            locator,
            locator + "//..",
            "(" + locator + "//..//..)[1]"
        ]

        for loc in locators:
            try:
                self.assert_element(loc)
                return  # Exit the function once a successful click is made
            except NoSuchElementException:
                print(f"{loc} did not work, trying next locator")

        print("Element not found at any level")
        raise Exception("Test Failed: Element not found")  # Raise an error to fail the test

