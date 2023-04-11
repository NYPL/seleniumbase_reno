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
from examples.nypl_pages.page_online_resources import OnlineResourcesPage
from examples.nypl_pages.page_research import ResearchPage
from examples.nypl_pages.page_research_support import ResearchSupportPage
from examples.nypl_pages.page_snfl import SnflPage

from selenium.webdriver.common.by import By

import requests
import urllib3


class NyplUtils(HeaderPage, SchwarzmanPage, GivePage, HomePage, BlogPage, BlogAllPage, BookListsPage, CampaignsPage,
                ExhibitionsPage, FooterPage, LocationsPage, OnlineResourcesPage, ResearchPage, ResearchSupportPage, SnflPage):
    """nypl login method for the catalog,
       taking 2 parameters, 'username' and 'password' """

    def nypl_login_catalog(self, username, password):
        # click login button
        self.click(self.login)
        # click 'log into the catalog'
        self.click(self.login_catalog)
        # enter username
        self.send_keys(self.username, username)
        # enter password
        self.send_keys(self.password, password)
        # click submit
        self.click(self.submit)

    """nypl login method for the research,
       taking 2 parameters, "username" and 'password' """

    def nypl_login_research(self, username, password):
        # click login button
        self.click(self.login)
        # click log into the research catalog
        self.click(self.login_research_catalog)
        # enter username
        self.send_keys(self.username, username)
        # enter password
        self.send_keys(self.password, password)
        # click submit
        self.click(self.submit)

    """ link assertion:
       click a link and assert the text in the URL,
       taking 2 parameters, 'link' to be clicked and 'text' to be checked"""

    def link_assertion(self, link, text):
        self.click(link)
        # assert the text in the URL
        self.assert_true(text in self.get_current_url(), "link and url texts did not match- expected = " + text + ", "
                                                                                                                  "actual = " + self.get_current_url())
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

    """assert links valid:
       A method to assert the child links are not broken in a list item ('li' tag),
       using HTTP method HEAD, and checks if the response is between the acceptable limits (200-400)
       """

    def assert_links_valid(self, locator):
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

    """a method to assert all the images on a  page.
       Using the default URL to test, or, a parameter can be added for URL,
       and then call method signature with the 'url' argument, e.g. image_assertion(self, url):"""

    def image_assertion(self):
        broken_image_count = 0  # broken image number instantiation

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # disabling some warnings

        image_list = self.find_elements('img')  # getting the images with the 'img' tag

        print('Total number of images on ' + self.get_current_url() + ' are = ' + str(len(image_list)))

        x = 1  # variable to use in the loop for image number iteration

        # using HTTP method 'get', asserting if the status code of the images == 200, which means image exist

        encountered_exceptions = []  # List to keep track of encountered exceptions to only print once

        for img in image_list:
            try:
                response = requests.get(img.get_attribute('src'), stream=True)
                if response.status_code != 200:
                    print("\n" + img.get_attribute('outerHTML') + " is broken.")
                    broken_image_count = (broken_image_count + 1)
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

        print('\nThe page ' + self.get_current_url() + ' has ' + str(broken_image_count) + ' broken images\n')
