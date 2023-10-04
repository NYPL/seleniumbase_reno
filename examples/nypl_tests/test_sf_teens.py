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

        # assert social media links (Instagram, Facebook, Twitter)
        self.link_assertion(EducationTeensPage.follow_nypl_teens_instagram, "nyplteens")
        self.link_assertion(EducationTeensPage.follow_nypl_teens_facebook, "nyplteens")
        self.link_assertion(EducationTeensPage.follow_nypl_teens_3_twitter, "nypl_teens")

    def test_education_teens_links_1(self):
        print("test_education_teens_links_1()\n")

        # assert 'back to school' elements successfully load
        self.assert_page_loads_successfully(EducationTeensTest.back_to_school_1)
        self.assert_page_loads_successfully(EducationTeensTest.back_to_school_2)
        self.assert_page_loads_successfully(EducationTeensTest.back_to_school_3)
        self.assert_page_loads_successfully(EducationTeensTest.back_to_school_4)

        # assert 'opportunities ..." elements successfully load
        self.assert_page_loads_successfully(EducationTeensTest.opportunities_1)
        self.assert_page_loads_successfully(EducationTeensTest.opportunities_2)
        self.assert_page_loads_successfully(EducationTeensTest.opportunities_3)

        # assert 'teen voices' elements successfully load
        self.assert_page_loads_successfully(EducationTeensTest.teen_voices_1)
        self.assert_page_loads_successfully(EducationTeensTest.teen_voices_2)
        self.assert_page_loads_successfully(EducationTeensTest.teen_voices_3)

    def test_education_teens_links_2(self):
        print("test_education_teens_links_2()\n")

        # assert 'academic resources' elements successfully load
        self.assert_page_loads_successfully(EducationTeensTest.academic_resources_1)
        self.assert_page_loads_successfully(EducationTeensTest.academic_resources_2)

        # assert 'books & ebooks...' elements successfully load
        self.assert_page_loads_successfully(EducationTeensTest.books_ebooks_1)
        self.assert_page_loads_successfully(EducationTeensTest.books_ebooks_2)
        self.assert_page_loads_successfully(EducationTeensTest.books_ebooks_3)
        self.assert_page_loads_successfully(EducationTeensTest.books_ebooks_4)

        # assert 'teens 360...' element successfully loads
        self.assert_page_loads_successfully(EducationTeensTest.teens_360)

        # assert 'more from NYPL' elements successfully load
        self.assert_page_loads_successfully(EducationTeensTest.more_from_nypl_1)
        self.assert_page_loads_successfully(EducationTeensTest.more_from_nypl_2)
        self.assert_page_loads_successfully(EducationTeensTest.more_from_nypl_3)
