import pytest

from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_speakout import SpeakoutPage


@pytest.mark.qa
class Speakout(NyplUtils):
    # https://www.nypl.org/speakout

    addresses = [
        {
            "label": "American Samoa",
            "street": "1 Ottoville Road",
            "apartment": "",
            "city": "Tafuna",
            "state": "American Samoa",
            "zip": "96799"
        },
        {
            "label": "District of Columbia",
            "street": "3206 Warder St NW",
            "apartment": "",
            "city": "Washington",
            "state": "District of Columbia",
            "zip": "20010"
        },
        {
            "label": "Guam",
            "street": "120 Birandan Juan C. Tenorio",
            "apartment": "",
            "city": "Yigo",
            "state": "Guam",
            "zip": "96929"
        },
        {
            "label": "Marshall Islands",
            "street": "House 22, Delap Village",
            "apartment": "",
            "city": "Majuro",
            "state": "Marshall Islands",
            "zip": "96960"
        },
        {
            "label": "Northern Mariana Islands",
            "street": "317 Chalan Pale Arnold Street",
            "apartment": "",
            "city": "Susupe",
            "state": "Northern Marianas Islands",
            "zip": "96950"
        },
        {
            "label": "Palau",
            "street": "House 7, Ngerchemai Hamlet",
            "apartment": "",
            "city": "Koror",
            "state": "Palau",
            "zip": "96940"
        },
        {
            "label": "Puerto Rico",
            "street": "1509 Calle Luchetti",
            "apartment": "",
            "city": "San Juan",
            "state": "Puerto Rico",
            "zip": "00911"
        },
        {
            "label": "U.S. Virgin Islands",
            "street": "53 Estate Whim",
            "apartment": "",
            "city": "Frederiksted",
            "state": "Virgin Islands",
            "zip": "00840"
        }
    ]

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def fill_common_fields(self, address):
        self.send_keys(SpeakoutPage.first_name, "Joe")
        self.send_keys(SpeakoutPage.last_name, "Doe")
        self.send_keys(SpeakoutPage.street_address, address["street"])
        if address["apartment"]:
            self.send_keys(SpeakoutPage.apartment, address["apartment"])
        self.send_keys(SpeakoutPage.city, address["city"])
        self.send_keys(SpeakoutPage.state, address["state"])
        self.send_keys(SpeakoutPage.postal, address["zip"])
        self.send_keys(SpeakoutPage.email, "joedoe_nypl@gmail.com")
        print(f"→ Using address for: {address['label']}")

    def test_speakout_all_districts(self):
        for address in self.addresses:
            print(f"\n🧪 Testing district: {address['label']}")
            self.open_speakout_page()
            self.fill_common_fields(address)
            self.send_keys(SpeakoutPage.favorite_location, "Stephen A. Schwarzman Building")
            self.click(SpeakoutPage.send_letter)
            self.wait(2)
            print(self.get_current_url())
