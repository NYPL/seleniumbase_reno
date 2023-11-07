from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_articles_homework import ArticlesHomeworkPage
import re


class ArticlesHomeworkTest(NyplUtils):

    # https://www.nypl.org/research/collections/articles-databases/featured/homework-help

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open main page
        self.open_articles_homework_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_articles_homework_main(self):
        print("test_articles_homework()\n")

        # assert title
        self.assert_title('Homework Help | The New York Public Library')

        # assert images on the page
        self.image_assertion()

        # assert breadcrumbs
        self.assert_element(ArticlesHomeworkPage.home)  # assert home button
        self.assert_element(ArticlesHomeworkPage.research)  # assert research button
        self.assert_element(ArticlesHomeworkPage.collections)  # assert collections button
        self.assert_element(ArticlesHomeworkPage.articles_databases)  # assert articles & databases button
        self.assert_element(ArticlesHomeworkPage.homework_help)  # assert homework help

        # asserting 'Clear all search terms.' button
        self.assert_element(ArticlesHomeworkPage.clear_all_search)  # assert clear all search button

        # asserting the result number > 0
        search_result_text = self.get_text(ArticlesHomeworkPage.search_result)  # retrieving the search result text
        # print(search_result_text)  # optional print
        # finding the result with regex
        search_result_number = int(re.findall(r'(\d+)', search_result_text)[1])  # getting the search number with regex
        # print(search_result_number)  # optional print
        # asserting the result number is > 0
        self.assert_true(search_result_number > 0, "actual result is not greater than 0")

        # assert number of h3 (results with links) > 0
        h3_amount = len(self.find_elements('h3'))
        h3_minimum = 1
        self.assert_true(h3_amount >= h3_minimum, "actual " + str(h3_amount) + " not > expected " + str(h3_minimum))
