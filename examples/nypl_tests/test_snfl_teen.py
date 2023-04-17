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

        # asserting Events
        self.assert_element(SnflTeenPage.events)
        # asserting Events links
        for x in range(1, 7):
            # getting the link text and assert if it is in the page title
            h3_link_text = self.get_text(
                f'//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/div/div/ul/li[{x}]/div[2]/h3/a')
            print("\n1: link text = " + h3_link_text)
            self.click(f'//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/div/div/ul/li[{x}]/div[2]/h3/a')

            # getting the page title element
            h1_title = self.get_text('//*[@id="page-title"]')
            print("2: title =  " + h1_title)
            # asserting h3 link text to the page title
            self.assert_true(h3_link_text in h1_title)

            self.go_back()  # go to the previous page for the next loop

        self.link_assertion(SnflTeenPage.teen_center_1, 'www.nypl.org/events/snfl-teen-studios-media-lab')
        self.link_assertion(SnflTeenPage.teen_center_2, 'www.nypl.org/locations/snfl/teen/study')
        self.link_assertion(SnflTeenPage.teen_center_3, 'docs.google.com')
        self.link_assertion(SnflTeenPage.teen_center_4, 'www.nypl.org/remote-learning-resources')
        self.link_assertion(SnflTeenPage.teen_center_5, 'www.nypl.org/education/teens')
        self.link_assertion(SnflTeenPage.teen_center_6, 'www.nypl.org/blog')

