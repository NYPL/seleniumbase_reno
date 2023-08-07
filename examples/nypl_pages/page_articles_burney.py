from seleniumbase import BaseCase


class ArticlesBurneyPage(BaseCase):
    home = '(//*[contains(text(), "Home")])[1]'
    research = '(//*[contains(text(), "Research")])[2]'
    collections = '(//*[contains(text(), "Collections")])[1]'
    articles_databases = '(//*[contains(text(), "Articles")])[1]'
    burney_collection_newspapers = '(//*[contains(text(), "Burney")])[2]'

    h3_burney_collection_newspapers = '(//*[contains(text(), "Burney")])[3]'

    def open_articles_burney_page(self):
        # self.open("https://www.nypl.org/research/collections/articles-databases/17th-18th-century-burney-collection-newspapers")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/research/collections/articles-databases/17th-18th-century-burney"
                      "-collection-newspapers")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/research/collections/articles-databases/17th-18th-century-burney"
                      "-collection-newspapers")
