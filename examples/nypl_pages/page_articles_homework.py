from seleniumbase import BaseCase


class ArticlesHomework(BaseCase):
    home = '(//*[contains(text(), "Home")])[2]'
    research = '(//*[contains(text(), "Research")])[2]'
    collections = '(//*[contains(text(), "Collections")])[1]'
    articles_databases = '(//*[contains(text(), "Articles")])[1]'
    homework_help = '(//*[contains(text(), "Homework")])[2]'

    clear_all_search = '(//*[contains(text(), "Clear all search")])'
    search_result = '//*[@id="search-results-details"]'

    def open_articles_homework_page(self):
        prod_url = "https://www.nypl.org/research/collections/articles-databases/featured/homework-help"
        qa_url = "https://qa-www.nypl.org/research/collections/articles-databases/featured/homework-help"

        if self.env == "qa":
            print("Running on QA Env")
            self.open(prod_url)

        else:
            print("Running on Production Env")
            self.open(qa_url)
