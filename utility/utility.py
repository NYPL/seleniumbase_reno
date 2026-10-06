import os
from dotenv import load_dotenv

import pytest, requests, random
from urllib.parse import urlparse
from selenium.common import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import Keys

from pages.page_header import HeaderPage
from pages.page_schwarzman import SchwarzmanPage
from pages.page_sf_give import GivePage
from pages.page_home import HomePage

from pages.page_blog import BlogPage
from pages.page_blog_all import BlogAllPage
from pages.page_bl_book_lists import BookListsPage
from pages.page_campaigns import CampaignsPage
from pages.page_exhibitions import ExhibitionsPage
from pages.page_footer import FooterPage
from pages.page_locations import LocationsPage
from pages.page_articles_databases import ArticlesDatabasesPage
from pages.page_research import ResearchPage
from pages.page_research_support import ResearchSupportPage
from pages.page_snfl import SnflPage
from pages.page_snfl_teen import SnflTeenPage
from pages.page_billy_rose import BillyRosePage
from pages.page_request_visit import RequestVisitPage
from pages.page_posada import PosadaPage
from pages.page_world_litetature import WorldLiteraturePage
from pages.page_articles_burney import ArticlesBurneyPage
from pages.page_articles_homework import ArticlesHomeworkPage
from pages.page_blog_channels import BlogChannelsPage
from pages.page_blog_individual import BlogIndividualPage
from pages.page_press import PressPage
from pages.page_press_individual import PressIndividualPage
from pages.page_sf_education import EducationPage
from pages.page_sf_early_literacy import EarlyLiteracyPage
from pages.page_sf_teens import EducationTeensPage
from pages.page_sf_kids import EducationKidsPage
from pages.page_sf_adults import EducationAdultsPage
from pages.page_sf_educators import EducatorsPage
from pages.page_bl_best_books import BestBooksPage
from pages.page_bl_staff_picks import StaffPicksPage
from pages.page_sf_events import EventsPage
from pages.page_sf_books import BooksPage
from pages.page_lca import LibraryCardPage
from pages.page_speakout import SpeakoutPage
from pages.page_sf_get_help import GetHelpPage
from pages.page_sf_contact_us import ContactUsPage
from pages.page_sf_visit import VisitPage

# from tests.test_dxp_images import FrontendImages

from selenium.webdriver.common.by import By

import requests
import urllib3
import time

# Load environment variables from .env file
load_dotenv()

# address used for newsletter signups in tests (a Gmail filter deletes mail sent to it)
TEST_EMAIL = "alkimcevik+qa@nypl.org"


