from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_campaigns import CampaignsPage


class Campaigns(NyplUtils):

    # https://www.nypl.org/125
    # https://www.nypl.org/125/timeline
    # https://www.nypl.org/125/topcheckouts

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open campaigns page
        # self.open_campaigns_page()  # opening URLs from within the tests itself

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_125_main(self):
        # https://www.nypl.org/125
        print("test_125()\n")
        self.open_campaigns_page(category='')

        # asserting the images on the page
        self.image_assertion()

        # assert all links on the page
        self.assert_links_valid(CampaignsPage.all_links)

        # assert home element
        self.assert_element(CampaignsPage.home)

        print("\n")
        # asserting the slides in 'The New York Public Library Through the Years'
        for y in range(1, 11):
            print(self.get_image_url(CampaignsPage.slide_images + '[' + str(y) + ']'))

        slide_length = len(self.find_elements(CampaignsPage.slide_images))  # this is 28 but there are total 10 images

        # assert slide number more than 9, currently 28 (10 as unique) as of June 2022
        print("\nSlide amount is " + str(slide_length))
        self.assert_true(slide_length > 9, "Slide length is less than desired amount")

    def test_125_timeline(self):
        # https://www.nypl.org/125/timeline
        print("test_125_timeline()\n")
        self.open_campaigns_page(category='timeline')

        # asserting the images on the page
        self.image_assertion()

        # assert all links on the page
        self.assert_links_valid(CampaignsPage.all_links)

        # assert breadcrumbs
        self.assert_element(CampaignsPage._125_years)
        self.assert_element(CampaignsPage.timeline_h1)

        # asserting cards in the page, 45 of them as of June 2022
        cards_length = len(self.find_elements(CampaignsPage.h2_cards))
        print("total cards (h2) on the page = " + str(cards_length))  # optional print of the total h2 on the page
        self.assert_true(cards_length >= 5, "Cards amount in the page is less than 5")

        # assert main h2 on the page
        self.assert_element(CampaignsPage.main_h2)

        # assert all h2 on the page
        for x in range(1, cards_length + 1):
            self.assert_element(CampaignsPage.h2_cards + '[' + str(x) + ']')

    def test_125_topCheckouts(self):
        # https://www.nypl.org/125/topcheckouts
        print("test_125_topCheckouts()\n")
        self.open_campaigns_page(category='topcheckouts')

        # asserting the images on the page
        self.image_assertion()

        # assert all links on the page
        self.assert_links_valid(CampaignsPage.all_links)

        # assert breadcrumbs
        self.assert_element(CampaignsPage._125_years)
        self.assert_element(CampaignsPage.checkouts_h1)

        # asserting h2 header 'Honorable Mention'
        self.assert_element(CampaignsPage.honorable_mention)

        # asserting the top checkout number is equal to 10
        top_checkout_amount = len(self.find_elements(CampaignsPage.top10_books))
        self.assert_true(top_checkout_amount == 10, "top checkout number is not equal to 10")


