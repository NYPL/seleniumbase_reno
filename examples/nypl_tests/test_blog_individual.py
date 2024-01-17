from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_blog_individual import BlogIndividualPage
import random


class BlogIndividualTest(NyplUtils):

    # https://www.nypl.org/blog/2022/09/22/reading-list-climate-week-nyc

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open main page
        self.open_blog_individual_page()

    def tearDown(self):
        print("\nRUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_blog_individual(self):
        print("test_blog_individual()\n")

        # assert title
        self.assert_title(BlogIndividualPage.home_title)

        # assert images on the page
        self.image_assertion()

        # assert breadcrumbs
        self.assert_element(BlogIndividualPage.home)
        self.assert_element(BlogIndividualPage.blog)

        # assert that page h3 link amount >= 1
        page_link_number = len(self.find_elements(BlogIndividualPage.page_link_amount))
        # print(page_link_number)  # optional print
        self.assert_true(page_link_number >= 1, "no h3 links on the page")

        # assert that links on the page go to 'nypl.vega'
        random_amount = 15  # random choice of amount of links to be clicked. 15 total links and random, as of Aug 2023
        elements = list(range(1, page_link_number + 1))  # total range of links on the page
        random_elements = random.sample(elements, random_amount)  # random_amount to be tested out of total links

        # for loop to test random amount of links out of total links
        # as of Aug 2023, looping through all 15 links
        for x in random_elements:
            link = f'(//*[@id="main-content"]//li//h3//a)[{x}]'
            self.click(link)
            current_url = self.get_current_url()
            print(f"\n {x}: " + current_url)
            self.assert_true('nypl' and 'vega' in current_url, "expected texts not in " + current_url)
            self.go_back()
