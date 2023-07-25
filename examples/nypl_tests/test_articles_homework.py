from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_articles_homework import ArticlesHomework
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
        self.assert_element(ArticlesHomework.home)
        self.assert_element(ArticlesHomework.research)
        self.assert_element(ArticlesHomework.collections)
        self.assert_element(ArticlesHomework.articles_databases)
        self.assert_element(ArticlesHomework.homework_help)

        # asserting 'Clear all search terms.' button
        self.assert_element(ArticlesHomework.clear_all_search)
        # asserting the result number > 0
        search_result_text = self.get_text(ArticlesHomework.search_result)
        # print(search_result_text)  # optional print
        # finding the result with regex
        search_result_number = int(re.findall(r'(\d+)', search_result_text)[1])
        # print(search_result_number)  # optional print
        # asserting the number is > 0
        self.assert_true(search_result_number > 0, "actual result is not greater than 0")
