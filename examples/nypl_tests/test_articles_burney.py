from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_articles_burney import ArticlesBurney


class ArticlesBurneyTest(NyplUtils):

    # https://www.nypl.org/research/collections/articles-databases/17th-18th-century-burney-collection-newspapers

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open main page
        self.open_articles_burney_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_articles_burney_main(self):
        print("test_articles_burney_main()\n")

        # assert title
        self.assert_title('17th-18th Century Burney Collection Newspapers | The New York Public Library')

        # assert images on the page
        self.image_assertion()

        # assert breadcrumbs
        self.assert_element(ArticlesBurney.home)
        self.assert_element(ArticlesBurney.research)
        self.assert_element(ArticlesBurney.collections)
        self.assert_element(ArticlesBurney.articles_databases)
        self.assert_element(ArticlesBurney.burney_collection_newspapers)

        # asserting the '17th-18th Century Burney Collection Newspapers' h3 with utility function
        self.link_assertion(ArticlesBurney.h3_burney_collection_newspapers, "login")