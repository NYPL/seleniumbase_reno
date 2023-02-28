from examples.nypl_pages.page_give import GivePage


class Give(GivePage):

    # https://www.nypl.org/give

    def setUp(self):
        super().setUp()
        print("=================================")
        print("\nRUNNING BEFORE EACH TEST")

        # open blog page
        self.open_give_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_give_page(self):
        print("test_give()\n")
        # asserting breadcrumbs and page elements
        self.assert_element(self.home)
        self.assert_element(self.h1)

        # asserting 'Donate' field
        self.assert_element(self.donate)
        self.double_click(self.donate_text_field)
        self.send_keys(self.donate_text_field, "125")  # asserting we can change the default amount
        self.click(self.single_donation)
        self.go_back()
        self.click(self.monthly_donation)
        self.go_back()

        # asserting all h3 links on the page by clicking, using a nested loop.
        # Loop over each h3 section
        for x in range(2, 6):
            # Find the number of child links in the current h3 section
            num_links = len(
                self.find_elements('/html/body/div[1]/div/div[2]/main/div[2]/div/div/div[' + str(x) + ']/ul/li'))
            # Loop over each child link in the current h3 section
            for y in range(1, num_links + 1):
                # Find the link element using the x and y values in the given locator
                self.click(f'/html/body/div[1]/div/div[2]/main/div[2]/div/div/div[{x}]/ul/li[{y}]/div/div[2]/h3/a')
                self.go_back()  # go to the previous page
                self.assert_element(
                    f'/html/body/div[1]/div/div[2]/main/div[2]/div/div/div[{x}]/ul/li[{y}]/div/div[1]/div/div/span/img')

