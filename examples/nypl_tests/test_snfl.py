from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_snfl import SnflPage


class SnflTest(NyplUtils):

    # https://www.nypl.org/locations/snfl

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open main page
        self.open_snfl_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_snfl_main(self):
        print("test_snfl_main()\n")

        # assert title
        self.assert_title('Stavros Niarchos Foundation Library (SNFL) | The New York Public Library')

        # assert images on the page
        self.image_assertion()

        # assert breadcrumbs and tabs
        self.assert_element(SnflPage.home)
        self.assert_element(SnflPage.locations)
        self.assert_element(SnflPage.visit)
        self.assert_element(SnflPage.explore)
        self.assert_element(SnflPage.read)

        # assert left directions pane
        self.assert_element(SnflPage.directions)
        self.assert_element(SnflPage.holiday_closings)
        expected_address = "455 Fifth Avenue"
        actual_address = self.get_text(SnflPage.address)
        self.assert_true(expected_address in actual_address,
                         "Actual " + expected_address + "doesn't match the expected " + actual_address)
        self.assert_element(SnflPage.give)
        self.assert_element(SnflPage.social_media)

        # assert that clicking on 'directions', '202x holiday hours' and links on the page will open the correct pages
        # using 'link_assertion' method from utility.py
        self.link_assertion(SnflPage.directions, "google.com/maps")
        self.link_assertion(SnflPage.holiday_closings, "nypl.org/help/closings")

        # assert 'in the spotlight' content
        self.link_assertion(SnflPage.in_the_spotlight_1, "nypl.org/locations/snfl/explore")
        self.link_assertion(SnflPage.in_the_spotlight_2, "nypl.org/locations/snfl/yoseloff-business")
        self.link_assertion(SnflPage.in_the_spotlight_3, "nypl.org/locations/snfl/event-center")
        self.link_assertion(SnflPage.in_the_spotlight_4, "nypl.org/about/locations/snfl/cafe")
        self.link_assertion(SnflPage.in_the_spotlight_5, "nypl.org/spotlight/snfl")

        # asserting 'About the Stephen A. ....'
        expected = 'About the Stavros Niarchos Foundation Library (SNFL)'
        actual = self.get_text(SnflPage.about_the_snfl)
        self.assert_true(expected == actual, "Expected = " + expected + ", Actual = " + actual)

    def test_snfl_events(self):
        print("test_snfl_events()")

        # asserting 'Kids, Teens and Adults - See All' web elements
        self.assert_element(SnflPage.kids_see_all)
        self.assert_element(SnflPage.teens_see_all)
        self.assert_element(SnflPage.adults_see_all)

        # asserting 'Kids, Teens and Adults tabs - Clicking them and comparing the titles of each to their h3 link texts
        for y in range(1, 4):
            # asserting 'For Kids' with a for loop by clicking every event and asserting the title
            # getting the length of the events h3 to use it in the for loop
            h3_length = len(
                self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/div[6]/div[1]/div/ul/li'))
            # for loop to go over every event
            for x in range(1, h3_length + 1):
                # getting the link text and assert if it is in the page title
                h3_link_text = self.get_text(
                    f'//*[@id="block-nypl-emulsify-content"]/div/div/div[6]/div[{y}]/div/ul/li[{x}]/div[2]/h3/a')
                print("\n1: link text = " + h3_link_text)
                self.click(f'//*[@id="block-nypl-emulsify-content"]/div/div/div[6]/div[{y}]/div/ul/li[{x}]/div[2]/h3/a')

                # getting the page title element
                h1_title = self.get_text('//*[@id="page-title"]')
                print("2: title =  " + h1_title)
                # asserting h3 link text to the page title
                self.assert_true(h3_link_text in h1_title)

                self.go_back()  # go to the previous page for the next loop
            print("\n=============================================\n")

    def test_snfl_remote_resources(self):
        print("test_snfl_remote_resources()")

        self.link_assertion(SnflPage.remote_resources_1, "nypl.org/books-music-movies/ebookcentral")
        self.link_assertion(SnflPage.remote_resources_2, "nypl.org/events/calendar/online")
        self.link_assertion(SnflPage.remote_resources_3, "nypl.org/research/collections/articles-databases")
        self.link_assertion(SnflPage.remote_resources_4, "nypl.org/get-help/community-resources")

    def test_snfl_explore(self):
        print("test_snfl_explore()\n")

        # click 'Explore' tab
        self.click(SnflPage.explore)

        print(self.get_title())

        # assert title
        self.assert_title('Explore Stavros Niarchos Foundation Library (SNFL) | The New York Public Library')

        # assert images on the page
        self.image_assertion()

        # assert Centers
        self.assert_links_valid(SnflPage.centers)
        self.assert_links_valid(SnflPage.more_resources)

    def test_snfl_read(self):
        print("test_snfl_read()\n")

        # click 'Read' tab
        self.click(SnflPage.read)

        print(self.get_title())

        # assert title
        self.assert_title("Stavros Niarchos Foundation Library (SNFL) Reader's Portal | The New York Public Library")

        # assert images on the page
        self.image_assertion()

        # assert top checkouts: amount assertion >= 1
        top_checkouts_amount = len(self.find_elements(SnflPage.top_checkouts))
        print("Top checkouts = " + str(top_checkouts_amount))
        self.assert_true(top_checkouts_amount >= 1, "Top checkouts not >= 1, it is " + str(top_checkouts_amount))
        # asser shelf help
        self.assert_element(SnflPage.shelf_help)

