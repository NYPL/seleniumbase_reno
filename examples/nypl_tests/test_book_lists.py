# from test.s_base.pages.book_lists_page import BookListsPage
import pytest

from examples.nypl_pages.page_book_lists import BookListsPage


class BookLists(BookListsPage):

    # https://www.nypl.org/books-more/recommendations/125/adults
    # https://www.nypl.org/books-more/recommendations/best-books/adults
    # https://www.nypl.org/books-more/recommendations/staff-picks/adults

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open book lists page
        self.open_book_lists_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")

        super().tearDown()

    def test_125_adults(self):
        # https://www.nypl.org/books-more/recommendations/125/adults
        print('test_125_adults()\n')

        # assert breadcrumbs and page elements
        self.assert_element(self.home)
        self.assert_element(self.books_and_more)
        self.assert_element(self.recommendations)
        self.assert_element(self.hero_header_h1)
        self.assert_element(self.adults)
        self.assert_element(self.teens)
        self.assert_element(self.kids)
        self.assert_element(self.filter_results_below)
        self.assert_element(self.additional_info)
        self.wait(2)
        self.hover_and_click(self.additional_info, self.learn_more)
        self.wait(2)
        self.go_back()

        # assert left side filter number more than given amount
        left_filter_length = len(self.find_elements('//*[@id="block-booklistsappealterms"]/div/nav/ul/li'))
        # optional print of the length of left side filter, 14 as of June 2022
        print("left side filter length is " + str(left_filter_length))
        # assert that filter is greater than wanted amount, 1 for now
        self.assert_true(left_filter_length > 1, "left side filter amount is not greater than given amount")

        # assert clicking every left side filter and
        for x in range(1, left_filter_length + 1):
            filter_text = self.get_text('//*[@id="block-booklistsappealterms"]/div/nav/ul/li[' + str(x) + ']/a/span')
            self.click('//*[@id="block-booklistsappealterms"]/div/nav/ul/li[' + str(x) + ']')
            self.wait(1)
            result_text = self.get_text('//*[@id="filter-notify"]/div')
            # assert if the filter text matches the filtered actual text when clicked
            self.assert_true(filter_text in result_text,
                             "clicked " + filter_text + " and " + result_text + " don't match")
            # optional print of filters and results
            # print(filter_text + " =? " + result_text)
            # going back after clicking, receiving and checking the texts
            self.go_back()

        # assert total book count on the page (125/adults) equal to 125. 125 as of June 2022
        book_amount = len(self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/ul/li'))
        # optional print of the number of the displayed books in the page
        print("book amount is = " + str(book_amount))
        self.assert_true(book_amount == 125, "book amount is not more than expected")

    def test_125_teens(self):
        # https://www.nypl.org/books-more/recommendations/125/teens
        print('test_125_teens\n')

        # asserting teens tab
        self.click(self.teens)
        teens_tab_h1_text = self.get_text(self.hero_header_h1)
        # print(teens_tab_h1_text)
        self.assert_true("Teens" in teens_tab_h1_text, "Teens was not found in the heading")

        # assert left side filter number more than given amount
        left_filter_length = len(self.find_elements('//*[@id="block-booklistsappealterms"]/div/nav/ul/li'))
        # optional print of the length of left side filter, 12 as of June 2022
        print("left side filter length is " + str(left_filter_length))
        # assert that filter is greater than wanted amount, 1 for now
        self.assert_true(left_filter_length > 1, "left side filter amount is not greater than given amount")

        # asserting left side filter amount
        for x in range(1, left_filter_length + 1):
            filter_text = self.get_text('//*[@id="block-booklistsappealterms"]/div/nav/ul/li[' + str(x) + ']/a/span')
            self.click('//*[@id="block-booklistsappealterms"]/div/nav/ul/li[' + str(x) + ']')
            self.wait(1)
            result_text = self.get_text('//*[@id="filter-notify"]/div')
            # assert if the filter text matches the filtered actual text when clicked
            self.assert_true(filter_text in result_text,
                             "clicked " + filter_text + " and " + result_text + " don't match")
            # optional print of filters and results
            # print(filter_text + " =? " + result_text)
            # going back after clicking, receiving and checking the texts
            self.go_back()

        # assert book number in the page equals to 125
        book_amount = len(self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/ul/li'))
        # optional print of the number of the displayed books in the page
        print("book amount is = " + str(book_amount))
        self.assert_true(book_amount == 125, "Teens book number is not 125")

    def test_125_kids(self):
        # https://www.nypl.org/books-more/recommendations/125/kids
        print('test_125_kids()\n')

        # asserting kids tab
        self.click(self.kids)
        kids_tab_h1_text = self.get_text(self.hero_header_h1)
        # print(kids_tab_h1_text)
        self.assert_true("Kids" in kids_tab_h1_text, "Kids was not found in the heading")

        # assert left side filter number more than given amount
        left_filter_length = len(self.find_elements('//*[@id="block-booklistsappealterms"]/div/nav/ul/li'))
        # optional print of the length of left side filter, 17 as of June 2022
        print("left side filter length is " + str(left_filter_length))
        # assert that filter is greater than wanted amount, 1 for now
        self.assert_true(left_filter_length > 1, "left side filter amount is not greater than given amount")

        # asserting left side filter amount
        for x in range(1, left_filter_length + 1):
            filter_text = self.get_text('//*[@id="block-booklistsappealterms"]/div/nav/ul/li[' + str(x) + ']/a/span')
            self.click('//*[@id="block-booklistsappealterms"]/div/nav/ul/li[' + str(x) + ']')
            self.wait(1)
            result_text = self.get_text('//*[@id="filter-notify"]/div')
            # assert if the filter text matches the filtered actual text when clicked
            self.assert_true(filter_text in result_text,
                             "clicked " + filter_text + " and " + result_text + " don't match")
            # optional print of filters and results
            # print(filter_text + " =? " + result_text)
            # going back after clicking, receiving and checking the texts
            self.go_back()

        # assert book number in the page equals to 125
        book_amount = len(self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/ul/li'))
        # optional print of the number of the displayed books in the page
        print("book amount is = " + str(book_amount))
        self.assert_true(book_amount == 125, "Kids book number is not 125")

    def test_best_books_adults(self):
        # https://www.nypl.org/books-more/recommendations/best-books/adults
        print('test_best_books_adults()\n')

        if self.env == 'qa':
            self.open('https://qa-www.nypl.org/books-more/recommendations/best-books/adults')
        else:
            self.open('https://www.nypl.org/books-more/recommendations/best-books/adults')

        # assert breadcrumbs and page elements
        self.assert_element(self.home)
        self.assert_element(self.books_and_more)
        self.assert_element(self.recommendations)
        self.assert_element(self.hero_header_h1)
        self.assert_true("Best Books" in self.get_text(self.hero_header_h1))
        self.assert_element(self.adults)
        self.assert_element(self.teens)
        self.assert_element(self.kids)
        self.assert_element(self.submit)
        self.assert_element(self.filter_results_below)
        self.assert_element(self.additional_info)
        self.wait(1)

        # assert 'Additional Information' Section by clicking all the links
        additional_info_length = len(
            self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/footer/div/div/div/div/p')) - 1
        print("additional info length is = " + str(additional_info_length))

        for x in range(1, additional_info_length + 1):
            additional_info = '//*[@id="block-nypl-emulsify-content"]/div/div/footer/div/div/div/div/p[' + str(
                x) + ']/a'
            self.hover_and_click(additional_info, additional_info)
            self.wait(0.2)
            self.go_back()

        # assert left side filter number more than given amount
        left_filter_length = len(self.find_elements('//*[@id="block-booklistsappealterms"]/div/nav/ul/li'))
        # optional print of the length of left side filter, 10 as of June 2022
        print("left side filter length is " + str(left_filter_length))
        # assert that filter is greater than wanted amount, 1 for now
        self.assert_true(left_filter_length > 1, "left side filter amount is not greater than given amount")

        # asserting left side filter content when it is clicked
        for x in range(1, left_filter_length + 1):
            filter_text = self.get_text('//*[@id="block-booklistsappealterms"]/div/nav/ul/li[' + str(x) + ']/a/span')
            self.click('//*[@id="block-booklistsappealterms"]/div/nav/ul/li[' + str(x) + ']')
            self.wait(1)
            result_text = self.get_text('//*[@id="filter-notify"]/div')
            # assert if the filter text matches the filtered actual text when clicked
            self.assert_true(filter_text in result_text,
                             "clicked " + filter_text + " and " + result_text + " don't match")
            # optional print of filters and results
            # print(filter_text + " =? " + result_text)
            # going back after clicking, receiving and checking the texts
            self.go_back()

        # assert book number in the page equal to the amount in the h3
        book_amount = len(self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/ul/li'))
        # amount in the h3
        h3_amount = int(self.get_text('//*[@id="spbb-list-details--heading--"]').split()[0])
        print("h3 amount is = " + str(h3_amount))  # optional print of the amount seen in h3 element
        # optional print of the number of the displayed books in the page
        print("book amount is = " + str(book_amount))
        self.assert_true(book_amount == h3_amount, "Kids book number and amount in the h3 don't match")

    def test_best_books_teens(self):
        # https://www.nypl.org/books-more/recommendations/best-books/teens
        print('test_best_books_teens()\n')

        if self.env == 'qa':
            self.open('https://qa-www.nypl.org/books-more/recommendations/best-books/teens')
        else:
            self.open('https://www.nypl.org/books-more/recommendations/best-books/teens')

        # assert breadcrumbs and page elements
        self.assert_element(self.home)
        self.assert_element(self.books_and_more)
        self.assert_element(self.recommendations)
        self.assert_element(self.hero_header_h1)
        self.assert_true("Best Books" in self.get_text(self.hero_header_h1))
        self.assert_element(self.adults)
        self.assert_element(self.teens)
        self.assert_element(self.kids)
        self.assert_element(self.submit)
        self.assert_element(self.filter_results_below)
        self.assert_element(self.additional_info)
        self.wait(1)

        # assert 'Additional Information' Section by clicking all the links
        additional_info_length = len(
            self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/footer/div/div/div/div/p')) - 1
        for x in range(1, additional_info_length + 1):
            additional_info = '//*[@id="block-nypl-emulsify-content"]/div/div/footer/div/div/div/div/p[' + str(
                x) + ']/a'
            self.hover_and_click(additional_info, additional_info)
            self.wait(0.2)
            self.go_back()

        # assert left side filter number more than given amount
        left_filter_length = len(self.find_elements('//*[@id="block-booklistsappealterms"]/div/nav/ul/li'))
        # optional print of the length of left side filter, 13 as of June 2022
        print("left side filter length is " + str(left_filter_length))
        # assert that filter is greater than wanted amount, 1 for now
        self.assert_true(left_filter_length > 1, "left side filter amount is not greater than given amount")

        # asserting left side filter amount
        for x in range(1, left_filter_length + 1):
            filter_text = self.get_text('//*[@id="block-booklistsappealterms"]/div/nav/ul/li[' + str(x) + ']/a/span')
            self.click('//*[@id="block-booklistsappealterms"]/div/nav/ul/li[' + str(x) + ']')
            self.wait(1)
            result_text = self.get_text('//*[@id="filter-notify"]/div')
            # assert if the filter text matches the filtered actual text when clicked
            self.assert_true(filter_text in result_text,
                             "clicked " + filter_text + " and " + result_text + " don't match")
            # optional print of filters and results
            print(filter_text + " =? " + result_text)
            # going back after clicking, receiving and checking the texts
            self.go_back()

        # assert book number in the page equal to the amount in the h3
        book_amount = len(self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/ul/li'))
        # amount in the h3
        h3_amount = int(self.get_text('//*[@id="spbb-list-details--heading--"]').split()[0])
        print("h3 amount is = " + str(h3_amount))  # optional print of the amount seen in h3 element
        # optional print of the number of the displayed books in the page
        print("book amount is = " + str(book_amount))
        self.assert_true(book_amount == h3_amount, "Kids book number and amount in the h3 don't match")

    def test_best_books_kids(self):
        # https://www.nypl.org/books-more/recommendations/best-books/kids
        print('test_best_books_kids()\n')

        if self.env == 'qa':
            self.open('https://qa-www.nypl.org/books-more/recommendations/best-books/kids')
        else:
            self.open('https://www.nypl.org/books-more/recommendations/best-books/kids')

        # assert breadcrumbs and page elements
        self.assert_element(self.home)
        self.assert_element(self.books_and_more)
        self.assert_element(self.recommendations)
        self.assert_element(self.hero_header_h1)
        self.assert_true("Best Books" in self.get_text(self.hero_header_h1))
        self.assert_element(self.adults)
        self.assert_element(self.teens)
        self.assert_element(self.kids)
        self.assert_element(self.submit)
        self.assert_element(self.filter_results_below)
        self.assert_element(self.additional_info)
        self.wait(1)

        # assert 'Additional Information' Section by clicking all the links
        additional_info_length = len(
            self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/footer/div/div/div/div/p')) - 1
        for x in range(1, additional_info_length + 1):
            additional_info = '//*[@id="block-nypl-emulsify-content"]/div/div/footer/div/div/div/div/p[' + str(
                x) + ']/a'
            self.hover_and_click(additional_info, additional_info)
            self.wait(0.2)
            self.go_back()

        # assert left side filter number more than given amount
        left_filter_length = len(self.find_elements('//*[@id="block-booklistsappealterms"]/div/nav/ul/li'))
        # optional print of the length of left side filter, 11 as of June 2022
        print("left side filter length is " + str(left_filter_length))
        # assert that filter is greater than wanted amount, 1 for now
        self.assert_true(left_filter_length > 1, "left side filter amount is not greater than given amount")

        # asserting left side filter amount
        for x in range(1, left_filter_length + 1):
            filter_text = self.get_text('//*[@id="block-booklistsappealterms"]/div/nav/ul/li[' + str(x) + ']/a/span')
            self.click('//*[@id="block-booklistsappealterms"]/div/nav/ul/li[' + str(x) + ']')
            self.wait(1)
            result_text = self.get_text('//*[@id="filter-notify"]/div')
            # assert if the filter text matches the filtered actual text when clicked
            self.assert_true(filter_text in result_text,
                             "clicked " + filter_text + " and " + result_text + " don't match")
            # optional print of filters and results
            print(filter_text + " =? " + result_text)
            # going back after clicking, receiving and checking the texts
            self.go_back()

        # assert book number in the page equal to the amount in the h3
        book_amount = len(self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/ul/li'))
        # amount in the h3
        h3_amount = int(self.get_text('//*[@id="spbb-list-details--heading--"]').split()[0])
        print("h3 amount is = " + str(h3_amount))  # optional print of the amount seen in h3 element
        # optional print of the number of the displayed books in the page
        print("book amount is = " + str(book_amount))
        self.assert_true(book_amount == h3_amount, "Kids book number and amount in the h3 don't match")

    def test_best_books_year_dropdown(self):
        # todo: might better to use a for loop to eliminate duplicate statements
        # https://www.nypl.org/books-more/recommendations/best-books/adults
        print('test_best_books_year_dropdown()\n')
        """
        asserting the year in h2 heading matches selected year on the dropdown
        :return:
        """

        if self.env == 'qa':
            self.open('https://qa-www.nypl.org/books-more/recommendations/best-books/adults')
        else:
            self.open('https://www.nypl.org/books-more/recommendations/best-books/adults')

        # todo left here asserting 'h2_heading' with 'selected_year'
        # todo also do this for the other sites e.g.
        # https: // www.nypl.org / books - more / recommendations / staff - picks / adults

        # asserting adults
        if self.env == 'qa':
            self.open('https://qa-www.nypl.org/books-more/recommendations/best-books/adults')
        else:
            self.open(
                'https://www.nypl.org/books-more/recommendations/best-books/adults')  # getting the year from h2 heading
        h2_heading_year = (self.get_text(self.h2_heading_year).split())
        # getting the selected year
        selected_year = self.get_text(self.selected_year)
        # optional printing both years to see
        print(h2_heading_year)
        print(self.get_text(self.selected_year))

        # asserting both years
        self.assert_true(selected_year in h2_heading_year, "selected year was not found in the h2 heading")

        # asserting teens
        if self.env == 'qa':
            self.open('https://qa-www.nypl.org/books-more/recommendations/best-books/teens')
        else:
            self.open('https://www.nypl.org/books-more/recommendations/best-books/teens')
        # getting the year from h2 heading
        h2_heading_year = (self.get_text(self.h2_heading_year).split())
        # getting the selected year
        selected_year = self.get_text(self.selected_year)
        # optional printing both years to see
        print(h2_heading_year)
        print(self.get_text(self.selected_year))

        # asserting both years
        self.assert_true(selected_year in h2_heading_year, "selected year was not found in the h2 heading")

        # asserting kids
        if self.env == 'qa':
            self.open('https://qa-www.nypl.org/books-more/recommendations/best-books/kids')
        else:
            self.open('https://www.nypl.org/books-more/recommendations/best-books/kids')
        # getting the year from h2 heading
        h2_heading_year = (self.get_text(self.h2_heading_year).split())
        # getting the selected year
        selected_year = self.get_text(self.selected_year)
        # optional printing both years to see
        print(h2_heading_year)
        print(self.get_text(self.selected_year))

        # asserting both years
        self.assert_true(selected_year in h2_heading_year, "selected year was not found in the h2 heading")

    def test_staff_picks_adults(self):
        # https://www.nypl.org/books-more/recommendations/staff-picks/adults
        print('test_staff_picks_adults()\n')

        if self.env == 'qa':
            self.open('https://qa-www.nypl.org/books-more/recommendations/staff-picks/adults')
        else:
            self.open('https://www.nypl.org/books-more/recommendations/staff-picks/adults')
        # assert Hero h1 element
        self.assert_element(self.hero_header_h1)
        self.assert_true("Staff Picks" in self.get_text(self.hero_header_h1))

        left_filter_length = len(self.find_elements('//*[@id="block-booklistsappealterms"]/div/nav/ul/li'))
        # optional print of the length of left side filter, 14 as of June 2022
        print("left side filter length is " + str(left_filter_length))
        # assert that filter is greater than wanted amount, 1 for now
        self.assert_true(left_filter_length > 1, "left side filter amount is not greater than given amount")

        # asserting left side filter content when it is clicked
        for x in range(1, left_filter_length + 1):
            filter_text = self.get_text('//*[@id="block-booklistsappealterms"]/div/nav/ul/li[' + str(x) + ']/a/span')
            self.click('//*[@id="block-booklistsappealterms"]/div/nav/ul/li[' + str(x) + ']')
            self.wait(1)
            result_text = self.get_text('//*[@id="filter-notify"]/div')
            # assert if the filter text matches the filtered actual text when clicked
            self.assert_true(filter_text in result_text,
                             "clicked " + filter_text + " and " + result_text + " don't match")
            # optional print of filters and results
            # print(filter_text + " =? " + result_text)
            # going back after clicking, receiving and checking the texts
            self.go_back()

        # assert book number in the page equal to the amount in the h3
        book_amount = len(self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/ul/li'))
        # amount in the h3
        h3_amount = int(self.get_text('//*[@id="spbb-list-details--heading--"]').split()[0])
        print("h3 amount is = " + str(h3_amount))  # optional print of the amount seen in h3 element
        # optional print of the number of the displayed books in the page
        print("book amount is = " + str(book_amount))
        self.assert_true(book_amount == h3_amount, "Kids book number and amount in the h3 don't match")

        # assert 'Additional Information' Section by clicking all the links
        additional_info_length = len(
            self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/footer/div/div/div/div/p')) - 1
        print("additional info length is = " + str(additional_info_length))

        # just for this for loop, x starts from 2 and ends at info length + 2, because the locator on the page
        # starts from the 2nd element, there is no first element [1], such as:
        # //*[@id="block-nypl-emulsify-content"]/div/div/footer/div/div/div/div/p[2]/a
        for x in range(2, additional_info_length + 2):
            additional_info = '//*[@id="block-nypl-emulsify-content"]/div/div/footer/div/div/div/div/p[' + str(
                x) + ']/a'
            self.hover_and_click(additional_info, additional_info)
            self.wait(0.2)
            self.go_back()

    def test_staff_picks_teens(self):
        # https://www.nypl.org/books-more/recommendations/staff-picks/teens
        print('test_staff_picks_teens()\n')

        if self.env == 'qa':
            self.open('https://qa-www.nypl.org/books-more/recommendations/staff-picks/teens')
        else:
            self.open('https://www.nypl.org/books-more/recommendations/staff-picks/teens')
        # assert Hero h1 element
        self.assert_element(self.hero_header_h1)
        self.assert_true("Staff Picks" in self.get_text(self.hero_header_h1))

        left_filter_length = len(self.find_elements('//*[@id="block-booklistsappealterms"]/div/nav/ul/li'))
        # optional print of the length of left side filter, 14 as of June 2022
        print("left side filter length is " + str(left_filter_length))
        # assert that filter is greater than wanted amount, 1 for now
        self.assert_true(left_filter_length > 1, "left side filter amount is not greater than given amount")

        # asserting left side filter content when it is clicked
        for x in range(1, left_filter_length + 1):
            filter_text = self.get_text('//*[@id="block-booklistsappealterms"]/div/nav/ul/li[' + str(x) + ']/a/span')
            self.click('//*[@id="block-booklistsappealterms"]/div/nav/ul/li[' + str(x) + ']')
            result_text = self.get_text('//*[@id="filter-notify"]/div')
            # assert if the filter text matches the filtered actual text when clicked
            self.assert_true(filter_text in result_text,
                             "clicked " + filter_text + " and " + result_text + " don't match")
            # optional print of filters and results
            # print(filter_text + " =? " + result_text)
            # going back after clicking, receiving and checking the texts
            self.go_back()

        # assert book number in the page equal to the amount in the h3
        book_amount = len(self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/ul/li'))
        # amount in the h3
        h3_amount = int(self.get_text('//*[@id="spbb-list-details--heading--"]').split()[0])
        print("h3 amount is = " + str(h3_amount))  # optional print of the amount seen in h3 element
        # optional print of the number of the displayed books in the page
        print("book amount is = " + str(book_amount))
        self.assert_true(book_amount == h3_amount, "Kids book number and amount in the h3 don't match")

        # assert 'Additional Information' Section by clicking all the links
        additional_info_length = len(
            self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/footer/div/div/div/div/p')) - 1
        print("additional info length is = " + str(additional_info_length))

        # just for this for loop, x starts from 2 and ends at info length + 2, because the locator on the page
        # starts from the 2nd element, there is no first element [1], such as:
        # //*[@id="block-nypl-emulsify-content"]/div/div/footer/div/div/div/div/p[2]/a
        for x in range(2, additional_info_length + 2):
            additional_info = '//*[@id="block-nypl-emulsify-content"]/div/div/footer/div/div/div/div/p[' + str(
                x) + ']/a'
            self.hover_and_click(additional_info, additional_info)
            self.wait(0.2)
            self.go_back()

    def test_staff_picks_kids(self):
        # https://www.nypl.org/books-more/recommendations/staff-picks/kids
        print('test_staff_picks_kids()\n')

        if self.env == 'qa':
            self.open('https://qa-www.nypl.org/books-more/recommendations/staff-picks/kids')
        else:
            self.open('https://www.nypl.org/books-more/recommendations/staff-picks/kids')
        # assert Hero h1 element
        self.assert_element(self.hero_header_h1)
        self.assert_true("Staff Picks" in self.get_text(self.hero_header_h1))

        left_filter_length = len(self.find_elements('//*[@id="block-booklistsappealterms"]/div/nav/ul/li'))
        # optional print of the length of left side filter, 14 as of June 2022
        print("left side filter length is " + str(left_filter_length))
        # assert that filter is greater than wanted amount, 1 for now
        self.assert_true(left_filter_length > 1, "left side filter amount is not greater than given amount")

        # asserting left side filter content when it is clicked
        for x in range(1, left_filter_length + 1):
            filter_text = self.get_text('//*[@id="block-booklistsappealterms"]/div/nav/ul/li[' + str(x) + ']/a/span')
            self.click('//*[@id="block-booklistsappealterms"]/div/nav/ul/li[' + str(x) + ']')
            self.wait(1)
            result_text = self.get_text('//*[@id="filter-notify"]/div')
            # assert if the filter text matches the filtered actual text when clicked
            self.assert_true(filter_text in result_text,
                             "clicked " + filter_text + " and " + result_text + " don't match")
            # optional print of filters and results
            # print(filter_text + " =? " + result_text)
            # going back after clicking, receiving and checking the texts
            self.go_back()

        # assert book number in the page equal to the amount in the h3
        book_amount = len(self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/ul/li'))
        # amount in the h3
        h3_amount = int(self.get_text('//*[@id="spbb-list-details--heading--"]').split()[0])
        print("h3 amount is = " + str(h3_amount))  # optional print of the amount seen in h3 element
        # optional print of the number of the displayed books in the page
        print("book amount is = " + str(book_amount))
        self.assert_true(book_amount == h3_amount, "Kids book number and amount in the h3 don't match")

        # assert 'Additional Information' Section by clicking all the links
        additional_info_length = len(
            self.find_elements('//*[@id="block-nypl-emulsify-content"]/div/div/footer/div/div/div/div/p')) - 1
        print("additional info length is = " + str(additional_info_length))

        # just for this for loop, x starts from 2 and ends at info length + 2, because the locator on the page
        # starts from the 2nd element, there is no first element [1], such as:
        # //*[@id="block-nypl-emulsify-content"]/div/div/footer/div/div/div/div/p[2]/a
        for x in range(2, additional_info_length + 2):
            additional_info = '//*[@id="block-nypl-emulsify-content"]/div/div/footer/div/div/div/div/p[' + str(
                x) + ']/a'
            self.hover_and_click(additional_info, additional_info)
            self.wait(0.2)
            self.go_back()

    def test_staff_picks_dropdown(self):
        # todo: might be improved by changing the season and year, submitting and asserting if the
        #  page displaying correct filter
        #  e.g.  switching season to Winter 2020 and verifying h2 displays results for Winter 2020

        print('test_staff_picks_dropdown()\n')

        # asserting adults tab
        if self.env == 'qa':
            self.open('https://qa-www.nypl.org/books-more/recommendations/staff-picks/adults')
        else:
            self.open('https://www.nypl.org/books-more/recommendations/staff-picks/adults')

        # getting the season and year text
        selected_season = self.get_text('//*[@id="season"]').split()[0]
        selected_year = self.get_text('//*[@id="season"]').split()[1]
        selected_time = selected_season + " " + selected_year
        print(selected_time)  # optional print

        # getting the text from the h2 heading
        h2_heading = self.get_text(self.h2_heading_year)
        print(h2_heading)  # optional print

        self.assert_true(selected_time in h2_heading)

        # asserting teens tab
        if self.env == 'qa':
            self.open('https://qa-www.nypl.org/books-more/recommendations/staff-picks/teens')
        else:
            self.open('https://www.nypl.org/books-more/recommendations/staff-picks/teens')

        # getting the season and year text
        selected_season = self.get_text('//*[@id="season"]').split()[0]
        selected_year = self.get_text('//*[@id="season"]').split()[1]
        selected_time = selected_season + " " + selected_year
        print(selected_time)  # optional print

        # getting the text from the h2 heading
        h2_heading = self.get_text(self.h2_heading_year)
        print(h2_heading)  # optional print

        self.assert_true(selected_time in h2_heading)

        # asserting kids tab
        if self.env == 'qa':
            self.open('https://qa-www.nypl.org/books-more/recommendations/staff-picks/kids')
        else:
            self.open('https://www.nypl.org/books-more/recommendations/staff-picks/kids')
        # getting the season and year text
        selected_season = self.get_text('//*[@id="season"]').split()[0]
        selected_year = self.get_text('//*[@id="season"]').split()[1]
        selected_time = selected_season + " " + selected_year
        print(selected_time)  # optional print

        # getting the text from the h2 heading
        h2_heading = self.get_text(self.h2_heading_year)
        print(h2_heading)  # optional print

        self.assert_true(selected_time in h2_heading)

    def test_for_loop_for_dropdowns(self):
        print('test_for_loop_for_dropdowns()\n')

        if self.env == 'qa':
            self.open("https://qa-www.nypl.org/books-more/recommendations/staff-picks/adults")
        else:
            self.open("https://www.nypl.org/books-more/recommendations/staff-picks/adults")
        # length of the Season dropdown to use in the for loop
        season_length = len(self.find_elements('//*[@id="season"]/option'))
        print(str(season_length) + " total season listed in the dropdown")  # optional print

        # base URL
        if self.env == 'qa':
            link = "https://qa-www.nypl.org/books-more/recommendations/staff-picks/"
        else:
            link = "https://www.nypl.org/books-more/recommendations/staff-picks/"

        # end points that going to be attached to the base URL
        adults = "adults"
        teens = "teens"
        kids = "kids"

        age_list = [adults, teens, kids]

        # for loop to open 3 links in order- adults, teens, kids
        for y in range(0, 3):
            # opening the URLs
            self.open(link + age_list[y])

            # clicking Submit button after selection
            self.click('//*[@id="season"]')

            print(" = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
            # for loop to go over every season
            for x in range(1, season_length):
                # clicking on the Season element
                self.click('//*[@id="season"]')
                self.click('//*[@id="season"]/option[' + str(x) + ']')
                self.click(self.submit)  # submitting the selection

                # getting the season and year text
                selected_season = self.get_text('//*[@id="season"]/option[' + str(x) + ']')
                print("Selected season " + selected_season)

                # getting the text from the h2 heading
                h2_heading = self.get_text(self.h2_heading_year)
                print("h2 heading = " + h2_heading)  # optional print

                # asserting both texts
                self.assert_true(selected_season in h2_heading)
