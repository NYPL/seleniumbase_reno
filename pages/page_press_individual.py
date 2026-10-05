from seleniumbase import BaseCase


class PressIndividualPage(BaseCase):
    home = '(//*[contains(text(), "Home")])[1]'
    press_releases = '//*[contains(text(), "Press Releases")]'

    home_title = 'Actress, Comedian & TV Host Sherri Shepherd and Chef & Restaurateur Melba Wilson Lead Celebrity ' \
                 'Story Time for NYC School Children at New York Public Library’s Schwarzman Building | The New York ' \
                 'Public Library'

    photos = '//*[contains(text(), "Photos")]//a'

    def open_press_individual_page(self):
        prod_url = "https://www.nypl.org/press/actress-comedian-tv-host-sherri-shepherd-and-chef-restaurateur-melba" \
                   "-wilson-lead-celebrity"
        qa_url = "https://qa-www.nypl.org/press/actress-comedian-tv-host-sherri-shepherd-and-chef-restaurateur-melba" \
                 "-wilson-lead-celebrity"

        if self.env == "qa":
            print("Running on QA Env")
            self.open(qa_url)

        else:
            print("Running on Production Env")
            self.open(prod_url)
