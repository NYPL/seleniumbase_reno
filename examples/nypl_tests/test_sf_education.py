from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_sf_education import EducationPage


class EducationTest(NyplUtils):

    # https://www.nypl.org/education

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        self.set_window_size(1920, 1080)

        # open main page
        self.open_education_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_education_main(self):
        print("test_education()\n")

        # assert title
        self.assert_title(EducationPage.title)

        # assert images on the page
        self.image_assertion()

        # assert breadcrumbs
        self.assert_element(EducationPage.home_button)

        # assert all links on the page
        self.assert_links_valid(EducationPage.all_links)

        # assert Newsletter Subscription
        self.assert_newsletter_signup(EducationPage)
