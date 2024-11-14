import pytest

from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_sf_adults import EducationAdultsPage


class EducationAdultsTest(NyplUtils):

    # https://www.nypl.org/education/adults

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        self.set_window_size(1920, 1080)

        # open main page
        self.open_education_adults_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_education_adults_main(self):
        print("test_education_adults_page_main()\n")

        # assert title
        self.assert_title(EducationAdultsPage.title)

        # assert images on the page
        self.image_assertion()

        # assert all links on the page
        self.assert_links_valid(EducationAdultsPage.all_links)

        # assert breadcrumbs
        self.assert_element(EducationAdultsPage.home_button)  # home
        self.assert_element(EducationAdultsPage.education)  # education

        # assert Newsletter Subscription
        self.assert_newsletter_signup(EducationAdultsPage)
