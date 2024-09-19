from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_lca import LibraryCardPage

import pytest


@pytest.mark.smoke
@pytest.mark.skip
class LibraryCard(NyplUtils):
    # https://www.nypl.org/library-card/new

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open locations page
        self.open_library_card_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    @pytest.mark.skip(reason="waiting for approval from ILS to create new accounts")
    @pytest.mark.smoke
    def test_library_card_main(self):
        # https://www.nypl.org/library-card/new
        print("test_library_card_main()\n")
        # self.open_library_card_page(category='')

        # asserting the images on the page
        self.image_assertion()

