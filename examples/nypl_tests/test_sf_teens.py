from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_sf_teens import EducationTeensPage


class EducationTeensTest(NyplUtils):

    # https://www.nypl.org/education/teens

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        self.set_window_size(1920, 1080)

        # open main page
        self.open_education_teens_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_education_teens_main(self):
        print("test_education_teens_page_main()\n")

        # assert title
        self.assert_title(EducationTeensPage.title)

        # assert images on the page
        self.image_assertion()

        # assert breadcrumbs
        self.assert_element(EducationTeensPage.home_button)  # home
        self.assert_element(EducationTeensPage.education)  # education

        # assert all links on the page
        self.assert_links_valid(EducationTeensPage.all_links)

        # assert social media links (Twitter, Instagram, Facebook)
        self.assert_element(EducationTeensPage.connect_with_us_instagram)
        self.assert_element(EducationTeensPage.connect_with_us_facebook)
        self.assert_element(EducationTeensPage.connect_with_us_twitter)
