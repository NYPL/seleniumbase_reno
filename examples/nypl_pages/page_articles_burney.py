from seleniumbase import BaseCase


class ArticlesBurneyPage(BaseCase):


    def open_articles_burney_page(self):

        qa = 'https://qa-www.nypl.org/research/collections/articles-databases/17th-18th-century-burney-collection-newspapers'
        prod = 'https://www.nypl.org/research/collections/articles-databases/17th-18th-century-burney-collection-newspapers'

        if self.env == "qa":
            print("Running on QA Env")
            self.open(qa)

        else:
            print("Running on Production Env")
            self.open(prod)
