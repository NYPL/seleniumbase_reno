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

        # assert breadcrumbs
        self.assert_element(EducationAdultsPage.home_button)  # home
        self.assert_element(EducationAdultsPage.education)  # education

        # assert email subscription
        self.assert_element(EducationAdultsPage.email_subscription)

    @pytest.mark.test
    def test_education_adults_links(self):
        print("test_education_adults_links()\n")

        # Assert 'h3' links for each 'h2' on the page
        total_h2_amount = len(self.find_elements(EducationAdultsPage.total_h2))
        for x in range(1, total_h2_amount):
            total_h3 = len(self.find_elements('(' + EducationAdultsPage.total_h2 + f'[{x}]//..//a)'))
            for y in range(1, total_h3 + 1):
                self.assert_page_loads_successfully('(' + EducationAdultsPage.total_h2 + f'[{x}]//..//a)[{y}]')

