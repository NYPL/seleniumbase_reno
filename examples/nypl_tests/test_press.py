from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_press import PressPage
import random


class PressTest(NyplUtils):

    # https://www.nypl.org/press

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open main page
        self.open_press_page()

    def tearDown(self):
        print("\nRUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_press_main(self):
        print("test_press_main()\n")

        # assert title
        self.assert_title(PressPage.home_title)

        # assert images on the page
        self.image_assertion()

        # assert breadcrumbs
        self.assert_element(PressPage.home)

        # assert that page h3 link amount >= 1
        page_link_number = len(self.find_elements(PressPage.page_link_amount))
        # print(page_link_number)  # optional print
        self.assert_true(page_link_number >= 1, "no h3 links on the page")

        # assert links on the page go to 'nypl.vega'
        random_amount = 10  # random choice of amount of links to be clicked. 10 total links and random, as of Aug 2023
        elements = list(range(1, page_link_number + 1))  # total range of links on the page
        random_elements = random.sample(elements, random_amount)  # random_amount to be tested out of total links

        # assert pagination amount
        pagination_amount = len(self.find_elements(PressPage.pagination_amount))
        # print(pagination_amount)  # optional print of the pagination elements amount
        self.assert_true(pagination_amount >= 1, "page amount not greater than 1")

        # asserting pagination
        self.click((PressPage.pagination_amount + "[2]"))  # going to the 2nd page and confirming 'previous' button
        # self.wait(2)
        self.assert_element(PressPage.previous_button)  # asserting previous button
        # print(self.get_current_url())  # optional print

        # for loop to test random amount of links out of total links on the page
        # as of Aug 2023, looping through all 10 links
        for x in random_elements:
            link = f'(//*[@id="main-content"]/div//ul//li//h3//a)[{x}]'
            self.click(link)
            self.wait(2)
            current_url = self.get_current_url()
            print(f"\n {x}: " + current_url)
            self.assert_true('nypl' and 'press' in current_url, "expected texts not in " + current_url)
            self.go_back()

