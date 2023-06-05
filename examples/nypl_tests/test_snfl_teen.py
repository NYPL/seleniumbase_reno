from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_snfl_teen import SnflTeenPage


class SnflTeenTest(NyplUtils):

    # https://www.nypl.org/locations/snfl/teen

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open main page
        self.open_snfl_teen_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_snfl_teen_main(self):
        print("test_snfl_teen_main()\n")

        # assert title
        self.assert_title('Teen Center | The New York Public Library')

        # assert images on the page
        self.image_assertion()

        # assert breadcrumbs
        self.assert_element(SnflTeenPage.home)
        self.assert_element(SnflTeenPage.locations)
        self.assert_element(SnflTeenPage.snfl)

        # assert left directions pane
        self.assert_element(SnflTeenPage.directions)
        self.assert_element(SnflTeenPage.email)
        self.assert_element(SnflTeenPage.holiday_closings)

    def test_snfl_teen_events(self):
        print("test_snfl_teen_events()\n")

        # asserting Events
        self.assert_element(SnflTeenPage.events)
        # asserting Events links
        for x in range(1, 7):
            # getting the link text and assert if it is in the page title
            h3_link = f'//*[contains(@class, "event-card event-card--locations event-card--center event-card--no-image")][{x}]//a'
            h1__text = self.get_text(h3_link)  # h1 text retrieved from teh clicked page
            print("\n1: link text = " + h1__text)
            self.click(h3_link)

            # getting the page title element
            h1_title = self.get_text('//*[@id="page-title"]')
            print("2: title =  " + h1_title)
            # asserting h3 link text to the page title
            self.assert_true(h1__text in h1_title)

            self.go_back()  # go to the previous page for the next loop

        # assert teen center resources links
        # list of teen center links to compare in the for loop
        teen_center_resources_links = ["www.nypl.org/events/snfl-teen-studios-media-lab",
                                       "www.nypl.org/locations/snfl/teen/study",
                                       "docs.google.com",
                                       "www.nypl.org/remote-learning-resources",
                                       "www.nypl.org/education/teens",
                                       "www.nypl.org/blog"]
        # loop to compare links in teen center resources, using link_assertion utility function
        for y in range(1, 7):
            self.link_assertion(f'//*[contains(@class, "link-card link-card--")][{y}]//a',
                                teen_center_resources_links[y - 1])

    def test_snfl_teen_center_resources(self):
        print("test_snfl_teen_center_resources()\n")

        self.link_assertion(SnflTeenPage.teen_center_1, 'events/snfl-teen-studios-media-lab')
        self.link_assertion(SnflTeenPage.teen_center_2, 'locations/snfl/teen/study')
        self.link_assertion(SnflTeenPage.teen_center_3, 'docs.google.com/')
        self.link_assertion(SnflTeenPage.teen_center_4, 'remote-learning-resources/college-career-pathways')
        self.link_assertion(SnflTeenPage.teen_center_5, 'education/teens')
        self.link_assertion(SnflTeenPage.teen_center_6, 'introducing-keeping-up-with-gen-z-teen-podcast')
