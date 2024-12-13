from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_articles_burney import ArticlesBurneyPage
import requests


class ArticlesBurneyTest(NyplUtils):

    # https://www.nypl.org/research/collections/articles-databases/17th-18th-century-burney-collection-newspapers

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open main page
        self.open_articles_burney_page()
        self.login_ad_catalog()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_articles_burney_main(self):
        print("test_articles_burney_main()\n")

        # assert title
        self.assert_title('Basic Search - Seventeenth and Eighteenth Century Burney Newspapers Collection')

        # assert status is 300s
        response = requests.head(self.get_current_url())
        print(response.status_code)
        self.assert_true(300 <= response.status_code <= 305, "Redirected Page status doesn't return between 300-305")

