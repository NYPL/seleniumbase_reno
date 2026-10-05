import requests
from urllib.parse import urlparse

from utility.utility import NyplUtils
from pages.page_articles_homework import ArticlesHomeworkPage
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
        # Homework Help redirects to libguides; assert the destination, not its title text
        self.assert_true(urlparse(self.get_current_url()).hostname == 'libguides.nypl.org', 'Not redirected to libguides: ' + self.get_current_url())
        self.assert_true(self.get_title().strip() != '', 'Empty page title')

        # assert images on the page
        self.image_assertion()

        print(self.get_current_url())
        assert 'homework' in self.get_current_url()
