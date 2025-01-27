from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_posada import PosadaPage


class PosadaTest(NyplUtils):

    # https://www.nypl.org/events/exhibitions/posada

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open posada exhibition page
        self.open_posada_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")

        super().tearDown()

    def test_posada_main(self):
        print("test_posada_main()\n")

        # check images on the page
        self.image_assertion()

        # assert title
        self.assert_title(PosadaPage.posada_title)

        # asserting breadcrumbs
        self.assert_element(PosadaPage.home)  # assert home breadcrumb
        self.assert_element(PosadaPage.events)  # assert events breadcrumb
        self.assert_element(PosadaPage.exhibitions)  # assert exhibitions breadcrumb

        # assert all links on the page
        self.assert_links_valid(PosadaPage.all_links)

        # assert hero by checking if "Posada" text is in hero text in h1 header
        hero_text = self.get_text(PosadaPage.hero)
        self.assert_true("Posada" in hero_text)

    def test_posada_sliders(self):
        print("test_posada_sliders()\n")

        # asserting "Pieces on Display" Slideshow
        self.assert_element(PosadaPage.previous_button_1)
        self.assert_element(PosadaPage.next_button_1)
        slide_show_1_image_amount = len(self.find_elements(PosadaPage.slide_images_1))
        print("Slide show 1 image amount: " + str(slide_show_1_image_amount))  # optional print
        self.assert_true(slide_show_1_image_amount > 1)

        # asserting slider 2- "Installation views | Fotos de la instalación"
        self.assert_element(PosadaPage.previous_button_2)
        self.assert_element(PosadaPage.next_button_2)
        slide_show_2_image_amount = len(self.find_elements(PosadaPage.slide_images_2))
        print("Slide show 2 image amount: " + str(slide_show_2_image_amount))  # optional print
        self.assert_true(slide_show_2_image_amount > 1)
