from selenium.common import NoSuchElementException

from examples.nypl_pages.page_header import HeaderPage
from examples.nypl_pages.page_schwarzman import SchwarzmanPage
from examples.nypl_pages.page_give import GivePage
from examples.nypl_pages.page_home import HomePage

from examples.nypl_pages.page_blog import BlogPage
from examples.nypl_pages.page_blog_all import BlogAllPage
from examples.nypl_pages.page_book_lists import BookListsPage
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
from examples.nypl_pages.page_sf_educators import EducatorsPage

# from examples.nypl_tests.test_dxp_images import FrontendImages

from selenium.webdriver.common.by import By

import requests
import urllib3
import time


class NyplUtils(HeaderPage, SchwarzmanPage, GivePage, HomePage, BlogPage, BlogAllPage, BookListsPage, CampaignsPage,
                ExhibitionsPage, FooterPage, LocationsPage, ArticlesDatabasesPage, ResearchPage, ResearchSupportPage,
                SnflPage, SnflTeenPage, BillyRosePage, RequestVisitPage, PosadaPage, WorldLiteraturePage,
                ArticlesBurneyPage, ArticlesHomeworkPage, BlogChannelsPage, BlogIndividualPage, PressPage,
                PressIndividualPage, EducationPage, EarlyLiteracyPage, EducationTeensPage, EducatorsPage):

    def nypl_login_catalog(self, username, password):

        """nypl login method for the catalog,
               taking 2 parameters, 'username' and 'password' """
        try:
            self.click(self.login_button)
        except NoSuchElementException:
            self.wait(3)
            self.click(self.login_button)

        try:
            self.click(self.login_catalog)
        except NoSuchElementException:
            self.wait(3)
            self.click(self.login_catalog)

        try:
            self.send_keys(self.username, username)
        except NoSuchElementException:
            self.wait(3)
            self.send_keys(self.username, username)

        try:
            self.send_keys(self.password, password)
        except NoSuchElementException:
            self.wait(3)
            self.send_keys(self.password, password)

        try:
            self.click(self.submit)
        except NoSuchElementException:
            self.wait(3)
            self.click(self.submit)

    """nypl login method for the research,
       taking 2 parameters, "username" and 'password' """

    def nypl_login_research(self, username, password):
        try:
            self.click(self.login_button)
        except NoSuchElementException:
            self.wait(3)
            self.click(self.login_button)

        try:
            self.click(self.login_research_catalog)
        except NoSuchElementException:
            self.wait(3)
            self.click(self.login_research_catalog)

        try:
            self.send_keys(self.username, username)
        except NoSuchElementException:
            self.wait(3)
            self.send_keys(self.username, username)

        try:
            self.send_keys(self.password, password)
        except NoSuchElementException:
            self.wait(3)
            self.send_keys(self.password, password)

        try:
            self.click(self.submit)
        except NoSuchElementException:
            self.wait(3)
            self.click(self.submit)

    """ link assertion:
       click a link and assert the text in the URL,
       taking 2 parameters, 'link' to be clicked and 'text' to be checked"""

    def link_assertion(self, link, text):
        self.click(link)

        try:
            # Try asserting the text in the URL
            self.assert_true(text in self.get_current_url(),
                             "expected link = " + text + ", actual link = " + self.get_current_url())
            print(self.get_current_url())
        except AssertionError:
            # If there's an AssertionError, wait for a few seconds and try again
            print("In 'Except' block, sleeping for a few seconds now")
            print("link before sleep")
            print(self.get_current_url())
            time.sleep(5)  # waits for 5 seconds. You can adjust this value as needed
            print("link after sleep")
            print(self.get_current_url())
            # Capture a screenshot just before the assertion
            self.save_screenshot("screenshot_before_assertion.png")
            self.assert_true(text in self.get_current_url(),
                             "expected link = " + text + ", actual link = " + self.get_current_url())

        # go to the previous page
        self.go_back()

    """ dynamic element link assertion:
    using link_assertion() method, click a link and assert the text in the URL,
    taking 2 parameters, 'locator' to be clicked and 'text' to be checked"""

    def dynamic_element_link_assertion(self, locator, text):
        # find the element with the locator and get the length
        exhibitions_length = len(self.find_elements(locator))

        # for loop to iterate over every element and asserting the link and text with link_assertion() method
        for x in range(1, exhibitions_length + 1):
            self.link_assertion(
                locator + '[' + str(x) + ']', text)

    def assert_links_valid(self, locator):
        """
        assert links valid in a <li, List Item:
       A method to assert that the child links are not broken in a list item ('li' tag),
       using HTTP method HEAD, and checks if the response is between the acceptable limits (200-400)
        :param locator:
        :return:
        """
        block_length = len(
            self.find_elements(locator))
        print(f"Number of links found: {block_length}")
        for x in range(1, block_length + 1):
            link = (self.find_element(locator + '[' + str(
                x) + ']')).find_element(By.TAG_NAME, "a")

            url = link.get_attribute('href')
            print("\nurl: " + url)
            response = requests.head(url)
            if response.status_code == 301:
                print(
                    f"WARNING: The requested resource at {url} has been definitively moved to the URL given by the "
                    f"Location headers")
            assert response.status_code < 400, f"Link {url} is broken"
        print("\n=====================================================\n")

    """a method to assert all the links on a page.
    pros: asserts all the links on a page with the given 'url' parameter.
    cons: asserts header and footer links as well.
    """

    def assert_all_links(self, url):
        self.open(url)
        link_elements = self.find_elements('a')
        num_links = len(link_elements)
        print(f"Number of links on the page: {num_links}")
        for index, link_element in enumerate(link_elements):
            url = link_element.get_attribute('href')
            print(f"\nLink {index + 1} of {num_links}: {url}")
            response = requests.head(url)
            if response.status_code == 301:
                print(
                    f"WARNING: The requested resource at {url} has been definitively moved to the URL given by the "
                    f"Location headers")
            assert response.status_code < 400, f"Link {url} is broken"
        print("\nAll links on the page are valid!")

    def assert_page_loads_successfully(self, link_locator):
        """Clicks a link and asserts the resulting page loads with a status code between 200 and 400."""

        # Click the link using SeleniumBase
        self.click(link_locator)

        # Wait for a moment to ensure the new page is loaded
        # self.sleep(2)

        # Get the current URL
        current_url = self.get_current_url()

        # Now use requests library to check the status code of the current page
        response = requests.get(current_url)

        # Check that the status code is in the desired range
        assert 200 <= response.status_code < 400, (f"Status code {response.status_code} not in expected range [200, "
                                                   f"400) for URL: {current_url}")

        # Go back to the original page for subsequent checks
        self.go_back()

    def image_assertion(self):
        """a method to assert all the images on a  page.
           Using the default URL to test, or, a parameter can be added for URL,
           and then call method signature with the 'url' argument, e.g. image_assertion(self, url):"""
        broken_image_count = 0  # broken image number instantiation

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # disabling some warnings

        image_list = self.find_elements('img')  # getting the images with the 'img' tag

        print('Total images on ' + self.get_current_url() + ' = ' + str(len(image_list)))

        x = 1  # variable to use in the loop for image number iteration
        y = 0  # counter to add up the failed image amount

        # using HTTP method 'get', asserting if the status code of the images == 200, which means image exist

        encountered_exceptions = []  # List to keep track of encountered exceptions to only print once

        for img in image_list:
            try:
                response = requests.get(img.get_attribute('src'), stream=True)
                if response.status_code != 200:
                    print(self.get_current_url())
                    print("\n" + img.get_attribute('outerHTML') + " is broken.")
                    broken_image_count = (broken_image_count + 1)
                    y += 1
                # else clause is optional to print the images
                else:
                    # print('\nImage ' + str(x) + ' URL: ' + img.get_attribute('src'))
                    x += 1

            except requests.exceptions.MissingSchema:
                if 'MissingSchema' not in encountered_exceptions:  # checking if the exception in the list
                    print("\nEncountered MissingSchema Exception")
                    encountered_exceptions.append('MissingSchema')  # adding to the dictionary if not added before
            except requests.exceptions.InvalidSchema:
                if 'InvalidSchema' not in encountered_exceptions:  # checking if the exception in the list
                    print("\nEncountered InvalidSchema Exception")
                    encountered_exceptions.append('InvalidSchema')  # adding to the dictionary if not added before
            except:
                if 'OtherException' not in encountered_exceptions:  # checking if the exception in the list
                    print("\nEncountered Some other Exception")
                    encountered_exceptions.append('OtherException')  # adding to the dictionary if not added before

        # Check if any images failed to load
        if y >= 1:
            raise ValueError(f"{y} images failed to load.")
            # or suggest a failed state with a print statement
            # print(f"{y} images failed to load. Please check the broken image links.")

        print('\nTotal broken images on ' + self.get_current_url() + ' = ' + str(broken_image_count))
