from seleniumbase import BaseCase


class BooksPage(BaseCase):
    home_button = '(//*[contains(text(), "Home")])[1]'  # 'home' breadcrumb
    books = '(//*[contains(text(), "Books")])[3]'  # 'books/music/movies' breadcrumb
    title = 'Books/Music/Movies | The New York Public Library'

    total_h2 = '(//*[@id="mainContent"]//h2)'  # total h2 on the page
    email_subscription = '(//*[contains(text(), "Sign Up for Our Newsletter")])[1]'  # 'newsletter signup' element

    def open_books_page(self):
        # self.open("https://www.nypl.org/books-music-movies")

        prod = "https://www.nypl.org/books-music-movies"
        qa = "https://qa-www.nypl.org/books-music-movies"

        if self.env == "qa":
            print("Running on QA Env")
            self.open(qa)

        else:
            print("Running on Production Env")
            self.open(prod)
