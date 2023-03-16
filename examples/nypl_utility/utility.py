from seleniumbase import BaseCase
from examples.nypl_pages.page_header import HeaderPage
from examples.nypl_pages.page_schwarzman import SchwarzmanPage
from examples.nypl_pages.page_give import GivePage

import requests
import urllib3


class NyplUtils(HeaderPage, SchwarzmanPage, GivePage):
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

    """click a link and assert the text in the URL,
       taking 2 parameters, 'link' to be clicked and 'text' to be checked"""

    def link_assertion(self, link, text):
        self.click(link)
        # assert the text in the URL
        self.assert_true(text in self.get_current_url(), "link and url texts did not match")
        # go to the previous page
        self.go_back()

    """a method to assert all the images on a  page,
       will use the default URL to test, or, a parameter can be added for URL,
       and then call method signature with the 'url' argument, e.g. image_assertion(self, url):"""

    def image_assertion(self):
        broken_image_count = 0  # broken image number instantiation

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # disabling some warnings

        image_list = self.find_elements('img')  # getting the images with the 'img' tag

        print('Total number of images on ' + self.get_current_url() + ' are ' + str(len(image_list)))

        x = 1  # variable to use in the loop for image number iteration

        # using HTTP method 'get', asserting if the status code of the images == 200, which means image exist
        for img in image_list:
            try:
                response = requests.get(img.get_attribute('src'), stream=True)
                if response.status_code != 200:
                    print(img.get_attribute('outerHTML') + " is broken.")
                    broken_image_count = (broken_image_count + 1)
                # else clause is optional to print the images
                else:
                    # print('\nImage ' + str(x) + ' URL: ' + img.get_attribute('src'))
                    x += 1

            except requests.exceptions.MissingSchema:
                print("Encountered MissingSchema Exception")
            except requests.exceptions.InvalidSchema:
                print("Encountered InvalidSchema Exception")
            except:
                print("Encountered Some other Exception")

        print('The page ' + self.get_current_url() + ' has ' + str(broken_image_count) + ' broken images')
