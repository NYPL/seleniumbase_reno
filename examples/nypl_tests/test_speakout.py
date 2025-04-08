import pytest

from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_speakout import SpeakoutPage


#@pytest.mark.skip("Only to be run on QA")
@pytest.mark.qa
@pytest.mark.smoke
class LibraryCard(NyplUtils):
    # https://www.nypl.org/speakout

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open locations page
        self.open_speakout_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    # @pytest.mark.skip
    # @pytest.mark.smoke
    def test_speakout_newyork(self):
        # https://www.nypl.org/speakout
        print("test_speakout_form()\n")

        # fill out personal info and assert all the fields
        self.send_keys(SpeakoutPage.first_name, "Joe")
        self.send_keys(SpeakoutPage.last_name, "Doe")
        self.send_keys(SpeakoutPage.street_address, "451 e 22nd street")
        self.send_keys(SpeakoutPage.apartment, "3F")
        self.send_keys(SpeakoutPage.city, "Brooklyn")
        self.send_keys(SpeakoutPage.state, "New York")
        self.send_keys(SpeakoutPage.postal, "11226")
        self.send_keys(SpeakoutPage.email, "joedoe_nypl@gmail.com")

        self.send_keys(SpeakoutPage.favorite_location, "Stephen A. Schwarzman Building")
        self.assert_element(SpeakoutPage.district_rep)  # assert the district rep text populated after address filled in
        print(self.get_text(SpeakoutPage.district_rep))  # optional print of the District and Council Members
        self.click(SpeakoutPage.send_letter)

        self.wait(2)
        print(self.get_current_url())

    # @pytest.mark.skip
    def test_speakout_non_newyork(self):
        # https://www.nypl.org/speakout
        print("test_speakout_form()\n")

        # fill out personal info and assert all the fields
        self.send_keys(SpeakoutPage.first_name, "Joe")
        self.send_keys(SpeakoutPage.last_name, "Doe")
        self.send_keys(SpeakoutPage.street_address, "60 Edgewater Road")
        # self.send_keys(SpeakoutPage.apartment, "3F")
        self.send_keys(SpeakoutPage.city, "Cliffside Park")
        self.send_keys(SpeakoutPage.state, "New Jersey")
        self.send_keys(SpeakoutPage.postal, "07086")
        self.send_keys(SpeakoutPage.email, "joedoe_nypl@gmail.com")

        self.send_keys(SpeakoutPage.favorite_location, "Eastchester Library")
        self.assert_element(SpeakoutPage.district_rep)  # assert the district rep text populated after address filled in
        print(self.get_text(SpeakoutPage.district_rep))  # optional print of the District and Council Members
        self.click(SpeakoutPage.send_letter)

        self.wait(2)
        print(self.get_current_url())
