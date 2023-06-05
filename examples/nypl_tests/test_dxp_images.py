import pytest
import requests

from examples.nypl_utility.utility import NyplUtils


class FrontendImagesAndLinks(NyplUtils):

    # this class intended to assert all the front end DXP pages' images and links

    # image assertion
    @pytest.mark.skip(reason="skipping for now")
    def test_dxp_pages(self):
        links = [
            "https://www.nypl.org/",
            "https://www.nypl.org/give",
            "https://www.nypl.org/research",
            "https://www.nypl.org/research/support",
            "https://www.nypl.org/locations",
            "https://www.nypl.org/locations/schwarzman",
            "https://www.nypl.org/locations/snfl",
            "https://www.nypl.org/locations/snfl/teen",
            "https://www.nypl.org/locations/lpa/billy-rose-theatre-division",
            "https://www.nypl.org/locations/request-visit",
            "https://www.nypl.org/events/exhibitions",
            "https://www.nypl.org/events/exhibitions/posada",
            "https://www.nypl.org/spotlight/world-literature-festival",
            "https://www.nypl.org/books-more/recommendations/staff-picks/teens",
            "https://www.nypl.org/research/collections/articles-databases",
            "https://www.nypl.org/research/collections/articles-databases/search",
            "https://www.nypl.org/research/collections/articles-databases/17th-18th-century-burney-collection-newspapers",
            "https://www.nypl.org/research/collections/articles-databases/featured/homework-help",
            "https://www.nypl.org/research/collections/articles-databases/search?alpha=L",
            "https://www.nypl.org/blog",
            "https://www.nypl.org/blog/all",
            "https://www.nypl.org/blog/channels",
            "https://www.nypl.org/blog/2022/09/22/reading-list-climate-week-nyc",
            "https://www.nypl.org/press",
            "https://www.nypl.org/press/actress-comedian-tv-host-sherri-shepherd-and-chef-restaurateur-melba-wilson-lead-celebrity"
        ]

        for link in links:
            self.open(link)
            self.image_assertion()

    # link assertion
    @pytest.mark.skip(reason="skipping for now")
    def test_links(self):

        links = [
            "https://www.nypl.org/",
            "https://www.nypl.org/give",
            "https://www.nypl.org/research",
            "https://www.nypl.org/research/support",
            "https://www.nypl.org/locations",
            "https://www.nypl.org/locations/schwarzman",
            "https://www.nypl.org/locations/snfl",
            "https://www.nypl.org/locations/snfl/teen",
            "https://www.nypl.org/locations/lpa/billy-rose-theatre-division",
            "https://www.nypl.org/locations/request-visit",
            "https://www.nypl.org/events/exhibitions",
            "https://www.nypl.org/events/exhibitions/posada",
            "https://www.nypl.org/spotlight/world-literature-festival",
            "https://www.nypl.org/books-more/recommendations/staff-picks/teens",
            "https://www.nypl.org/research/collections/articles-databases",
            "https://www.nypl.org/research/collections/articles-databases/search",
            "https://www.nypl.org/research/collections/articles-databases/17th-18th-century-burney-collection-newspapers",
            "https://www.nypl.org/research/collections/articles-databases/featured/homework-help",
            "https://www.nypl.org/research/collections/articles-databases/search?alpha=L",
            "https://www.nypl.org/blog",
            "https://www.nypl.org/blog/all",
            "https://www.nypl.org/blog/channels",
            "https://www.nypl.org/blog/2022/09/22/reading-list-climate-week-nyc",
            "https://www.nypl.org/press",
            "https://www.nypl.org/press/actress-comedian-tv-host-sherri-shepherd-and-chef-restaurateur-melba-wilson-lead-celebrity"
        ]

        for x in links:
            self.open(x)
            links_in_page = self.find_elements("a")
            num_links = len(links_in_page)
            print("\n" + x)
            print("number of links = " + str(num_links))
            for y in links_in_page:
                href = y.get_attribute("href")
                if href.startswith("http"):
                    response = requests.get(href)
                    assert response.status_code < 400, f"{href} returned a status code of {response.status_code}"
