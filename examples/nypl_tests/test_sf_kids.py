from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_sf_kids import EducationKidsPage


class EducationKidsTest(NyplUtils):

    # https://www.nypl.org/education/kids

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        self.set_window_size(1920, 1080)

        # open main page
        self.open_education_kids_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_education_kids_main(self):
        print("test_education_kids_page_main()\n")

        # assert title
        self.assert_title(EducationKidsPage.title)

        # assert images on the page
        self.image_assertion()

        # assert breadcrumbs
        self.assert_element(EducationKidsPage.home_button)  # home
        self.assert_element(EducationKidsPage.education)  # education

        # assert all links on the page
        self.assert_links_valid(EducationKidsPage.all_links)

        # assert Newsletter Subscription
        self.assert_newsletter_signup(EducationKidsPage)
