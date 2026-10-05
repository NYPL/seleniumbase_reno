from seleniumbase import BaseCase


class BlogPage(BaseCase):
    home = '(//*[contains(text(), "Home")])[1]'
    title = "NYPL Blog | The New York Public Library"
    blog_button = '(//*[contains(text(), "Blog")])[2]'
    nypl_blog = '(//*[contains(text(), "Blog")])[3]'

    all_links = '((//*[@id="page-container--content-primary"]//li)//a)'  # locator for 'page-container'

    featured_posts = '//*[@id="featured-posts"]'
    view_all_blogs = '(//*[contains(text(), "View all blog posts")])'

    get_a_library_card = '(//*[contains(text(),"Get a Library Card")])[1]'
    find_your_next_book = '(//*[contains(text(),"Find Your Next Book")])[1]'
    search_library_locations = '//*[contains(text(),"Search Library Loca")]'
    reserve_a_computer = '(//*[contains(text(),"Reserve a Compu")])[1]'

    need_help_1 = '//*[@id="ask-nypl"]//li[1]'
    need_help_3 = '//*[@id="ask-nypl"]//li[3]'
    need_help_4 = '//*[@id="ask-nypl"]//li[4]'
    need_help_5 = '//*[@id="ask-nypl"]//li[5]'
    need_help_6 = '//*[@id="ask-nypl"]//li[6]'

    volunteer = '(//*[contains(text(),"Volunteer")])[1]'
    support_your_library = '(//*[contains(text(),"Support Your Library")])[1]'

    featured_posts_length = '(//*[@id="featured-posts"]//..//..//..//h3)'

    view_all_channels = '//*[contains(text(), "View all channels")]'

    def open_blog_page(self):

        qa = "https://qa-www.nypl.org/blog"
        prod = "https://www.nypl.org/blog"

        if self.env == "qa":
            print("Running on QA Env")
            self.open(qa)

        else:
            print("Running on Production Env")
            self.open(prod)

