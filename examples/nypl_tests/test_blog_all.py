from examples.nypl_pages.page_blog_all import BlogAllPage
import random


class BlogAllTests(BlogAllPage):

    # https://www.nypl.org/blog/all

    def setUp(self):
        super().setUp()
        print("=================================")
        print("\nRUNNING BEFORE EACH TEST")

        # open blog/all page
        self.open_blog_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_page_elements(self):
        print("test_page_elements()\n")
        # assert Explore By:
        self.assert_element(BlogAllPage.explore_by)

    def test_channels(self):
        print("test_channels()\n")
        # asserting 'Channels' tab

        # asserting channel categories
        # creating a list for Channel Filters
        li = ["asian_american", "biography", "black_culture", "book_lists", "comics_graphic", "digital_collections",
              "doc_chat", "early_literacy", "espanol_spanish", "for_kids", "for_teachers", "for_teens",
              "francais_french", "hispanic_latinx", "horror", "lgbtq+", "library_stories", "library_talks",
              "mysteries_crime", "nonfiction", "poetry", "popular_culture", "research_at_nypl", "romance",
              "science_fiction", "the_librarian", "women's_history", "work_cited", "chinese_language"]
        # keywords for the Channel Filters, we use these keywords to look in the every link text
        keywords = ["Asian", "Memoir", "Black", "Book Lists", "Comic", "Digital", "Doc", "Early Literacy", "de",
                    'for kids', 'for teachers', 'for teens', 'de', 'Hispanic', 'Horror', 'LGBTQ', 'Library Stories',
                    'Library Talks', 'Mysteries', 'Nonfiction', 'Poetry', 'Popular Culture', 'Research at nypl',
                    'Romance', 'Science Fiction', 'Librarian', 'Women', 'Work/Cited', 'Chinese']
        # assertion for first 6 channels
        for x in range(1, 6):
            self.click(BlogAllPage.channels)
            self.click('/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[1]/div/ul/li[' + str(
                x) + ']/div/label/span[1]')
            self.click(BlogAllPage.apply_channel)
            self.wait(1)

            search_results = self.get_text('//*[@id="search-results-details"]')

            result = search_results.split()[2]
            print(result + " results for " + keywords[x])
            self.assert_true(int(result) >= 5)

            self.wait(1)
            self.click(BlogAllPage.clear_all_search_terms)

    def test_subjects(self):
        print("test_subjects()\n")
        """
        this method assert the child elements of the subject button and if they are clickable
        """

        # assert subjects button
        self.click(BlogAllPage.subjects)
        self.assert_element(BlogAllPage.subjects)

        # length of the subjects children
        children_subject = len(
            self.find_elements('/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[2]/div/ul/li'))
        self.click(BlogAllPage.subjects)

        print("Total child elements = " + str(children_subject))

        # asserting that we can click each child element
        for x in range(1, children_subject + 1):
            #
            self.click(BlogAllPage.subjects)
            self.click('/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[2]/div/ul/li[' + str(
                x) + ']/div/label/span[2]')
            self.click(BlogAllPage.apply_subject)
            self.assert_true(BlogAllPage.search_results)
            print("Child element = " + str(x))
            self.click(BlogAllPage.clear_all_search_terms)

    def test_libraries(self):
        print("test_libraries()\n")
        """this method randomly takes 10 elements (can be changed) and asserts the child elements of the library 
        button and if they are clickable """

        # assert libraries button
        self.assert_element(BlogAllPage.libraries)

        # length of the libraries children
        self.click(BlogAllPage.libraries)
        children_amount = len(
            self.find_elements('/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[3]/div/ul/li'))
        self.click(BlogAllPage.libraries)

        print("Total child elements = " + str(children_amount))

        # creating a list of random 15 elements for the loop
        num_random_elements = 10
        elements = list(range(1, children_amount + 1))
        random_elements = random.sample(elements, num_random_elements)

        # asserting (randomly) that we can click each child element
        for x in random_elements:
            self.click(BlogAllPage.libraries)
            self.click('/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[3]/div/ul/li[' + str(
                x) + ']/div/label/span[2]')
            self.click(BlogAllPage.apply_library)
            self.assert_true(BlogAllPage.search_results)
            print("Child element " + str(x))
            self.click(BlogAllPage.clear_all_search_terms)

    def test_divisions(self):
        print("test_divisions()\n")
        """this method randomly takes 10 elements (can be changed) and asserts the child elements of the divisions 
        button and if they are clickable """

        # assert divisions button
        self.assert_element(BlogAllPage.divisions)

        # length of the divisions children
        self.click(BlogAllPage.divisions)
        children_amount = len(
            self.find_elements('/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[4]/div/ul/li'))
        self.click(BlogAllPage.divisions)

        print("Total child elements = " + str(children_amount))

        num_random_elements = 10
        elements = list(range(1, children_amount + 1))
        random_elements = random.sample(elements, num_random_elements)

        # asserting that we can click each child element
        for x in random_elements:
            #
            self.click(BlogAllPage.divisions)
            self.click('/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[4]/div/ul/li[' + str(
                x) + ']/div/label/span[2]')
            self.click(BlogAllPage.apply_division)
            self.assert_true(BlogAllPage.search_results)
            print("Child element " + str(x))
            self.click(BlogAllPage.clear_all_search_terms)

        print("\n========================================\n")

    def test_audience(self):
        print("test_audience()\n")
        # assert Audience button
        self.assert_element(BlogAllPage.audience)

        # click 'Audience' tab
        self.click(BlogAllPage.audience)

        # click 'Adults' filter
        self.click(BlogAllPage.adults)
        self.click(BlogAllPage.apply_audience)
        self.wait(1)
        # wait for the next page, see the results (this is for sync issues)
        self.wait_for_element(BlogAllPage.search_results)
        # url text for the filter
        url_text = self.get_current_url()
        print(self.get_current_url())
        # assert the url has the given text
        self.wait(1)
        self.assert_true('audience_by_age=216' in url_text)
        self.click(BlogAllPage.audience)
        self.wait(1)
        # unclick 'adults'
        self.click(BlogAllPage.adults)

        # click 'Kids' filter
        self.click(BlogAllPage.kids)
        self.click(BlogAllPage.apply_audience)
        self.wait(1)
        # wait for the next page, see the results (this is for sync issues)
        self.wait_for_element(BlogAllPage.search_results)
        # url text for the filter
        url_text = self.get_current_url()
        print(self.get_current_url())
        # assert the url has the given text
        self.wait(1)
        self.assert_true('audience_by_age=217' in url_text)
        self.click(BlogAllPage.audience)
        self.wait(1)
        # unclick 'kids'
        self.click(BlogAllPage.kids)

        # click 'Teens' filter
        self.click(BlogAllPage.teens)
        self.click(BlogAllPage.apply_audience)
        self.wait(1)
        # wait for the next page, see the results (this is for sync issues)
        self.wait_for_element(BlogAllPage.search_results)
        # url text for the filter
        url_text = self.get_current_url()
        print(self.get_current_url())
        # assert the url has the given text
        self.wait(1)
        self.assert_true('audience_by_age=222' in url_text)
