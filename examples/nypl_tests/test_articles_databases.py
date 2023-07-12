from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_articles_databases import ArticlesDatabasesPage


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
        first_search_result_text = (self.get_text(ArticlesDatabasesPage.first_result_h3)).lower()  # search result in lowercase
        print(first_search_result_text)  # optional print
        self.assertTrue(keyword in first_search_result_text)

        # assert 'Clear all search terms'
        self.click(ArticlesDatabasesPage.clear_search)
        self.wait(2)

    def test_articles_databases_main_page_elements(self):
        print("test_articles_databases_main_page_elements()\n")
        # asserting h2 heading and its elements
        self.assert_element(ArticlesDatabasesPage.featured_resources)

        # getting the length of the list of elements on the 'Featured Resources'
        featured_list_length = len(self.find_elements('/html/body/div[1]/div/div[2]/main/div[2]/div[1]/div[1]/ul/li'))
        print("featured list length is = " + str(featured_list_length))

        # asserting the h3 links on the list
        for x in range(1, featured_list_length + 1):
            self.hover_and_click(
                '/html/body/div[1]/div/div[2]/main/div[2]/div[1]/div[1]/ul/li[' + str(x) + ']/div/div[2]/h3/a',
                '/html/body/div[1]/div/div[2]/main/div[2]/div[1]/div[1]/ul/li[' + str(x) + ']/div/div[2]/h3/a')
            self.wait(1)

            if self.env == "qa":
                self.open("https://qa-www.nypl.org/research/collections/articles-databases")

            else:
                self.open("https://www.nypl.org/research/collections/articles-databases")

        # asserting 'most popular' h2
        self.assert_element(ArticlesDatabasesPage.most_popular)

        # length of the 'most popular'
        most_pop_length = len(self.find_elements('/html/body/div[1]/div/div[2]/main/div[2]/div[1]/div[2]/ul/li'))
        print("most popular list length is = " + str(most_pop_length))

        for x in range(1, most_pop_length + 1):
            self.click('/html/body/div[1]/div/div[2]/main/div[2]/div[1]/div[2]/ul/li[' + str(x) + ']/div/div/h3/a')
            self.wait(0.5)
            if self.env == "qa":
                self.open("https://qa-www.nypl.org/research/collections/articles-databases")

            else:
                self.open("https://www.nypl.org/research/collections/articles-databases")

        # assert bottom a-z article & databases element
        self.assert_element(ArticlesDatabasesPage.a_z_database)

        # assert the letters/alphabet

        # get the length of the alphabet
        alpha_length = len(self.find_elements('//*[@id="page-container--content-primary"]/div[3]/div[2]/a'))

        # for loop to go over every letter
        for x in range(1, alpha_length + 1):
            if x == 24:  # skipping 'X' letter as it does not have any data
                continue
            self.click('//*[@id="page-container--content-primary"]/div[3]/div[2]/a[' + str(x) + ']')
            self.wait(1)
            if self.env == "qa":
                self.open("https://qa-www.nypl.org/research/collections/articles-databases")

            else:
                self.open("https://www.nypl.org/research/collections/articles-databases")

    def test_articles_databases_subjects_filter(self):
        print("test_articles_databases_subjects_filter()\n")
        # asserting the 'Subjects' filter
        # clicking every filter in the Subjects filter and asserting their lengths
        self.click(ArticlesDatabasesPage.subjects_button)
        subject_filter_length = len(self.find_elements('//*[@id="multiselect-subject"]/div/ul/li'))
        # optional print of the subject filter
        print("subject filter length is = " + str(subject_filter_length))
        self.assert_true(subject_filter_length > 10, "subject filter amount is not greater than 10")
        self.click(ArticlesDatabasesPage.subjects_button)

        # click every filter and apply filters and assert lengths of the sub-filters
        for x in range(1, subject_filter_length + 1):
            self.click(ArticlesDatabasesPage.subjects_button)
            self.click('/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/form/div[2]/div/div/div[1]/div/ul/li[' + str(x) + ']/div/label/span[2]')
            # sub-filter texts
            sub_filter = self.get_text('/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/form/div[2]/div/div/div[1]/div/ul/li[' + str(x) + ']/div/label/span[2]')

            # for loop to assert lengths of the sub-filters, will pass if they are greater than 1
            sub_filter_length = len(
                self.find_elements('//*[@id="multiselect-subject"]/div/ul/li[' + str(x) + ']/ul/li'))
            for y in range(1, sub_filter_length + 1):
                if sub_filter_length <= 0:
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
        # asserting the 3 audience filters, 'adults, kids, teens' by checking if the char count is
        # more than given (1000) amount
        for x in range(1, 4):
            self.click(ArticlesDatabasesPage.audience_button)
            self.click('/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/form/div[2]/div/div/div[2]/div/ul/li[' + str(x) + ']/div/label/span[2]')
            # getting filter text to use it later
            filter_text = self.get_text(
                '/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/form/div[2]/div/div/div[2]/div/ul/li[' + str(x) + ']/div/label/span[2]')
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
        # asserting the 'availability' filter

        # for loop to go over 3 items and click them 1 after each other
        # no need to un-click items since they are radio buttons
        count = 0  # optional counter to see if the for loop is a success
        for x in range(1, 4):
            self.click(ArticlesDatabasesPage.availability_button)
            self.click('/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/form/div[2]/div/div/div[3]/div/ul/li[' + str(x) + ']/div/label/span[2]/span')
            self.click(ArticlesDatabasesPage.apply_availability)
            count += 1
            print(str(count) + "st/nd/rd round")  # optional print of the counter with the loop items
            self.wait(2)  # using wait element to resolve the sync issue

        # asserting the 'clear' button
        self.click(ArticlesDatabasesPage.availability_button)
        self.click(ArticlesDatabasesPage.clear_availability)

    def test_articles_databases_right_side_tab(self):
        print("test_articles_databases_right_side_tab()\n")
        # assert ' more research tools' h2
        self.assert_element(ArticlesDatabasesPage.more_research)

        # assert list underneath 'more research' h2

        # length of the 'tools' list
        tools_list_length = len(self.find_elements('//*[@id="research-tools-menu"]/ul/li'))

        # for loop to iterate the 'more research tools' list
        for x in range(1, tools_list_length + 1):
            self.click('//*[@id="research-tools-menu"]/ul/li[' + str(x) + ']/a')
            self.wait(0.5)
            self.go_back()

        # length of the 'help' list
        help_list_length = len(self.find_elements('//*[@id="research-help-menu"]/ul/li'))

        # for loop to iterate the 'research help' list
        for y in range(1, help_list_length + 1):
            self.click('//*[@id="research-help-menu"]/ul/li[' + str(y) + ']/a')
            self.wait(0.5)
            self.go_back()

    def test_articles_databases_search_page(self):
        print("test_articles_databases_search_page()\n")
        # testing a blank search, no keys entered
        # go to blank search page
        if self.env == "qa":
            self.open("https://qa-www.nypl.org/research/collections/articles-databases/search?q=&page=1")
        else:
            self.open("https://www.nypl.org/research/collections/articles-databases/search?q=&page=1")

        # assert h3 headings elements amount and if they are equal to or greater than 10

        h3_length = len(self.find_elements('/html/body/div[1]/div/div[2]/main/div[2]/div[1]/div/div[2]/div'))
        print("h3 headings count is = " + str(h3_length))  # optional print of the h3 count
        # asserting if the count is equal or greater than 10
        self.assert_true(h3_length >= 10, "h3 headings count is not equal or greater than 10")

        # for loop to iterate over the 10 search results on the page
        for x in range(1, 10):
            self.wait_for_element(
                '/html/body/div[1]/div/div[2]/main/div[2]/div[1]/div/div[2]/div[' + str(x) + ']/div/div[1]/h3/a')
            self.click('/html/body/div[1]/div/div[2]/main/div[2]/div[1]/div/div[2]/div[' + str(x) + ']/div/div[1]/h3/a')
            # go back
            if self.env == "qa":
                self.open("https://qa-www.nypl.org/research/collections/articles-databases/search?q=&page=1")
            else:
                self.open("https://www.nypl.org/research/collections/articles-databases/search?q=&page=1")
            self.wait(1)
