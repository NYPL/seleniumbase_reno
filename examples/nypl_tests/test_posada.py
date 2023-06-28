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
        print("test_posada_page()\n")

        # check images on the page
        self.image_assertion()

        # assert title
        self.assert_title(PosadaPage.posada_title)

        # asserting breadcrumbs
        self.assert_element(PosadaPage.home)  # assert home breadcrumb
        self.assert_element(PosadaPage.events)  # assert events breadcrumb
        self.assert_element(PosadaPage.exhibitions)  # assert exhibitions breadcrumb

        # assert hero by checking if "Posada" text is in hero text in h1 header
        hero_text = self.get_text(PosadaPage.hero)
        self.assert_true("Posada" in hero_text)

    def test_la_catrina(self):
        # asserting 'Explore the Online Exhibition'
        # links are hardcoded, so when the exhibition list changes on the page, these list below needs to be updated
        # the new link texts

        exhibition_links_list = ["la-catrina",
                                 "don-chepito-mariguano",
                                 "la-revolucion",
                                 "iconos-revolucionarios",
                                 "transporte-publico",
                                 "la-fiesta-en-ultratumba"]

        for x in range(1, 7):
            url = f'//*[@class="exhibition-card card"][{x}]'

            print("exh list " + exhibition_links_list[x - 1])

            self.link_assertion(url, exhibition_links_list[x-1])
            print("\n===========================")