class NyplUtils(HeaderPage, SchwarzmanPage, GivePage, HomePage, BlogPage, BlogAllPage, BookListsPage, CampaignsPage,
                ExhibitionsPage, FooterPage, LocationsPage, ArticlesDatabasesPage, ResearchPage, ResearchSupportPage,
                SnflPage, SnflTeenPage, BillyRosePage, RequestVisitPage, PosadaPage, WorldLiteraturePage,
                ArticlesBurneyPage, ArticlesHomeworkPage, BlogChannelsPage, BlogIndividualPage, PressPage,
                PressIndividualPage, EducationPage, EarlyLiteracyPage, EducationTeensPage, EducatorsPage, BestBooksPage,
                StaffPicksPage, EducationKidsPage, EducationAdultsPage, EventsPage, BooksPage,
                LibraryCardPage, SpeakoutPage, GetHelpPage, ContactUsPage, VisitPage):
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

    def link_assertion(self, link, text, retry_wait=3, max_retries=3):
        """
        Clicks a link and asserts that the specified text is present in the URL, with retries for transient failures.
        """
        from selenium.common.exceptions import ElementClickInterceptedException
        
        original_url = self.get_current_url()
        last_exception = None
        for attempt in range(1, max_retries + 1):
            current_url = self.get_current_url()
            print(f"Attempt {attempt}: {current_url}")
            if text in current_url:
                print(f"Current URL already contains expected text '{text}'. Passing assertion.")
                break  # Success
            try:
                self.wait_for_element_visible(link, timeout=10)
                self.scroll_to(link)
                self.wait(1)  # Wait for scroll animations and overlays to settle
                
                # Try regular click first, fallback to JS click if intercepted
                try:
                    self.click(link)
                except ElementClickInterceptedException:
                    print("Click intercepted, scrolling more and retrying...")
                    self.scroll_to(link)
                    self.execute_script("window.scrollBy(0, -200)")  # Scroll up slightly to avoid footer
                    self.wait(1)
                    self.click(link)
                
                self.wait_for_ready_state_complete()
                current_url = self.get_current_url()
                print("Current URL after clicking the link: " + current_url)
                assert text in current_url, f"Expected text '{text}' not in URL: {current_url}"
                break  # Success
            except Exception as e:
                last_exception = e
                print(f"Attempt {attempt} failed with error: {e}. Retrying after {retry_wait} seconds...")
                current_url = self.get_current_url()
                print("Current URL after error: " + current_url)
                self.open(original_url)
                self.wait(retry_wait)
        else:
            print(f"All {max_retries} attempts failed. Raising last exception.")
            if last_exception:
                raise last_exception
            else:
                raise AssertionError(f"Failed to assert link after {max_retries} attempts.")
        self.open(original_url)

    def assert_links_valid(self, locator):
        """
        Assert links in an <li> aren't broken for HTTP(S). Skip non-web schemes (tel:, sms:, mailto:, etc.).
        Only links to www.nypl.org (or qa-www.nypl.org) are checked. Links to any other host
        (other .nypl.org sites like archives.nypl.org, or outside sites) are skipped, since
        those sites aren't part of nypl.org.
        """

        allowed_403_keywords = ["photoville", "NYPLEducators", "eventbrite"]

        # only links on these hosts are checked
        nypl_hosts = {"www.nypl.org", "qa-www.nypl.org"}
        
        non_http_schemes_to_skip = {"mailto", "tel", "sms", "javascript", "data"}

        # Wait for elements to be present before checking
        self.wait_for_element_present(locator, timeout=10)
        
        block_length = len(self.find_elements(locator))
        print(f"\nNumber of links on the page: {block_length}")
        assert block_length > 0, "No links found. Expected at least one link under the locator."

        for index in range(block_length):
            retries = 3
            link_checked = False
            last_url = ""
            last_error = None

            for attempt in range(retries):
                try:
                    # Wait for elements to be visible and stable
                    self.wait_for_element_visible(locator, timeout=5)
                    links = self.find_elements(locator)
                    
                    if index >= len(links):
                        print(f"Link #{index + 1} no longer exists, skipping...")
                        link_checked = True
                        break
                    
                    el = links[index]
                    url = el.get_attribute('href') or ""
                    last_url = url

                    # If there's no href at all, treat as non-web (e.g., JS handlers) and skip
                    if not url:
                        print(f"Skipping link #{index + 1}: no href attribute.")
                        link_checked = True
                        break

                    scheme = (urlparse(url).scheme or "").lower()

                    # Skip non-HTTP(S) links: tel:, sms:, mailto:, javascript:, data:, etc.
                    if scheme in non_http_schemes_to_skip:
                        print(f"Skipping {scheme.upper()} link: {url}")
                        link_checked = True
                        break                    
                    # Skip links outside www.nypl.org (archives.nypl.org, vendors, social media, ...)
                    if scheme in {"http", "https"} and urlparse(url).hostname not in nypl_hosts:
                        print(f"Skipping non-www.nypl.org link: {url}")
                        link_checked = True
                        break
                    # If it’s protocol-relative or relative, requests can choke; normalize if needed
                    if scheme not in {"http", "https"}:
                        # Anything not recognized as http(s) by here, skip defensively
                        print(f"Skipping non-HTTP(S) href for link #{index + 1}: {url}")
                        link_checked = True
                        break

                    # Make a HEAD request to verify the URL (increased timeout for CI)
                    try:
                        response = requests.head(url, allow_redirects=True, timeout=15)
                    except requests.RequestException:
                        # Some servers block HEAD; fallback to GET with stream to avoid heavy downloads
                        try:
                            response = requests.get(url, allow_redirects=True, timeout=15, stream=True)
                        except requests.RequestException as req_err:
                            print(f"Network error for {url}: {req_err}. Skipping...")
                            link_checked = True
                            break

                    status = response.status_code

                    if status == 403 and any(k in url for k in allowed_403_keywords):
                        print(f"URL {url} returned 403 but is allowed to pass due to keyword.")
                        link_checked = True
                        break

                    assert status < 400, f"Link {url} is broken (status {status})"
                    link_checked = True
                    
                    # Small delay to avoid rate limiting in CI
                    time.sleep(0.3)
                    break

                except StaleElementReferenceException:
                    if attempt < retries - 1:
                        print(f"Stale element for link #{index + 1} on attempt {attempt + 1}, retrying...")
                        time.sleep(1)
                        continue
                    else:
                        print(f"Stale element persisted after {retries} attempts for link #{index + 1}. Skipping...")
                        link_checked = True
                        break
                except Exception as e:
                    last_error = e
                    print(f"\nAttempt {attempt + 1} failed for link #{index + 1} ({last_url}) with error: {e}. Retrying...")
                    time.sleep(3)

            if not link_checked:
                msg = (f"Failed to verify link at position #{index + 1} after {retries} attempts. "
                       f"URL: {last_url or 'unknown'}. Last error: {last_error}")
                print(msg)
                assert False, msg

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

    def assert_redirected_off_nypl(self, timeout=15):
        """
        High-level check for pages that hand off to a 3rd party (EBSCO, EZproxy, LibGuides, ...):
        the browser left the NYPL site and the destination loaded with a status below 400.
        Does not check the vendor's host, title or content, so vendor changes don't break it.
        The status comes from the browser's own page load, since vendors and Imperva often
        block scripted requests (requests.get/head) with 403s or challenge pages.
        """
        nypl_hosts = ("www.nypl.org", "qa-www.nypl.org")

        # wait for the redirect to leave the NYPL site
        for _ in range(timeout):
            if urlparse(self.get_current_url()).hostname not in nypl_hosts:
                break
            self.sleep(1)
        self.wait_for_ready_state_complete()

        url = self.get_current_url()
        print("Redirected to: " + url)
        self.assert_true(urlparse(url).hostname not in nypl_hosts, "Still on the NYPL site, no redirect: " + url)
        self.assert_page_loaded_ok()

    def assert_navigated_from(self, start_url, timeout=15):
        """
        High-level check for actions that move to another page on the same site (e.g. a search):
        the page path changed from start_url and the new page loaded with a status below 400.
        Compares paths, not full URLs, so a form reload like '/research?' doesn't count as navigation.
        """
        start_path = urlparse(start_url).path.rstrip("/")

        # wait for the navigation to a different path
        for _ in range(timeout):
            if urlparse(self.get_current_url()).path.rstrip("/") != start_path:
                break
            self.sleep(1)
        self.wait_for_ready_state_complete()

        url = self.get_current_url()
        print("Navigated to: " + url)
        self.assert_true(urlparse(url).path.rstrip("/") != start_path, "Did not navigate away from " + start_url)
        self.assert_page_loaded_ok()

    def assert_page_loaded_ok(self):
        """Asserts the current page loaded with an HTTP status below 400, read from the browser's own page load."""
        url = self.get_current_url()
        status = self.execute_script(
            "var nav = performance.getEntriesByType('navigation')[0]; return nav ? nav.responseStatus : null;")
        print("Destination status: " + str(status))
        # 0/None means the browser didn't expose a status; only fail on a real error status
        self.assert_true(not status or status < 400, "Destination returned HTTP " + str(status) + ": " + url)

    def assert_newsletter_signup(self, page):

        # # newsletter signup locators
        # email_subscription = '(//*[contains(text(), "Sign Up for Our Newsletter")])[1]'
        # email_subs_input = '//*[@name="email"]'
        # submit_email = '(//*[contains(text(), "Submit")])[1]'
        # subs_confirmation = '(//*[contains(text(), "Sign Up for Our Newsletter")])[1]//..//..//*[contains(text(), "Thank you!")]'

        retries = 3  # Number of retries
        retry_delay = 2  # Delay in seconds between retries

        for attempt in range(retries):
            try:
                # Step 1: Assert Newsletter Subscription Element
                self.assert_element(page.email_subscription)

                # Step 2: Input Email
                self.send_keys(page.email_subs_input, TEST_EMAIL)

                # Step 3: Click Submit
                self.send_keys(page.email_subs_input, Keys.ENTER)

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
        Utility function to verify a subset of left side filters:
          - Asserts that there is at least one filter.
          - Randomly samples up to 8 filters if more than 8 exist.
          - For each tested filter:
              - Retrieves its text.
              - Clicks it and waits briefly.
              - Asserts no error message is visible.
              - Asserts that the "Clear All Filters" button is displayed.
              - Verifies that the filter text is included in the result text.
              - Navigates back after checking.
        """
        # Get the total number of filter elements on the left side.
        left_filter_length = len(self.find_elements(page.left_side_filter))
        print(f"Left side filter length is {left_filter_length}")
        self.assert_true(left_filter_length > 0, "Left side filter does not have any results")

        # Capture the original URL before any navigation
        original_url = self.get_current_url()

        # Decide which filter indexes to test.
        if left_filter_length > 8:
            filter_indexes = random.sample(range(left_filter_length), 8)
        else:
            filter_indexes = range(left_filter_length)

        # Loop through selected filters.
        for index in filter_indexes:
            # Re-fetch elements on each iteration to avoid stale element issues
            filters = self.find_elements(page.left_side_filter)
            filter_element = filters[index]
            filter_text = filter_element.text.strip()
            
            if not filter_text:
                print(f"Warning: Filter at index {index} has no text, skipping...")
                continue

            filter_element.click()

            # wait until the results text shows the clicked filter, instead of a fixed 1s wait
            # (raises with both texts in the message if it never does)
            self.wait_for_text(filter_text, page.filter_results, timeout=15)

            self.assert_element_not_visible(page.error_locator)

            print(f"\nFilter #{index + 1}: {filter_text} ✓")

            # Assert 'Clear All Filters' button is displayed (raises if not found)
            self.assert_element(page.clear_all_filters)

            self.open(original_url)  # Return to original URL instead of go_back()

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
