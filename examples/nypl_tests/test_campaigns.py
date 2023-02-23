from examples.nypl_pages.page_campaigns import CampaignsPage


class Campaigns(CampaignsPage):

    # https://www.nypl.org/125
    # https://www.nypl.org/125/timeline
    # https://www.nypl.org/125/topcheckouts

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open campaigns page
        self.open_campaigns_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_125(self):
        # https://www.nypl.org/125
        print("test_125()\n")

        # assert home element
        self.assert_element(self.home)

        # assert hero
        self.assert_element(self.main_card)

        # assert rest of the cards in range (1, card_length)
        card_length = len(self.find_elements('/html/body/div[1]/div/main/div[2]/div/div/div/div/div'))

        for x in range(1, card_length + 1):
            # assert each card in the page, there is 16 cards as of June 2022
            card_xpath = '/html/body/div[1]/div/main/div[2]/div/div/div/div/div[' + str(x) + ']'
            self.assert_element(card_xpath)
            # optional hovering over the element for visibility and printing
            # self.hover_on_element(card_xpath)
            # print("assert number = " + str(x))

        print("\n")

        # asserting the slides in 'The New York Public Library Through the Years'
        for y in range(1, 11):
            print(self.get_image_url(
                '/html/body/div[1]/div/main/div[2]/div/div/div/div/div[14]/div[3]/div/div/div/div[' + str(
                    y) + ']/div/li/button/img'))

        slide_length = len(
            self.find_elements('/html/body/div[1]/div/main/div[2]/div/div/div/div/div[14]/div[3]/div/div/div/div'))

        # assert slide number more than 9, currently 28 (10 as unique) as of June 2022
        print("\nSlide amount is " + str(slide_length))
        self.assert_true(slide_length > 9, "Slide length is less than desired amount")

    def test_125_timeline(self):
        # https://www.nypl.org/125/timeline
        print("test_125_timeline()\n")

        if self.env == 'qa':
            self.open('https://qa-www.nypl.org/125/timeline')
        else:
            self.open('https://www.nypl.org/125/timeline')

        # assert breadcrumbs
        self.assert_element(self._125_years)
        self.assert_element(self.timeline_h1)

        # asserting cards in the page, 45 of them as of June 2022
        cards_length = len(self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/div'))
        self.assert_true(cards_length >= 45, "Cards amount in the page is less than " + str(cards_length))

        # assert main h2 heading and main paragraph
        self.assert_element('//*[@id="featured-card--heading--1579"]')
        self.assert_element('//*[@id="block-nypl-emulsify-content"]/div/div/div[1]/ul/li/div[1]/div/p')

        # asserting rest of the 44 h2 and paragraphs, starting from the 2nd one
        for x in range(2, cards_length + 1):
            # first two hovering on and printing h2's are optional
            # self.hover_on_element('//*[@id="block-nypl-emulsify-content"]/div/div/div[' + str(x) + ']/div/div/p')
            # print(self.get_text('/html/body/div[1]/div/main/div[2]/div/div/div/div/div[' + str(x) + ']/div/h2'))
            self.assert_element('/html/body/div[1]/div/main/div[2]/div/div/div/div/div[' + str(x) + ']/div/h2')
            self.assert_element('//*[@id="block-nypl-emulsify-content"]/div/div/div[' + str(x) + ']/div/div/p')

        # asserting images, 19 images as of June2022
        images_count = len(self.find_elements('//img'))
        self.assert_true(images_count > 15, "images on the page are less than given amount")

    def test_125_topCheckouts(self):
        # https://www.nypl.org/125/topcheckouts
        print("test_125_topCheckouts()\n")

        if self.env == 'qa':
            self.open('https://qa-www.nypl.org/125/topcheckouts')
        else:
            self.open('https://www.nypl.org/125/topcheckouts')

        # assert breadcrumbs
        self.assert_element(self._125_years)
        self.assert_element(self.checkouts_h1)
        self.assert_elements(self.topcheckout_paragraphs)

        # asserting top 3 card grid '125 books we love' ...
        # length of the grid to use in 'for loop' for dynamic purposes in future
        grid_length = len(self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/ul/li'))
        for x in range(1, grid_length + 1):
            # asserting the Grids elements' text
            self.assert_element(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/ul/li[' + str(x) + ']/div[1]/div/p[1]')
            # asserting by clicking the link on the top 3 grid h2 elements
            self.hover_and_click(
                '/html/body/div[1]/div/main/div[2]/div/div/div/div/div[2]/ul/li[' + str(x) + ']/div[1]/h2/a',
                '/html/body/div[1]/div/main/div[2]/div/div/div/div/div[2]/ul/li[' + str(x) + ']/div[1]/h2/a')
            self.wait(0.2)
            self.go_back()
            # asserting same 3 elements with their image-card links
            self.hover_and_click(
                '/html/body/div[1]/div/main/div[2]/div/div/div/div/div[2]/ul/li[' + str(x) + ']/div[2]',
                '/html/body/div[1]/div/main/div[2]/div/div/div/div/div[2]/ul/li[' + str(x) + ']/div[2]')
            self.wait(0.2)
            self.go_back()
            # asserting 'Explore the List' elements
            self.hover_and_click(
                '//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/ul/li[' + str(x) + ']/div[1]/a',
                '//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/ul/li[' + str(x) + ']/div[1]/a')
            self.wait(0.2)
            self.go_back()
            # asserting grid elements in a nested for loop
            for y in range(1, 3):
                self.assert_element(
                    '//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/ul/li[' + str(x) + ']/div[' + str(y) + ']')
                self.hover_on_element(
                    '//*[@id="block-nypl-emulsify-content"]/div/div/div[2]/ul/li[' + str(x) + ']/div[' + str(y) + ']')

        # asserting h2 header 'Honorable Mention'
        self.assert_element('//*[@id="block-nypl-emulsify-content"]/div/div/div[3]/div/h2')
        # asserting the whole 'Honorable mention' div
        self.assert_element('//*[@id="block-nypl-emulsify-content"]/div/div/div[3]')
        # asserting landing page text- 'A note on Methodology'
        self.assert_element('//*[@id="block-nypl-emulsify-content"]/div/div/div[4]/div/div')
        # asserting card-grids at the bottom of the page
        self.assert_elements('//*[@id="block-nypl-emulsify-content"]/div/div/div[5]/ul/li[1]',
                             '//*[@id="block-nypl-emulsify-content"]/div/div/div[5]/ul/li[2]')

    def test_125_topCheckouts_top10Books(self):
        # https://www.nypl.org/125/topcheckouts
        print("test_125_topCheckouts_top100Books()\n")

        if self.env == 'qa':
            self.open('https://qa-www.nypl.org/125/topcheckouts')
        else:
            self.open('https://www.nypl.org/125/topcheckouts')

        # asserting the 10 books/elements
        # asserting the top checkout number is equal to 10
        top_checkout_number = len(self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/ol/li'))
        self.assert_true(top_checkout_number == 10, "top checkout number is not equal to 10")

        # asserting each book by clicking
        for y in range(1, top_checkout_number + 1):
            self.assert_element(
                '//*[@id="block-nypl-emulsify-content"]/div/div/ol/li[' + str(y) + ']/div[1]/div[2]/div[3]/a[1]')
            self.hover_and_click('//*[@id="block-nypl-emulsify-content"]/div/div/ol/li[' + str(y) + ']/div[1]/div['
                                                                                                    '2]/div[3]/a[1]',
                                 '//*[@id="block-nypl-emulsify-content"]/div/div/ol/li[' + str(y) + ']/div[1]/div['
                                                                                                    '2]/div[3]/a[1]')

            print("Request Book for the book " + str(y) + " is verified")
            self.go_back()
            if not self.is_element_visible(
                    '//*[@id="block-nypl-emulsify-content"]/div/div/ol/li[' + str(y) + ']/div[1]/div[2]/div[3]/a[2]'):
                print("Request E-Book element is not present on book " + str(y))
                print("\n-----------------------------------------------------\n")
                continue
            else:
                self.assert_element('//*[@id="block-nypl-emulsify-content"]/div/div/ol/li[' + str(y) + ']/div[1]/div['
                                                                                                       '2]/div[3]/a['
                                                                                                       '2]')
                self.hover_and_click(
                    '//*[@id="block-nypl-emulsify-content"]/div/div/ol/li[' + str(y) + ']/div[1]/div[2]/div[3]/a[2]',
                    '//*[@id="block-nypl-emulsify-content"]/div/div/ol/li[' + str(y) + ']/div[1]/div[2]/div[3]/a[2]')
                print("Request E-Book for the book " + str(y) + " is verified")
                self.go_back()
                print("\n-----------------------------------------------------\n")
