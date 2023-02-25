from examples.nypl_pages.page_home import HomePage
from seleniumbase import BaseCase
from selenium.webdriver.common.action_chains import ActionChains


class HomePageTest(HomePage):

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

        # self.goto('https://qa-www.nypl.org/')

        # assert title
        self.assert_title(self.home_title)
        # assert hero
        self.assert_element(self.hero)

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
                 ("nypl.org/press", 7)
                 ]

        for y, index in links:

            print(str(index) + ": " + y)

            self.click('/html/body/div[1]/div/div[2]/main/div[2]/div[' + str(index) + ']/div/div[1]/div/h2/a')
            self.assert_true(y in self.get_current_url())
            self.go_back()

    def test_slider(self):
        # new & noteworthy slider
        print("test_slider()\n")

        # self.goto('https://qa-www.nypl.org/')

        # assert the 'New & Noteworthy' h2
        self.assert_element('/html/body/div[1]/div/div[2]/main/div[2]/div[5]/div/div[1]/div/h2')
        # getting the length of the slide and asserting it is more than X amount
        slide_length = len(self.find_elements(self.new_noteworthy_slide))
        self.assert_true(slide_length > 5)
        # asserting we can click next button and go forward

        # asserting that we can click next button
        for i in range(5):
            self.click(self.slide_next)

        # asserting we can click previous button
        for i in range(5):
            self.click(self.slide_prev)

        print("========\n")

        # asserting that we can drag the slider by dragging one of the elements
        drag_element = self.find_element(
            '/html/body/div[1]/div/div[2]/main/div[2]/div[5]/div/div[2]/div/div[2]/ul/li[4]/div/div[2]/a/div/span/img')
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(drag_element, 200, 0)
        action.perform()
