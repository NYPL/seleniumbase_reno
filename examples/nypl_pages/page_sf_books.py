from seleniumbase import BaseCase


class BooksPage(BaseCase):
    home_button = '(//*[contains(text(), "Home")])[1]'  # 'home' breadcrumb
    books = '(//*[contains(text(), "Books")])[3]'  # 'books/music/movies' breadcrumb
    title = 'Books/Music/Movies | The New York Public Library'

    all_links = '((//*[@id="page-container--content-primary"]//li)//a)'  # locator for 'page-container'

    # newsletter signup locators
    email_subscription = '(//*[contains(text(), "Sign Up for Our Newsletter")])[1]'
    email_subs_input = '//*[@id="email-input"]'
    submit_email = '(//*[contains(text(), "Submit")])[1]'
    subs_confirmation = '(//*[contains(text(), "Sign Up for Our Newsletter")])[1]//..//..//*[contains(text(), "Thank you!")]'

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
