from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_sf_early_literacy import EarlyLiteracyPage


class EarlyLiteracyTest(NyplUtils):

    # https://www.nypl.org/education/early-literacy

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        self.set_window_size(1920, 1080)

        # open main page
        self.open_early_literacy_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_early_literacy(self):
        print("test_early_literacy()\n")

        # assert title
        self.assert_title(EarlyLiteracyPage.title)

        # assert images on the page
        self.image_assertion()

        # assert breadcrumbs
        self.assert_element(EarlyLiteracyPage.home_button)  # home
        self.assert_element(EarlyLiteracyPage.education)  # education

        # assert 'visit the library'
        visit_library = ["locations", "event", "card"]
        visit_library_links = [EarlyLiteracyPage.visit_library_1, EarlyLiteracyPage.visit_library_2,
                               EarlyLiteracyPage.visit_library_3]

        for link, text in zip(visit_library_links, visit_library):
            self.link_assertion(link, text)

        # assert 'Staten Island Big Playdate'
        self.link_assertion(EarlyLiteracyPage.staten_island, "staten")

        # assert "Activities for Little Learners"
        activities_for_learner = ["drupal", "home", "education", "vimeo"]
        activities_for_learner_links = [EarlyLiteracyPage.activities_for_learners_1,
                                        EarlyLiteracyPage.activities_for_learners_2,
                                        EarlyLiteracyPage.activities_for_learners_3,
                                        EarlyLiteracyPage.activities_for_learners_4]

        for link, text in zip(activities_for_learner_links, activities_for_learner):
            if text != "drupal":
                self.link_assertion(link, text)

        # assert 'Early Literacy' for Spanish and Chinese
        self.link_assertion(EarlyLiteracyPage.early_literacy_spanish, "es")
        self.link_assertion(EarlyLiteracyPage.early_literacy_chinese, "zh")
        