from seleniumbase import BaseCase


class ArticlesHomeworkPage(BaseCase):


    def open_articles_homework_page(self):

        qa = "https://qa-www.nypl.org/research/collections/articles-databases/featured/homework-help"
        prod = "https://www.nypl.org/research/collections/articles-databases/featured/homework-help"

        if self.env == "qa":
            print("Running on QA Env")
            self.open(qa)

        else:
            print("Running on Production Env")
            self.open(prod)
