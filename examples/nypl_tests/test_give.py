from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_give import GivePage


class Give(NyplUtils):

    # https://www.nypl.org/give

    def setUp(self):
        super().setUp()
        print("=================================")
        print("\nRUNNING BEFORE EACH TEST")

        # open blog page
        self.open_give_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_give(self):
        # https://www.nypl.org/give
        print("test_give()\n")

        # check images on the page
        self.image_assertion()

        # asserting breadcrumbs and page elements
        self.assert_element(GivePage.home)
        self.assert_element(GivePage.h1)

        # assert all links on the page
        self.assert_links_valid(GivePage.all_links)

        # asserting 'Donate' box
        self.assert_element(GivePage.donate)
        self.assert_element(GivePage.donation_form)

        self.double_click(GivePage.donate_text_field)
        self.send_keys(GivePage.donate_text_field, "125")  # asserting we can change the default amount
        self.click(GivePage.single_donation)
        self.open_give_page()
        self.click(GivePage.monthly_donation)
        self.open_give_page()

