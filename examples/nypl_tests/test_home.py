from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_home import HomePage
from selenium.webdriver.common.action_chains import ActionChains


class HomePageTest(NyplUtils):

    # https://www.nypl.org/

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open home page
        self.open_home_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")

        super().tearDown()

    def test_home_page(self):
        print("test_home_page()\n")

        # check images on the page
        self.image_assertion()

        # assert title
        self.assert_title(HomePage.home_title)
        # assert hero
        self.assert_element(HomePage.hero)

        # assert all the h2  and 'See More' buttons ("Spotlight", "What's on", "Discover", "Staff Picks",
        # "New & Noteworthy", "From Our Blog", "Updates") in a loop

        h2_length = len(self.find_elements('/html/body/div[1]/div/div[2]/main/div[2]/div'))  # getting the length
        for x in range(1, h2_length + 1):
            # excluding 'New & Noteworthy' h2 since it has a different layout
            if x == 5:
                print("skipping x = 5\n")  # optional print
                continue

            # asserting h2 elements
            self.assert_element('/html/body/div[1]/div/div[2]/main/div[2]/div[' + str(x) + ']/div/div[1]/div/h2')
            # asserting 'See More' buttons- 'new & noteworthy' excluded
            self.assert_element('/html/body/div[1]/div/div[2]/main/div[2]/div[' + str(x) + ']/div/div[3]/div/a')

        # asserting h2s by clicking and comparing the URL on the next page
        links = [("nypl.org/spotlight", 1),
                 ("nypl.org/events", 2),
                 ("nypl.org/about/remote-resources", 3),
                 ("nypl.org/books-more/recommendations/staff-picks", 4),
                 ("nypl.org/books-music-movies/new-arrivals", 5),
                 ("nypl.org/blog", 6),
                 ("nypl.org/locations", 7)
                 ]

        for x, y in links:
            print(str(y) + ": " + x)

            self.click(f'(//*[@id="content-primary"]//h2//a)[{y}]')
            current_url_text = self.get_current_url()
            self.assert_true(x in current_url_text, "expected: " + str(y) + " actual: " + current_url_text)
            self.go_back()

    def test_slider(self):
        # new & noteworthy slider
        print("test_slider()\n")

        # getting the length of the slide and asserting it is more than X amount
        slide_length = len(self.find_elements(HomePage.new_noteworthy_slide))
        self.assert_true(slide_length > 5)
        # asserting we can click next button and go forward

        # asserting that we can click next button
        for i in range(5):
            self.click(HomePage.slide_next)

        # asserting we can click previous button
        for i in range(5):
            self.click(HomePage.slide_prev)

        print("========\n")
