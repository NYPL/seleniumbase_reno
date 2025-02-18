import pytest

from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_bl_staff_picks import StaffPicksPage
import random


class StaffPicks(NyplUtils):

    # https://www.nypl.org/books-more/recommendations/staff-picks/adults
    # https://www.nypl.org/books-more/recommendations/staff-picks/teens
    # https://www.nypl.org/books-more/recommendations/staff-picks/kids

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open book lists page
        # self.open_best_books_page()  # opening URLs from within the tests itself

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")

        super().tearDown()

    def test_staff_picks_adults(self):
        # https://www.nypl.org/books-more/recommendations/staff-picks/adults
        print('test_staff_picks_adults()\n')
        self.open_staff_picks_page(category='adults')

        # assert breadcrumbs and page elements
        self.assert_element(StaffPicksPage.home)
        self.assert_element(StaffPicksPage.books_and_more)
        self.assert_element(StaffPicksPage.recommendations)
        self.assert_element(StaffPicksPage.adults_tab)
        self.assert_element(StaffPicksPage.teens_tab)
        self.assert_element(StaffPicksPage.kids_tab)

        # assert images on the page
        self.image_assertion()

        # assert all links on the page
        self.assert_links_valid(StaffPicksPage.all_links)

        left_filter_length = len(self.find_elements(StaffPicksPage.left_side_filter))
        # optional print of the length of left side filter, 14 as of June 2022
        print("left side filter length is " + str(left_filter_length))
        # assert that filter is greater than wanted amount, 1 for now
        self.assert_true(left_filter_length > 1, "left side filter amount is not greater than given amount")

        # asserting left side filter content
        for x in range(1, left_filter_length + 1):
            filter_text = self.get_text(StaffPicksPage.left_side_filter + "[" + str(x) + "]/span")
            self.click(StaffPicksPage.left_side_filter + "[" + str(x) + "]")
            self.wait(1)
            result_text = self.get_text(StaffPicksPage.filter_results)
            # assert if the filter text matches the filtered actual text when clicked
            self.assert_true(filter_text in result_text,
                             "clicked " + filter_text + " and " + result_text + " don't match")
            # optional print of filters and results
            # print(filter_text + " =? " + result_text)
            # going back after clicking, receiving and checking the texts
            self.go_back()

        # assert book number in the page equal to the amount in the h3
        book_amount = len(self.find_elements(StaffPicksPage.total_books_found))
        # amount in the h3
        h3_amount = int(self.get_text(StaffPicksPage.h3_book_results).split()[0])
        print("h3 amount is = " + str(h3_amount))  # optional print of the amount seen in h3 element
        # optional print of the number of the displayed books in the page
        print("book amount is = " + str(book_amount))
        self.assert_true(book_amount == h3_amount, "Kids book number and amount in the h3 don't match")

    def test_staff_picks_teens(self):
        # https://www.nypl.org/books-more/recommendations/staff-picks/teens
        print('test_staff_picks_teens()\n')
        self.open_staff_picks_page(category='teens')

        # assert images on the page
        self.image_assertion()

        # assert all links on the page
        self.assert_links_valid(StaffPicksPage.all_links)

        left_filter_length = len(self.find_elements(StaffPicksPage.left_side_filter))
        # optional print of the length of left side filter, 14 as of June 2022
        print("left side filter length is " + str(left_filter_length))
        # assert that filter is greater than wanted amount, 1 for now
        self.assert_true(left_filter_length > 1, "left side filter amount is not greater than given amount")

        # asserting left side filter content
        for x in range(1, left_filter_length + 1):
            filter_text = self.get_text(StaffPicksPage.left_side_filter + "[" + str(x) + "]/span")
            self.click(StaffPicksPage.left_side_filter + "[" + str(x) + "]")
            self.wait(1)
            result_text = self.get_text(StaffPicksPage.filter_results)
            # assert if the filter text matches the filtered actual text when clicked
            self.assert_true(filter_text in result_text,
                             "clicked " + filter_text + " and " + result_text + " don't match")
            # optional print of filters and results
            # print(filter_text + " =? " + result_text)
            # going back after clicking, receiving and checking the texts
            self.go_back()

        # assert book number in the page equal to the amount in the h3
        book_amount = len(self.find_elements(StaffPicksPage.total_books_found))
        # amount in the h3
        h3_amount = int(self.get_text(StaffPicksPage.h3_book_results).split()[0])
        print("h3 amount is = " + str(h3_amount))  # optional print of the amount seen in h3 element
        # optional print of the number of the displayed books in the page
        print("book amount is = " + str(book_amount))
        self.assert_true(book_amount == h3_amount, "Kids book number and amount in the h3 don't match")

    def test_staff_picks_kids(self):
        # https://www.nypl.org/books-more/recommendations/staff-picks/kids
        print('test_staff_picks_kids()\n')
        self.open_staff_picks_page(category='kids')

        # assert images on the page
        self.image_assertion()

        # assert all links on the page
        self.assert_links_valid(StaffPicksPage.all_links)

        left_filter_length = len(self.find_elements(StaffPicksPage.left_side_filter))
        # optional print of the length of left side filter, 14 as of June 2022
        print("left side filter length is " + str(left_filter_length))
        # assert that filter is greater than wanted amount, 1 for now
        self.assert_true(left_filter_length > 1, "left side filter amount is not greater than given amount")

        # asserting left side filter content
        for x in range(1, left_filter_length + 1):
            filter_text = self.get_text(StaffPicksPage.left_side_filter + "[" + str(x) + "]/span")
            self.click(StaffPicksPage.left_side_filter + "[" + str(x) + "]")
            self.wait(1)
            result_text = self.get_text(StaffPicksPage.filter_results)
            # assert if the filter text matches the filtered actual text when clicked
            self.assert_true(filter_text in result_text,
                             "clicked " + filter_text + " and " + result_text + " don't match")
            # optional print of filters and results
            # print(filter_text + " =? " + result_text)
            # going back after clicking, receiving and checking the texts
            self.go_back()

        # assert book number in the page equal to the amount in the h3
        book_amount = len(self.find_elements(StaffPicksPage.total_books_found))
        # amount in the h3
        h3_amount = int(self.get_text(StaffPicksPage.h3_book_results).split()[0])
        print("h3 amount is = " + str(h3_amount))  # optional print of the amount seen in h3 element
        # optional print of the number of the displayed books in the page
        print("book amount is = " + str(book_amount))
        self.assert_true(book_amount == h3_amount, "Kids book number and amount in the h3 don't match")

    def test_staff_picks_seasons(self):
        # https://www.nypl.org/books-more/recommendations/staff-picks/adults
        print('test_staff_picks_seasons()\n')

        # asserting each filter with season selections to confirm the selected season matches the h2 heading on the page

        categories = [
            ('adults', StaffPicksPage.h2_heading_staff_picks_adults),
            ('teens', StaffPicksPage.h2_heading_staff_picks_teens),
            ('kids', StaffPicksPage.h2_heading_staff_picks_kids)
        ]

        for category, h2_heading_locator in categories:
            # Open staff picks page for the category
            self.open_staff_picks_page(category=category)

            # Getting the season and year text
            selected_season = self.get_text(StaffPicksPage.season_dropdown).split()[0]
            selected_year = self.get_text(StaffPicksPage.season_dropdown).split()[1]
            selected_time = selected_season + " " + selected_year
            print(selected_time)  # Optional print

            # Getting the text from the h2 heading
            h2_heading = self.get_text(h2_heading_locator)
            print(h2_heading)  # Optional print

            # Assert the selected time/date from the dropdown for the current category
            self.assert_true(selected_time in h2_heading)

    def test_staff_picks_dropdown(self):
        # https://www.nypl.org/books-more/recommendations/staff-picks/adults
        print('test_staff_picks_dropdown()\n')

        self.open_staff_picks_page(category='adults')

        # asserting dropdowns for each filter (adults/teens/kids)
        # length of the Season dropdown to use in the for loop
        season_length = len(self.find_elements('//*[@id="season"]/option'))
        print(str(season_length) + " total season listed in the dropdown")  # optional print

        # Endpoints that going to be attached to the base URL
        age_list = [
            ('adults', StaffPicksPage.h2_heading_staff_picks_adults),
            ('teens', StaffPicksPage.h2_heading_staff_picks_teens),
            ('kids', StaffPicksPage.h2_heading_staff_picks_kids)
        ]

        # Outer loop to open 3 links in order: adults, teens, kids
        for category, h2_heading_locator in age_list:
            print(" = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
            # Opening the URLs
            self.open_staff_picks_page(category=category)

            # Inner loop to go over every season
            for x in range(1, season_length + 1):
                # Clicking on the Season element
                self.click(StaffPicksPage.season_dropdown)
                self.click(f'//*[@id="season"]/option[{x}]')
                self.click(StaffPicksPage.submit)  # Submitting the selection

                # Getting the season and year text
                selected_season = self.get_text(f'//*[@id="season"]/option[{x}]')
                print("Selected season: " + selected_season)

                # Getting the text from the h2 heading
                h2_heading = self.get_text(h2_heading_locator)
                print("h2 heading: " + h2_heading)  # Optional print

                # Asserting both texts
                self.assert_true(selected_season in h2_heading, "selected season: " + selected_season + ", h2_heading: " + h2_heading)

