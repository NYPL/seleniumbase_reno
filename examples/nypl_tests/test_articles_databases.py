from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_articles_databases import ArticlesDatabasesPage
import re


class ArticlesDatabasesTest(NyplUtils):
    # https://www.nypl.org/research/collections/articles-databases

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open articles and databases page
        self.open_articles_databases_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_articles_databases_main(self):
        print("test_articles_databases_main_page_elements()\n")

        # asserting h2 headings ('Featured Resources' & "Most Popular")
        self.assert_element(ArticlesDatabasesPage.featured_resources)
        self.assert_element(ArticlesDatabasesPage.most_popular)

        # assert all links on the page
        self.assert_links_valid(ArticlesDatabasesPage.all_links)

    def test_articles_databases_breadcrumbs(self):
        print("test_articles_databases_breadcrumbs()\n")

        # asserting the images on the page
        self.image_assertion()

        # assert title
        self.assert_title(ArticlesDatabasesPage.articles_databases_title)

        # assert breadcrumbs
        self.assert_element(ArticlesDatabasesPage.home)
        self.assert_element(ArticlesDatabasesPage.research)
        self.assert_element(ArticlesDatabasesPage.collections)
        self.assert_element(ArticlesDatabasesPage.articles_databases)
        self.assert_element(ArticlesDatabasesPage.h1_heading)
        self.assert_element(ArticlesDatabasesPage.h1_paragraph)

        # assert 'filter by'
        self.assert_element(ArticlesDatabasesPage.subjects_button)
        self.assert_element(ArticlesDatabasesPage.audience_button)
        self.assert_element(ArticlesDatabasesPage.availability_button)

    def test_articles_databases_search(self):
        print("test_articles_databases_search()\n")

        # asserting search bar
        self.assert_element(ArticlesDatabasesPage.search_bar)

        # asserting the search results with keywords
        # searching for the keyword and asserting it shows up on the first h3 result
        keyword = 'books'.lower()  # keyword in lowercase
        print(keyword)  # optional print
        self.send_keys(ArticlesDatabasesPage.search_bar, keyword)  # searching for keyword
        self.click(ArticlesDatabasesPage.submit_button)  # submitting the keyword
        first_search_result_text = (
            self.get_text(ArticlesDatabasesPage.first_result_h3)).lower()  # search result in lowercase
        print(first_search_result_text)  # optional print
        # asserting the search results with the above keyword
        self.assertTrue(keyword in first_search_result_text)

        # asserting the result number > 0
        search_result_text = self.get_text(ArticlesDatabasesPage.search_result)
        # print(search_result_text)  # optional print
        # finding the result with regex
        search_result_number = int(re.findall(r'(\d+)', search_result_text)[1])
        # print(search_result_number)  # optional print
        # asserting the result number is > 0
        self.assert_true(search_result_number > 0, "actual result is not greater than 0")

        # assert 'Clear all search terms' button by clicking
        self.click(ArticlesDatabasesPage.clear_search)
        self.wait(2)

    def test_articles_databases_pagination(self):
        print("test_articles_databases_pagination()\n")

        # assert each letters/alphabet can be clicked and there is no error on the next page using a for loop
        for x in range(2, 28):
            if x == 24:  # skipping 'X' letter as it is not clickable
                continue
            self.click(ArticlesDatabasesPage.alphabet_pagination + f'[{x}]')
            # print(x)  # optional print of the alphabet element
            self.wait(1)

    def test_articles_databases_subjects_filter(self):
        print("test_articles_databases_subjects_filter()\n")

        # asserting the 'Subjects' filter
        # clicking every filter in the Subjects filter and asserting their lengths
        self.click(ArticlesDatabasesPage.subjects_button)
        subject_filter_length = len(self.find_elements('//*[@id="multiselect-subject"]/div/ul/li'))
        # assert subject filter amount > 10
        print("subject filter length is = " + str(subject_filter_length))
        self.assert_true(subject_filter_length > 10, "subject filter amount is not greater than 10")
        self.click(ArticlesDatabasesPage.subjects_button)

        # click every filter and apply filters and assert lengths of the sub-filters with a for loop
        for x in range(1, subject_filter_length + 1):
            self.click(ArticlesDatabasesPage.subjects_button)
            self.click(f'//*[@id="multiselect-subject"]/div/ul/li[{x}]')
            # sub-filter texts
            sub_filter = self.get_text(f'//*[@id="multiselect-subject"]/div/ul/li[{x}]')

            # for loop to assert lengths of the sub-filters, will pass if they are greater than 1
            sub_filter_length = len(
                self.find_elements('//*[@id="multiselect-subject"]/div/ul/li[' + str(x) + ']/ul/li'))
            for y in range(1, sub_filter_length + 1):
                if sub_filter_length <= 0:
                    print("sub-filter length is not greater than 1")
                    continue
                else:
                    self.assert_true(sub_filter_length >= 1, "sub-filter length is not greater than 1")
            print(str(sub_filter_length) + " sub-filter for " + sub_filter)

            self.click(ArticlesDatabasesPage.apply_subject)
            self.wait(1)
            # clearing/unchecking filters for the next filter
            self.click(ArticlesDatabasesPage.subjects_button)
            self.click(ArticlesDatabasesPage.clear_subject)

    def test_articles_databases_audience(self):
        print("test_articles_databases_audience()\n")

        # assert the 3 audience filters ('adults, kids, teens'), by checking if the character count on the page is
        # more than given (1000) amount, using a for loop
        for x in range(1, 4):
            self.click(ArticlesDatabasesPage.audience_button)
            self.click(f'//*[@id="multiselect-audience_by_age"]//li[{x}]')
            # getting filter text to use it later
            filter_text = self.get_text(f'//*[@id="multiselect-audience_by_age"]//li[{x}]')
            self.click(ArticlesDatabasesPage.apply_audience)
            self.wait(3)

            # finding the total characters in the page to assert later
            adults_content_char_length = len(self.get_text('//*[@id="page-container--content-primary"]'))
            # optional print of the contents on the clicked page
            # print(self.get_text('//*[@id="page-container--content-primary"]'))
            # optional print of the filter text char length
            print(x)
            print(filter_text + " page total char length is = " + str(adults_content_char_length))
            # asserting the total char count is greater than 1000
            self.wait(2)
            self.assert_true(adults_content_char_length > 1000, "Adults page contains fewer than 1000 characters")

            self.click(ArticlesDatabasesPage.audience_button)
            self.click(ArticlesDatabasesPage.clear_audience)
        print("---------------------------------------------------------------------")

    def test_articles_databases_availability(self):
        print("test_articles_databases_availability()\n")

        # asserting the 'availability' filter by clicking each item and verifying there are no error on the next page

        # for loop to go over 3 items and click them 1 after each other
        count = 0  # optional counter to see if the for loop is a success
        for x in range(1, 4):
            self.click(ArticlesDatabasesPage.availability_button)
            self.click(f'//*[@id="multiselect-availability"]/div/ul/li[{x}]')
            self.click(ArticlesDatabasesPage.apply_availability)
            count += 1
            print(str(count) + "st/nd/rd round")  # optional print of the counter with the loop items
            self.wait(2)  # using wait element to resolve the sync issue

        # asserting the 'clear' button
        self.click(ArticlesDatabasesPage.availability_button)  # click "Availability"
        self.click(ArticlesDatabasesPage.clear_availability)  # click "Clear" button

    def test_articles_databases_right_side_tab(self):
        print("test_articles_databases_right_side_tab()\n")

        # assert ' more research tools' h2
        self.assert_element(ArticlesDatabasesPage.more_research)

        # assert list underneath 'more research' h2
        # length of the 'tools' list
        tools_list_length = len(self.find_elements('//*[@id="research-tools-menu"]//li'))

        # for loop to iterate the 'more research tools' list and verify the pages load without error
        for x in range(1, tools_list_length + 1):
            self.click('//*[@id="research-tools-menu"]//li[' + str(x) + ']/a')
            self.wait(0.5)
            self.go_back()

        # length of the 'help' list
        help_list_length = len(self.find_elements('//*[@id="research-help-menu"]//li'))

        # for loop to iterate the 'research help' list and verify the links load without any error
        for y in range(1, help_list_length + 1):
            self.click('//*[@id="research-help-menu"]//li[' + str(y) + ']/a')
            self.wait(0.5)
            self.go_back()
