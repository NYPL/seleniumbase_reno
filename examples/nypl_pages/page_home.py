from seleniumbase import BaseCase


class HomePage(BaseCase):
    hero = '/html/body/div[1]/div/div[2]/main/div[1]/div/div/div[2]/a'
    home_title = 'The New York Public Library'
    spotlight = '/html/body/div[1]/div/div[2]/main/div[2]/div[1]/div/div[1]/div/h2'

    slide_next = '/html/body/div[1]/div/div[2]/main/div[2]/div[5]/div/div[2]/div/div[3]/button'
    slide_prev = '/html/body/div[1]/div/div[2]/main/div[2]/div[5]/div/div[2]/div/div[1]/button'
    new_noteworthy_slide = '/html/body/div[1]/div/div[2]/main/div[2]/div[5]/div/div[2]/div/div[2]/ul/li'

    def open_home_page(self):
        # self.open("https://www.nypl.org/")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/")
