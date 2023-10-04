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

    def test_education(self):
        print("test_education()\n")

        # assert title
        self.assert_title(EducationPage.title)

        # assert images on the page
        self.image_assertion()

        # assert breadcrumbs
        self.assert_element(EducationPage.home_button)

        # assert "learning opportunities for aes"ll ag
        learning_opportunities = ["early-literacy", "kids", "teens", "adults"]
        learning_opportunities_links = [EducationPage.learning_opportunities_1, EducationPage.learning_opportunities_2,
                                        EducationPage.learning_opportunities_3, EducationPage.learning_opportunities_4]

        for link, text in zip(learning_opportunities_links, learning_opportunities):
            self.link_assertion(link, text)

        # assert "Center for Educators & Schools"
        self.link_assertion(EducationPage.center_for_educators, "education")
        # assert "Multilingual Resources"
        self.link_assertion(EducationPage.multilingual_resources, "multilingual")

        # assert "More for Babies & Toddlers"
        more_for_babies = ["early-literacy", "events/calendar", "drupal", "at-home-play"]
        more_for_babies_links = [EducationPage.more_for_babies_1, EducationPage.more_for_babies_2,
                                 EducationPage.more_for_babies_3, EducationPage.more_for_babies_4]

        for link, text in zip(more_for_babies_links, more_for_babies):
            if text != "drupal":  # Skip the assertion for "discovery"
                self.link_assertion(link, text)

        # assert "More for Kids"
        more_for_kids = ["kids", "events", "discovery", "recommendations"]
        more_for_kids_links = [EducationPage.more_for_kids_1, EducationPage.more_for_kids_2,
                               EducationPage.more_for_kids_3, EducationPage.more_for_kids_4]

        for link, text in zip(more_for_kids_links, more_for_kids):
            self.link_assertion(link, text)

        # assert "More for Teens"
        more_for_teens = ["teens", "centers", "remote", "recommendations"]
        more_for_teens_links = [EducationPage.more_for_teens_1, EducationPage.more_for_teens_2,
                                EducationPage.more_for_teens_3, EducationPage.more_for_teens_4]

        for link, text in zip(more_for_teens_links, more_for_teens):
            self.link_assertion(link, text)

        # assert "More for Adults"
        more_for_adults = ["adults", "google", "education", "events"]  # left here
        more_for_adults_links = [EducationPage.more_for_adults_1, EducationPage.more_for_adults_2,
                                 EducationPage.more_for_adults_3, EducationPage.more_for_adults_4]

        for link, text in zip(more_for_adults_links, more_for_adults):
            self.link_assertion(link, text)

        # assert "More for Educators"
        more_for_educators = ["educator", "primary", "events", "recommendations"]
        more_for_educators_links = [EducationPage.more_for_educators_1, EducationPage.more_for_educators_2,
                                    EducationPage.more_for_educators_3, EducationPage.more_for_educators_4]

        for link, text in zip(more_for_educators_links, more_for_educators):
            self.link_assertion(link, text)
