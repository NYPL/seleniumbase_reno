from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_sf_educators import EducatorsPage


class EducatorsTest(NyplUtils):

    # https://www.nypl.org/education/educators

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        self.set_window_size(1920, 1080)

        # open main page
        self.open_educators_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_educators_main(self):
        print("test_educators_main()\n")

        # assert title
        self.assert_title(EducatorsPage.title)

        # assert images on the page
        self.image_assertion()

        # assert breadcrumbs
        self.assert_element(EducatorsPage.home_button)  # home
        self.assert_element(EducatorsPage.education)  # education

        # assert "Read More" for 'Our Mission"
        self.assert_element(EducatorsPage.our_mission_read_more)

        # assert social media links (Twitter, Instagram, Facebook)
        self.link_assertion(EducatorsPage.connect_with_us_twitter, "NYPLEducators")
        self.link_assertion(EducatorsPage.connect_with_us_instagram, "nypleducators")
        self.link_assertion(EducatorsPage.connect_with_us_facebook, "NYPLEducators")

    def test_educators_links_1(self):
        print("test_educators_links_1()\n")

        # assert 'back to school' elements successfully load
        self.assert_page_loads_successfully(EducatorsPage.back_to_school_1)
        self.assert_page_loads_successfully(EducatorsPage.back_to_school_2)
        self.assert_page_loads_successfully(EducatorsPage.back_to_school_3)

        # assert "Attend Events & Workshops for Educators" elements successfully load
        self.assert_page_loads_successfully(EducatorsPage.attend_events_1)
        self.assert_page_loads_successfully(EducatorsPage.attend_events_2)

        # assert "Watch!" element successfully loads
        self.assert_page_loads_successfully(EducatorsPage.watch)

        # assert "Teach with NYPL" element successfully loads
        self.assert_page_loads_successfully(EducatorsPage.teach_with_nypl)
        self.assert_page_loads_successfully(EducatorsPage.teach_with_nypl_1)
        self.assert_page_loads_successfully(EducatorsPage.teach_with_nypl_2)
        self.assert_page_loads_successfully(EducatorsPage.teach_with_nypl_3)
        self.assert_page_loads_successfully(EducatorsPage.teach_with_nypl_4)

    def test_educators_links_2(self):
        print("test_educators_links_2()\n")

        # assert "Explore Resources" elements successfully load
        self.assert_page_loads_successfully(EducatorsPage.explore_resources_1)
        # self.assert_page_loads_successfully(EducatorsPage.explore_resources_2)  # skipping this assertion because
        # the URL ("https://www.mylibrarynyc.org/)" has an SSL issue
        self.assert_page_loads_successfully(EducatorsPage.explore_resources_3)

        # assert "Plan In-Class" elements successfully load
        self.assert_page_loads_successfully(EducatorsPage.plan_in_class_1)
        self.assert_element(EducatorsPage.plan_in_class_2)  # this is a mail feature, checking only the element.
        self.assert_element(EducatorsPage.plan_in_class_3)  # asserting the element only

        # assert "Discover Book Lists" element successfully loads
        self.assert_page_loads_successfully(EducatorsPage.discover_books_lists)

        # assert "Apply for Fellowship..." element successfully loads
        self.assert_page_loads_successfully(EducatorsPage.apply_for_fellowship)

        # assert "Find Additional Resources" elements successfully load
        self.assert_page_loads_successfully(EducatorsPage.find_additional_resources_1)
        self.assert_page_loads_successfully(EducatorsPage.find_additional_resources_2)
        self.assert_page_loads_successfully(EducatorsPage.find_additional_resources_3)
        self.assert_page_loads_successfully(EducatorsPage.find_additional_resources_4)




