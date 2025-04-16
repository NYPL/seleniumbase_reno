import pytest

from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_speakout import SpeakoutPage


# @pytest.mark.skip("Only to be run on QA")
@pytest.mark.qa
# @pytest.mark.smoke
class Speakout(NyplUtils):
    # https://www.nypl.org/speakout

    # Set the address index (0-7) depending on which one you want to use
    # 0 = American Samoa
    # 1 = Washington DC
    # 2 = Guam
    # 3 = Marshall Islands
    # 4 = Northern Mariana Islands
    # 5 = Palau
    # 6 = Puerto Rico
    # 7 = U.S. Virgin Islands
    address_index = 6  # <<< CHANGE THIS to test a specific location

    addresses = [
        {
            "street": "1 Ottoville Road",
            "apartment": "",
            "city": "Tafuna",
            "state": "American Samoa",
            "zip": "96799"
        },
        {
            "street": "3206 Warder St NW",
            "apartment": "",
            "city": "Washington",
            "state": "District of Columbia",
            "zip": "20010"
        },
        {
            "street": "120 Birandan Juan C. Tenorio",
            "apartment": "",
            "city": "Yigo",
            "state": "Guam",
            "zip": "96929"
        },
        {
            "street": "House 22, Delap Village",
            "apartment": "",
            "city": "Majuro",
            "state": "Marshall Islands",
            "zip": "96960"
        },
        {
            "street": "317 Chalan Pale Arnold Street",
            "apartment": "",
            "city": "Susupe",
            "state": "Northern Marianas Islands",
            "zip": "96950"
        },
        {
            "street": "House 7, Ngerchemai Hamlet",
            "apartment": "",
            "city": "Koror",
            "state": "Palau",
            "zip": "96940"
        },
        {
            "street": "1509 Calle Luchetti",
            "apartment": "",
            "city": "San Juan",
            "state": "Puerto Rico",
            "zip": "00911"
        },
        {
            "street": "53 Estate Whim",
            "apartment": "",
            "city": "Frederiksted",
            "state": "Virgin Islands",
            "zip": "00840"
        }
    ]

    print("\naddress index: " + str(address_index))

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

    def fill_common_fields(self):
        address = self.addresses[self.address_index]
        self.send_keys(SpeakoutPage.first_name, "Joe")
        self.send_keys(SpeakoutPage.last_name, "Doe")
        self.send_keys(SpeakoutPage.street_address, address["street"])
        if address["apartment"]:
            self.send_keys(SpeakoutPage.apartment, address["apartment"])
        self.send_keys(SpeakoutPage.city, address["city"])
        self.send_keys(SpeakoutPage.state, address["state"])
        self.send_keys(SpeakoutPage.postal, address["zip"])
        self.send_keys(SpeakoutPage.email, "joedoe_nypl@gmail.com")

        print(address)

    # @pytest.mark.skip
    # @pytest.mark.smoke
    def test_speakout(self):
        # https://www.nypl.org/speakout
        print("test_speakout_newyork()\n")

        self.fill_common_fields()
        self.send_keys(SpeakoutPage.favorite_location, "Stephen A. Schwarzman Building")
        # self.assert_element(SpeakoutPage.district_rep)
        # print(self.get_text(SpeakoutPage.district_rep))
        self.click(SpeakoutPage.send_letter)

        self.wait(2)
        print(self.get_current_url())


