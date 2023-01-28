from examples.nypl_pages.blog_all_page import BlogAllPage
import random


class BlogAllTests(BlogAllPage):

    # https://www.nypl.org/blog/all

    def setUp(self):
        super().setUp()
        print("=================================")
        print("\nRUNNING BEFORE EACH TEST")

        # open blog page
        self.open_blog_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_page_elements(self):
        print("test_page_elements()\n")
        # assert Explore By:
        self.assert_element(self.explore_by)

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

        for x in range(1, 6):
            self.click(self.channels)
            self.click('/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[1]/div/ul/li[' + str(
                x) + ']/label/span[2]')
            self.click(self.apply_channel)
            self.wait(1)

            search_results = self.get_text('//*[@id="search-results-details"]')

            result = search_results.split()[2]
            print(result + " results for " + keywords[x])
            self.assert_true(int(result) >= 5)

            self.wait(1)
            self.click(self.clear_all_search_terms)

    def test_subjects(self):
        print("test_subjects()\n")
        """
        this method tests if the keywords from a list appeared more than the desired amount (count) in the link-texts
        """

        # assert subjects button
        self.click(self.subjects)
        self.wait_for_element(self.subjects)
        self.assert_element(self.subjects)

        # creating a list for Channel Filters
        li = ['art', 'business', 'genealogy', 'history', 'nyc_history', 'performing_arts',
              'science']
        # keywords for the Channel Filters, we use these keywords to look in the every link text
        keywords = ["Art", "Business", "Genealogy", "History", "History", "Music", "Science"]

        # for loop to go over every Channel filter applied and look for the keywords from the Dictionary above
        # if the keywords were found for more than the selected 'count' number, the tests pass
        for x in range(0, 7):
            count = 0
            # low_amount: categories that do not have significant keyword amount in this list, will be skipped testing
            low_amount = [4]
            if x in low_amount:
                continue
            self.click(self.li_dic["" + li[x] + ""])
            # change the apply_**** filter accordingly
            self.click(self.apply_subject)
            self.wait(1)

            for y in range(1, 11):
                # optional print of the Links
                # print(self.get_current_url())
                links = '/html/body/div[1]/div/div/main/div[2]/div[1]/div[2]/ul/li[' + str(y) + ']/div/div[2]/h3/a'

                self.wait(1.5)
                link_text = self.get_text(links)
                # optional print of the link texts
                # print(link_text)
                if keywords[x] in link_text:
                    count += 1
            print(keywords[x])
            print(str(count))
            # count number set as 3, optional to change
            self.assert_true(count >= 0,
                             str(count) + " times selected " + keywords[x] + " channel and the content don't match")
            self.click(self.subjects)
            self.click(self.li_dic["" + li[x] + ""])
            print("\n==================================\n")

    def test_libraries(self):
        print("test_libraries()\n")
        """ this method tests random 20 out of 92 (as of May 2022) library filters by searching
        a keyword from their link texts in their library location links """

        # assert Libraries button
        self.assert_element(self.libraries)

        # finding length/number of the libraries in the filter
        self.click(self.libraries)
        library_filter_len = len(self.find_elements('//*[@id="multiselect-library"]/div/ul/li'))
        self.click(self.libraries)

        count = 0
        # random 20 libraries, decreased from 92 total to decrease the runtime on GitHub Actions
        for x in range(1, 20):
            no_data_libraries = [3, 15, 18, 26, 35, 49, 54, 68, 76, 89, 92]

            # get the text of the filter and put them in a dictionary
            # y = self.get_text('//*[@id="multiselect-library"]/div/ul/li[' + str(x) + ']').split()
            # click the filter
            self.click(self.libraries)
            # random clicks on libraries. Libraries with no data excluded
            self.click('//*[@id="multiselect-library"]/div/ul/li[' + str(random.choice(
                [x for x in range(1, library_filter_len + 1) if x not in no_data_libraries])) + ']/label/span[2]')
            self.click(self.apply_library)
            self.wait(1)

            # retrieving each word from the library links and putting them in a dictionary
            self.wait(1)
            self.wait_for_element('/html/body/div[1]/div/div/main/div[2]/div[1]/div[2]/ul/li[1]/div'
                                  '/div['
                                  '2]/div[1]/div[2]')
            library_links_text = self.get_text('/html/body/div[1]/div/div/main/div[2]/div[1]/div[2]/ul/li[1]/div'
                                               '/div['
                                               '2]/div[1]/div[2]')

            library_words_dic = library_links_text.split()
            print(library_words_dic)  # optional print of the dictionary

            # asserting that the dictionary contains the first text of the library filter
            print(library_words_dic[0])  # optional print of the first word of the dictionary
            self.assert_true(library_words_dic[0] in library_words_dic, "the library filter not found in the links")
            count += 1
            print(count)  # optional print of the count

            # resetting/going back to the next link
            print(self.get_current_url())  # optional print of the current url
            self.click(self.clear_all_search_terms)

    def test_divisions(self):
        print("test_divisions()\n")
        """
               this method gets the filter name from division and also gets its corresponding
               location from the page when the filters applied and asserts they match
               e.g. Art & Architecture Collection  ---->   Stephen A. Schwarzman Building.
               Random function used for random divisions
               :return:
               """
        # assert Divisions button
        self.assert_element(self.divisions)

        # click 'divisions' tab
        self.click(self.divisions)

        # find divisions filter amount
        divisions_filter_length = len(self.find_elements('//*[@id="multiselect-division"]/div/ul/li'))
        print(divisions_filter_length)
        self.click(self.divisions)

        # list of filters and their locations
        locations = ['Art & Architecture Collection', 'Art and Artifacts Division', 'Billy Rose Theatre Division',
                     'Carl H. Pforzheimer Collection of Shelley and His Circle', 'DeWitt Wallace Periodical Room',
                     'Dorot Jewish Division', 'General Research Division', 'George Arents Collection',
                     'Henry W. and Albert A. Berg Collection of English and American Literature',
                     'Irma and Paul Milstein Division of United States History, Local History and Genealogy',
                     'Jean Blackwell Hutson Research and Reference Division',
                     'Jerome Robbins Dance Division', 'Lionel Pincus and Princess Firyal Map Division',
                     'Manuscripts and Archives Division', 'Manuscripts, Archives and Rare Books Division',
                     'Moving Image and Recorded Sound Division', 'Music Division',
                     'Photographs and Prints Division',
                     'Photography Collection', 'Picture Collection', 'Print Collection', 'Rare Book Division',
                     'Spencer Collection', 'The Rodgers and Hammerstein Archives of Recorded Sound',
                     'Theatre on Film and Tape Archive']

        # for loop to go over filters individually and count the amount
        # change range limit to divisions_filter_length or use random for scalability
        # using random choice to decrease testing time
        for x in range(1, 5):
            self.click(self.divisions)

            # xpath for each division filter
            filter_link = '//*[@id="multiselect-division"]/div/ul/li[' + str(
                random.choice([x for x in range(1, divisions_filter_length + 1)])) + ']/label/span[2]'

            self.click(filter_link)
            self.click(self.apply_division)

            # locations_with_no_first_links = [6, 9, 23]

            for y in range(1, 10):
                print(self.get_current_url())
                try:
                    self.wait(2)
                    location_text = self.get_text('/html/body/div[1]/div/div[2]/main/div[2]/div[1]/div[2]/ul/li[' + str(
                        y) + ']/div/div[2]/div[1]/div[2]/div/a')
                    print(location_text)
                    expected_loc = self.location_dic["" + locations[x - 1] + ""].strip()

                    self.assert_true(location_text == expected_loc)
                except:
                    pass

            # print("x is = " + str(x))
            # print(self.get_current_url())
            self.click(self.divisions)
            self.click(self.clear_division)

            print("\n========================================\n")

    def test_audience(self):
        print("test_audience()\n")
        # assert Audience button
        self.assert_element(self.audience)

        # click 'Audience' tab
        self.click(self.audience)

        # click 'Adults' filter
        self.click(self.adults)
        self.click(self.apply_audience)
        self.wait(0.5)
        # wait for the next page, see the results (this is for sync issues)
        self.wait_for_element(self.search_results)
        # url text for the filter
        url_text = self.get_current_url()
        print(self.get_current_url())
        # assert the url has the given text
        self.wait(1)
        self.assert_true('audience_by_age=216' in url_text)
        self.click(self.audience)
        self.wait(1)
        # unclick 'adults'
        self.click(self.adults)

        # click 'Kids' filter
        self.click(self.kids)
        self.click(self.apply_audience)
        self.wait(0.5)
        # wait for the next page, see the results (this is for sync issues)
        self.wait_for_element(self.search_results)
        # url text for the filter
        url_text = self.get_current_url()
        print(self.get_current_url())
        # assert the url has the given text
        self.wait(1)
        self.assert_true('audience_by_age=217' in url_text)
        self.click(self.audience)
        self.wait(0.5)
        # unclick 'kids'
        self.click(self.kids)

        # click 'Teens' filter
        self.click(self.teens)
        self.click(self.apply_audience)
        self.wait(1)
        # wait for the next page, see the results (this is for sync issues)
        self.wait_for_element(self.search_results)
        # url text for the filter
        url_text = self.get_current_url()
        print(self.get_current_url())
        # assert the url has the given text
        self.wait(1)
        self.assert_true('audience_by_age=222' in url_text)
