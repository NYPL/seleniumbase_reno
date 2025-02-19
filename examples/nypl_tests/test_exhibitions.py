from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_exhibitions import ExhibitionsPage


class Exhibitions(NyplUtils):
    # https://www.nypl.org/events/exhibitions
    # https://www.nypl.org/events/exhibitions/upcoming
    # https://www.nypl.org/events/exhibitions/past
    # https://www.nypl.org/events/exhibitions/archived-exhibition-resources
    # https://www.nypl.org/events/exhibitions/community-showcases
    # https://www.nypl.org/events/exhibitions/online

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open exhibitions page
        # self.open_exhibitions_page()  # opening URLs from within the tests itself

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_exhibitions_main(self):
        # https://www.nypl.org/events/exhibitions
        print("test_exhibitions_main_page_elements()\n")
        self.open_exhibitions_page(category='')

        # assert title
        self.assert_title('Exhibitions | The New York Public Library')

        # asserting the images on the page
        self.image_assertion()

        # assert all links on the page
        self.assert_links_valid(ExhibitionsPage.all_links)

        # assert breadcrumbs and page elements
        self.assert_element(ExhibitionsPage.home)
        self.assert_element(ExhibitionsPage.events)
        self.assert_element(ExhibitionsPage.exhibitions_h1)
        self.assert_element(ExhibitionsPage.current_exhibitions)

        # ------------------------------------------------------------------------------------------------
        # asserting 'See All' elements
        see_all_length = len(self.find_elements(ExhibitionsPage.see_all))
        print("Total 'See All' elements = " + str(see_all_length))  # optional print of the 'See All' links amount
        for x in range(1, see_all_length):
            self.click(f"{ExhibitionsPage.see_all}[{x}]")
            self.go_back()

    def test_exhibitions_upcoming(self):
        # https://www.nypl.org/events/exhibitions/upcoming
        print("test_exhibitions_upcoming()\n")
        self.open_exhibitions_page(category='upcoming')

        # assert title
        self.assert_title('Upcoming Exhibitions | The New York Public Library')

        # asserting the images on the page
        self.image_assertion()

        # assert all links on the page
        self.assert_links_valid(ExhibitionsPage.all_links)

        # assert breadcrumbs and page elements
        self.assert_element(ExhibitionsPage.home)
        self.assert_element(ExhibitionsPage.events)
        self.assert_element(ExhibitionsPage.exhibitions)
        self.assert_element(ExhibitionsPage.upcoming_1)

    def test_exhibitions_past(self):
        # https://www.nypl.org/events/exhibitions/past
        print("test_exhibitions_past()\n")
        self.open_exhibitions_page(category='past')

        # assert title
        self.assert_title('Past Exhibitions | The New York Public Library')

        # asserting the images on the page
        self.image_assertion()

        # assert all links on the page
        self.assert_links_valid(ExhibitionsPage.all_links)

        # assert breadcrumbs and page elements
        self.assert_element(ExhibitionsPage.home)
        self.assert_element(ExhibitionsPage.events)
        self.assert_element(ExhibitionsPage.exhibitions)
        self.assert_element(ExhibitionsPage.past_exhibitions_h1)

        # asserting pagination elements
        self.assert_element(ExhibitionsPage.next_page)

        # asserting the pager links at the bottom of the page
        pager_length = len(self.find_elements(ExhibitionsPage.pagination_list))

        for x in range(1, pager_length):
            self.click(ExhibitionsPage.pagination_list + '[' + str(x) + ']')
            url_text = self.get_current_url()
            print(url_text)  # optional print
            # asserting if the url text contains page=random_number
            print('page = ' + str(x - 1))
            self.assert_true(str(x - 1) in url_text)
            self.open_exhibitions_page(category='past')

    def test_exhibitions_archived_exhibition_resources(self):
        # https://www.nypl.org/events/exhibitions/archived-exhibition-resources
        print("test_exhibitions_archived_exhibition_resources()\n")
        self.open_exhibitions_page(category='archived-exhibition-resources')

        # assert title
        self.assert_title('Archived Exhibition Resources | The New York Public Library')

        # asserting the images on the page
        self.image_assertion()

        # assert all links on the page
        self.assert_links_valid(ExhibitionsPage.all_links)

        # assert breadcrumbs and page elements
        self.assert_element(ExhibitionsPage.home)
        self.assert_element(ExhibitionsPage.events)
        self.assert_element(ExhibitionsPage.exhibitions)
        self.assert_element(ExhibitionsPage.archived_h1)
        self.assert_element(ExhibitionsPage.archived_h2)

        # asserting the pager links at the bottom of the page
        pager_length = len(self.find_elements(ExhibitionsPage.pagination_list))

        for x in range(1, pager_length):
            self.click(ExhibitionsPage.pagination_list + '[' + str(x) + ']')
            url_text = self.get_current_url()
            print(url_text)  # optional print
            # asserting if the url text contains page=random_number
            print('page = ' + str(x - 1))
            self.assert_true(str(x - 1) in url_text)
            self.open_exhibitions_page(category='archived-exhibition-resources')

        # asserting the forward icon > and ellipsis '...'
        self.assert_element(ExhibitionsPage.next_page)

        # asserting right-icon
        self.assert_element(ExhibitionsPage.next_page)

    def test_exhibitions_community_showcases(self):
        # https://www.nypl.org/events/exhibitions/community-showcases
        print("test_exhibitions_community_showcases()\n")
        self.open_exhibitions_page(category='community-showcases')

        # assert title
        self.assert_title('Community Showcases | The New York Public Library')

        # asserting the images on the page
        self.image_assertion()

        # using 'try' and 'except' block since the webpage might have no exhibitions at all
        try:  # if the page does not have any showcases, this 'try' block will take care of the test
            # skip test if there is no current "Community Showcase"
            no_community_showcase_text = self.get_text(ExhibitionsPage.no_community_showcase)
            assertion_text = 'currently have no community showcases'
            if assertion_text in no_community_showcase_text:
                print("No Community Showcases, so nothing to assert.")
        except:  # if there are showcases, this 'except' block will run and assert the elements
            # assert breadcrumbs and page elements
            self.assert_element(ExhibitionsPage.home)
            self.assert_element(ExhibitionsPage.events)
            self.assert_element(ExhibitionsPage.exhibitions)
            self.assert_element(ExhibitionsPage.community_h1)

            # assert all links on the page
            self.assert_links_valid(ExhibitionsPage.all_links)

            # asserting the pager links at the bottom of the page
            pager_length = len(self.find_elements(ExhibitionsPage.pagination_list))

            for x in range(1, pager_length):
                self.click(ExhibitionsPage.pagination_list + '[' + str(x) + ']')
                url_text = self.get_current_url()
                print(url_text)  # optional print
                # asserting if the url text contains page=random_number
                print('page = ' + str(x - 1))
                self.assert_true(str(x - 1) in url_text)
                self.open_exhibitions_page(category='community-showcases')

    def test_exhibitions_online(self):
        # https://www.nypl.org/events/exhibitions/online
        print("test_exhibitions_online()\n")
        self.open_exhibitions_page(category='online')

        # assert title
        self.assert_title('Online Exhibitions | The New York Public Library')

        # asserting the images on the page
        self.image_assertion()

        # assert all links on the page
        self.assert_links_valid(ExhibitionsPage.all_links)

        # assert breadcrumbs and page elements
        self.assert_element(ExhibitionsPage.home)
        self.assert_element(ExhibitionsPage.events)
        self.assert_element(ExhibitionsPage.exhibitions)
        self.assert_element(ExhibitionsPage.online_h1)

        # asserting the pager links at the bottom of the page
        pager_length = len(self.find_elements(ExhibitionsPage.pagination_list))

        for x in range(1, pager_length):
            self.click(ExhibitionsPage.pagination_list + '[' + str(x) + ']')
            url_text = self.get_current_url()
            print(url_text)  # optional print
            # asserting if the url text contains page=random_number
            print('page = ' + str(x - 1))
            self.assert_true(str(x - 1) in url_text)
            self.open_exhibitions_page(category='online')
