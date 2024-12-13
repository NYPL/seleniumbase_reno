import pytest

from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_articles_databases import ArticlesDatabasesPage
import requests


class ArticlesDatabasesTest(NyplUtils):
    # https://www.nypl.org/research/collections/online-resources-databases

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open articles and databases page
        self.open_articles_databases_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_articles_databases_main(self):
        print("test_articles_databases_main_page_elements()\n")

        # asserting the images on the page
        self.image_assertion()

        # assert title
        self.assert_title(ArticlesDatabasesPage.articles_databases_title)

        # assert breadcrumbs
        self.assert_element(ArticlesDatabasesPage.home)
        self.assert_element(ArticlesDatabasesPage.research)
        self.assert_element(ArticlesDatabasesPage.collections)

        # assert all links on the page
        self.assert_links_valid(ArticlesDatabasesPage.all_links)

        # assert Newsletter Subscription
        self.assert_newsletter_signup(ArticlesDatabasesPage)

    def test_articles_databases_search(self):
        print("test_articles_databases_search()\n")

        # asserting search bar
        self.assert_element(ArticlesDatabasesPage.search_bar)

        # asserting the search results with keywords
        # searching for the keyword and asserting it shows up on the first h3 result
        keyword = 'books'.lower()  # keyword in lowercase
        print(keyword)  # optional print
        self.send_keys(ArticlesDatabasesPage.search_bar, keyword)  # searching for keyword
        self.click(ArticlesDatabasesPage.submit_button)  # submitting the keyword
        print(self.get_current_url())
        assert 'research' in self.get_current_url()

        # assert status is 300s
        response = requests.head(self.get_current_url())
        print(response.status_code)
        self.assert_true(300 <= response.status_code <= 305, "Redirected Page status doesn't return between 300-305")
