from selenium.common import NoSuchElementException

from examples.nypl_pages.page_schwarzman import SchwarzmanPage
from examples.nypl_utility.utility import NyplUtils


class Schwarzman(NyplUtils):

    # https://www.nypl.org/locations/schwarzman

    def setUp(self):
        super().setUp()
        print("=================================")
        print("\nRUNNING BEFORE EACH TEST")

        # open blog page
        self.open_schwarzman_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_schwarzman_visit(self):
        print("test_schwarzman_main()\n")

        # asserting the images on the page
        self.image_assertion()

        # assert breadcrumbs and hero
        self.assert_element(SchwarzmanPage.home)
        self.assert_element(SchwarzmanPage.hero)

        # assert 'Visit' and 'Research' tabs
        self.assert_element(SchwarzmanPage.visit)
        self.assert_element(SchwarzmanPage.research)
        # asserting title
        self.assert_title("Stephen A. Schwarzman Building | The New York Public Library")

        # assert address in the left panel
        expected_address = "Fifth Avenue and 42nd Street"
        actual_address = self.get_text(SchwarzmanPage.address)
        self.assert_true(expected_address in actual_address,
                         "Actual " + expected_address + " doesn't match the expected " + actual_address)

        # assert sidebar, holiday closings, and
        # using 'link_assertion' method from utility.py
        self.assert_element(SchwarzmanPage.sidebar)  # assert sidebar
        self.link_assertion(SchwarzmanPage.holiday_closings, "nypl.org/help/closings")  # assert holiday schedule

        # assert "In the Spotlight" links with a for loop
        in_the_spotlight_link_amount = len(self.find_elements(SchwarzmanPage.in_the_spotlight))
        for x in range(1, in_the_spotlight_link_amount + 1):
            self.assert_page_loads_successfully(SchwarzmanPage.in_the_spotlight + f"[{x}]")

        # assert "Featured at the Stephen..." links with a for loop
        featured_link_amount = len(self.find_elements(SchwarzmanPage.featured_at_sasb))
        for x in range(1, featured_link_amount + 1):
            self.assert_page_loads_successfully(SchwarzmanPage.featured_at_sasb + f"[{x}]")

        # Asserting 'Current Exhibitions' by using dynamic_element_link_assertion
        # clicking each Current Exhibition and asserting the URL contains the text provided
        self.dynamic_element_link_assertion('//*[@id="block-nypl-emulsify-content"]/div/div/div[6]/div[1]/div/div/div['
                                            '2]/ul/li', "nypl.org/events/exhibitions")

        # asserting 'Events - See All' web element
        self.assert_element(SchwarzmanPage.events_see_all)
        # asserting 'Events' with a for loop by clicking every event and asserting the title
        # getting the length of the events h3 to use it in the for loop
        h3_length = len(
            self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/div[6]/div[2]/div/div/ul/li'))
        # for loop to go over every event
        for x in range(1, h3_length + 1):
            # getting the link text and assert if it is in the page title
            h3_link_text = self.get_text(
                f'//*[@id="block-nypl-emulsify-content"]/div/div/div[6]/div[2]/div/div/ul/li[{x}]/div[2]/h3/a')
            print("\n1: " + h3_link_text)
            self.click(f'//*[@id="block-nypl-emulsify-content"]/div/div/div[6]/div[2]/div/div/ul/li[{x}]/div[2]/h3/a')

            # getting the page title element
            h1_title = self.get_text('//*[@id="page-title"]')
            print("2: " + h1_title)
            # asserting h3 link text to the page title
            self.assert_true(h3_link_text in h1_title)

            self.go_back()  # go to the previous page for the next loop

        # asserting 'About the Stephen A. ....'
        self.assert_true(self.get_text(SchwarzmanPage.about_the_sasb) == "About the Stephen A. Schwarzman Building")

    def test_schwarzman_research(self):
        print("test_schwarzman_research()")

        # clicking the 'Research' tab
        self.click(SchwarzmanPage.research)

        # assert title
        self.assert_title("Research at Stephen A. Schwarzman Building | The New York Public Library")

        # asserting the images on the page
        self.image_assertion()

        # assert "Explore Divisions" links with a for loop
        explore_divisions_link_amount = len(self.find_elements(SchwarzmanPage.explore_division_centers))
        for x in range(1, explore_divisions_link_amount + 1):
            try:
                self.assert_page_loads_successfully(SchwarzmanPage.explore_division_centers + f"[{x}]")
            except NoSuchElementException:
                print("inside except block, will wait for a few seconds")
                self.wait(3)
                self.assert_page_loads_successfully(SchwarzmanPage.explore_division_centers + f"[{x}]")

        # assert "Further Resources" links with a for loop
        further_resources_link_amount = len(self.find_elements(SchwarzmanPage.further_resources))
        for x in range(1, further_resources_link_amount + 1):
            try:
                self.assert_page_loads_successfully(SchwarzmanPage.further_resources + f"[{x}]")
            except NoSuchElementException:
                print("inside except block, will wait for a few seconds")
                self.wait(3)
                self.assert_page_loads_successfully(SchwarzmanPage.further_resources + f"[{x}]")

        # assert "More NYPL Resources" links with a for loop
        more_nypl_resources_link_amount = len(self.find_elements(SchwarzmanPage.more_nypl_resources))
        for x in range(1, more_nypl_resources_link_amount + 1):
            try:
                self.assert_page_loads_successfully(SchwarzmanPage.more_nypl_resources + f"[{x}]")
            except NoSuchElementException:
                print("inside except block, will wait for a few seconds")
                self.wait(3)
                self.assert_page_loads_successfully(SchwarzmanPage.more_nypl_resources + f"[{x}]")
