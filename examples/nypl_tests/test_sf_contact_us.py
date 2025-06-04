from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_sf_contact_us import ContactUsPage


class ContactUs(NyplUtils):

    # https://www.nypl.org/get-help/contact-us

    def setUp(self):
        super().setUp()
        print("=================================")
        print("\nRUNNING BEFORE EACH TEST")

        # open blog page
        self.open_contact_us_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_contact_us(self):
        # https://www.nypl.org/get-help/contact-us
        print("test_sf_contact_us()\n")

        # # check images on the page
        # self.image_assertion()

        # asserting breadcrumbs and page elements
        self.assert_element(ContactUsPage.home)
        self.assert_element(ContactUsPage.get_help)
        self.assert_element(ContactUsPage.h1)

        # # assert title
        self.assert_title(ContactUsPage.contact_us_title)

        # assert all links on the page
        self.assert_links_valid(ContactUsPage.all_links)
