from seleniumbase import BaseCase


class FooterPage(BaseCase):

    nypl_logo = '//*[@id="footer"]/span'
    main_building_image = '//*[@id="footer"]/div[2]/div[1]/img'
    careers_page_title = 'Jobs at The New York Public Library | The New York Public Library Careers'

    '''
    footer_list = ["accessibility", "press", "careers", "space_rental", "privacy_policy"
        , "other_policies", "terms_conditions", "governance", "rules_regulations"
        , "about_nypl", "language"]
    '''

    footer_links_dic = {"accessibility": '//*[@id="footer"]/div[1]/ul[1]/li[1]/ul/li[1]/a',
                        "press": '//*[@id="footer"]/div[1]/ul[1]/li[1]/ul/li[2]/a',
                        "careers": '//*[@id="footer"]/div[1]/ul[1]/li[1]/ul/li[3]/a',
                        "space_rental": '//*[@id="footer"]/div[1]/ul[1]/li[1]/ul/li[4]/a',

                        "privacy_policy": '//*[@id="footer"]/div[1]/ul[1]/li[2]/ul/li[1]/a',
                        "other_policies": '//*[@id="footer"]/div[1]/ul[1]/li[2]/ul/li[2]/a',
                        "terms_conditions": '//*[@id="footer"]/div[1]/ul[1]/li[2]/ul/li[3]/a',
                        "governance": '//*[@id="footer"]/div[1]/ul[1]/li[2]/ul/li[4]/a',

                        "rules_regulations": '//*[@id="footer"]/div[1]/ul[1]/li[3]/ul/li[1]/a',
                        "about_nypl": '//*[@id="footer"]/div[1]/ul[1]/li[3]/ul/li[2]/a',
                        "language": '//*[@id="footer"]/div[1]/ul[1]/li[3]/ul/li[3]/a',

                        "facebook": '//*[@id="face-book-id-title"]',
                        "twitter": '//*[@id="twitter-id-title"]',
                        "instagram": '//*[@id="instagram-id-title"]',
                        "youtube": '//*[@id="youtube-id-title"]',
                        }

    accessibility = '//*[@id="footer"]/div[1]/ul[1]/li[1]/ul/li[1]/a'
    press = '//*[@id="footer"]/div[1]/ul[1]/li[1]/ul/li[2]/a'
    careers = '//*[@id="footer"]/div[1]/ul[1]/li[1]/ul/li[3]/a'
    space_rental = '//*[@id="footer"]/div[1]/ul[1]/li[1]/ul/li[4]/a'

    privacy_policy = '//*[@id="footer"]/div[1]/ul[1]/li[2]/ul/li[1]/a'
    other_policies = '//*[@id="footer"]/div[1]/ul[1]/li[2]/ul/li[2]/a'
    terms_conditions = '//*[@id="footer"]/div[1]/ul[1]/li[2]/ul/li[3]/a'
    governance = '//*[@id="footer"]/div[1]/ul[1]/li[2]/ul/li[4]/a'

    rules_regulations = '//*[@id="footer"]/div[1]/ul[1]/li[3]/ul/li[1]/a'
    about_nypl = '//*[@id="footer"]/div[1]/ul[1]/li[3]/ul/li[2]/a'
    language = '//*[@id="footer"]/div[1]/ul[1]/li[3]/ul/li[3]/a'

    facebook = '//*[contains(text(), "NYPL on Facebook")]/..'
    twitter = '//*[contains(text(), "NYPL on Twitter")]/..'
    # twitter_username = "(//*[contains(text(), 'username')])[1]"

    instagram = '//*[contains(text(), "NYPL on Instagram")]/..'
    youtube = '//*[contains(text(), "NYPL on Youtube")]/..'

    # footer is using same page as page_home
    """
    def open_home_page(self):
        # self.open("https://www.nypl.org/")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/")
    """