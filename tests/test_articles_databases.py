import pytest

from utility.utility import NyplUtils
from pages.page_articles_databases import ArticlesDatabasesPage


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
        keyword = 'books'.lower()  # keyword in lowercase
        print(keyword)  # optional print
        self.send_keys(ArticlesDatabasesPage.search_bar, keyword)  # searching for keyword
        self.click(ArticlesDatabasesPage.submit_button)  # submitting the keyword
        # the search hands off to a 3rd party (EBSCO); only check that the redirect works
        self.assert_redirected_off_nypl()
