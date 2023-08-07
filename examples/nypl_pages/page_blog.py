from seleniumbase import BaseCase


class BlogPage(BaseCase):
    home_button = '/html/body/div[1]/div/div/nav/ol/li[1]/a/span'
    home_title = "The New York Public Library"
    blog_button = '/html/body/div[1]/div/div/nav/ol/li[2]/span/span'
    nypl_blog = '/html/body/div[1]/div/div/main/div[1]/div/div/h1'
    nypl_blog_paragraph = '//*[@id="main-content"]/div[1]/div/div/p'

    featured_posts = '//*[@id="featured-posts"]'
    view_all_blogs = '//*[@id="page-container--content-primary"]/div[1]/div/div/a'
    take_a_look_text = '//*[@id="page-container--content-primary"]/div[1]/p'

    more_at_nypl = '//*[@id="more-at-nypl"]'

    get_a_library = '/html/body/div[1]/div/div/main/div[2]/div[2]/nav[1]/ul/li[1]/a'
    find_your_next = "//*[contains(text(),'Find Your Next Book')]"
    search_library_loca = "//*[contains(text(),'Search Library Loca')]"
    reserve_a_comp = "//*[contains(text(),'Reserve a Compu')]"

    need_help = '//*[@id="need-help?-ask-nypl"]'
    text_917 = '/html/body/div[1]/div/div/main/div[2]/div[2]/nav[2]/ul/li[3]/span'
    call_917 = '/html/body/div[1]/div/div/main/div[2]/div[2]/nav[2]/ul/li[4]/a'
    string_917_275 = '/html/body/div[1]/div/div/main/div[2]/div[2]/nav[2]/ul/li[5]/a'
    tty_212 = '/html/body/div[1]/div/div/main/div[2]/div[2]/nav[2]/ul/li[6]/span'
    support_nypl = '//*[@id="support-nypl"]'
    support_nypl_link = '//*[@id="support-nypl"]/ul/li[2]/a'
    volunteer = '/html/body/div[1]/div/div/main/div[2]/div[2]/nav[3]/ul/li[1]/a'
    support_your_library = '/html/body/div[1]/div/div/main/div[2]/div[2]/nav[3]/ul/li[2]/a'

    books_for_all = "//*[contains(text(), 'Books For All')]"
    celebrate_spring = "//*[contains(text(), 'Celebrate Spring With')]"
    e_cookbooks = "//*[contains(text(), 'Cookbooks for Passover')]"
    reading_recommendations = "//*[contains(text(), 'Reading Recommendations')]"
    announcing_the_2022 = "//*[contains(text(), 'Announcing the 2022')]"

    post_links = '//*[@id="page-container--content-primary"]/div[1]/ul/li'

    explore_by_channel = '//*[@id="explore-by-channel"]'
    view_all_channels = '//*[@id="page-container--content-primary"]/div[2]/div/div/a'
    the_nypl_blog_text = '//*[@id="page-container--content-primary"]/div[2]/p'
    first_img = '/html/body/div[1]/div/div/main/div[2]/div[1]/div[2]/ul/li[1]/div/div[1]/div'
    second_img = '/html/body/div[1]/div/div/main/div[2]/div[1]/div[2]/ul/li[2]/div/div[1]/div'
    first_box = '/html/body/div[1]/div/div/main/div[2]/div[1]/div[2]/ul/li[1]/div/div[2]/h3/a'
    second_box = '/html/body/div[1]/div/div/main/div[2]/div[1]/div[2]/ul/li[2]/div/div[2]/h3/a'

    explore_by_h2 = '//*[@id="search-filters--heading"]'

    def open_blog_page(self):
        # self.open("https://www.nypl.org/blog")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/blog")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/blog")

