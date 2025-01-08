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

        # assert all links on the page
        self.assert_links_valid(EducatorsPage.all_links)

        # assert Newsletter Subscription
        self.assert_newsletter_signup(EducatorsPage)

        # assert social media links (Twitter, Instagram, Facebook)
        self.assert_element(EducatorsPage.connect_with_us_twitter)
        self.assert_element(EducatorsPage.connect_with_us_instagram)
        self.assert_element(EducatorsPage.connect_with_us_facebook)

