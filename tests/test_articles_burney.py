from utility.utility import NyplUtils
from pages.page_articles_burney import ArticlesBurneyPage


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

        # the NYPL page hands off to a 3rd party (EZproxy login for the Gale database);
        # only check that the redirect works, not the vendor's page
        self.assert_redirected_off_nypl()
