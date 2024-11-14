import pytest

from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_sf_events import EventsPage


class EventsTest(NyplUtils):

    # https://www.nypl.org/events

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        self.set_window_size(1920, 1080)

        # open main page
        self.open_events_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_events_main(self):
        print("test_events_page_main()\n")

        # assert title
        self.assert_title(EventsPage.title)

        # assert images on the page
        self.image_assertion()

        # assert breadcrumbs
        self.assert_element(EventsPage.home_button)  # home
        self.assert_element(EventsPage.events)  # events

        # assert Newsletter Subscription
        self.assert_newsletter_signup(EventsPage)

    def test_events_links(self):
        print("test_events_links()\n")

        # Assert 'h3' links for each 'h2' on the page
        total_h2_amount = len(self.find_elements(EventsPage.total_h2))
        for x in range(1, total_h2_amount):
            total_h3 = len(self.find_elements('(' + EventsPage.total_h2 + f'[{x}]//..//a)'))
            for y in range(1, total_h3 + 1):
                self.assert_page_loads_successfully('(' + EventsPage.total_h2 + f'[{x}]//..//a)[{y}]')
