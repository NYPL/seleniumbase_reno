from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_blog_all import BlogAllPage
import random

base_url = 'https://www.nypl.org/blog/all'


class BlogAllTests(NyplUtils):

    # https://www.nypl.org/blog/all
    def setUp(self):
        super().setUp()
        print("=================================")
        print("\nRUNNING BEFORE EACH TEST")

        # open blog/all page
        self.open_blog_page_all()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_blog_all_main(self):
        print("test_page_elements()\n")

        # asserting the images on the page
        self.image_assertion()

        # assert Explore By:
        self.assert_element(BlogAllPage.explore_by)

    def click_filter_option(self, filter_name, option_index):
        """
        Clicks an option in a specified filter.
        :param filter_name: The name of the filter (e.g., "Subjects", "Channels").
        :param option_index: The index of the option to click.
        """
        filter_xpath = f'//*[contains(text(), "{filter_name}")]//..//..//..//li[{option_index}]/*/*'
        self.click(filter_xpath)

    def test_channels_filter(self):
        print("test_channels()\n")
        """this test asserts the child elements of the Channels filter and if they consist keywords
         related to the subfilter"""

        # asserting 'Channels' filter
        # keywords for the Channel Filters. These keywords are used to look in every search result for assertion
        keywords = ["Asian", "Memoir", "Black", "Book Lists", "Comic", "Digital", "Doc", "Early Literacy", "de",
                    'for kids', 'for teachers', 'for teens', 'de', 'Hispanic', 'Horror', 'LGBTQ', 'Library Stories',
                    'Library Talks', 'Mysteries', 'Nonfiction', 'Poetry', 'Popular Culture', 'Research at nypl',
                    'Romance', 'Science Fiction', 'Librarian', 'Women', 'Work/Cited', 'Chinese']

        # assertion for the first 4 channels by clicking and checking if the result >= 1 on the clicked page
        for x in range(1, 4):
            self.click(BlogAllPage.channels)
            print(f"\nChecking {x}")
            self.click_filter_option("Channels", x)
            self.click(BlogAllPage.apply_channel)
            self.wait(1)
            print(self.get_current_url())

            filter_results = self.get_text(BlogAllPage.filter_results)

            result = filter_results.split()[2]
            print(result + " results for " + keywords[x - 1])
            self.assert_true(int(result) >= 1)
            self.goto(base_url)

    def test_subjects_filter(self):
        print("test_subjects()\n")
        """
        this test asserts the child elements of the Subjects filter and if they are clickable
        """

        # assert subjects button
        self.click(BlogAllPage.subjects)
        self.assert_element(BlogAllPage.subjects)

        # length of the subjects children
        children_subject = len(self.find_elements(BlogAllPage.sub_filters))
        self.click(BlogAllPage.subjects)

        print("Total child elements = " + str(children_subject))

        # asserting that we can click each child element of the children filter
        for x in range(1, 4):
            self.click(BlogAllPage.subjects)
            print(f"\nChecking {x}")
            self.click_filter_option("Subjects", x)
            self.click(BlogAllPage.apply_subject)
            self.assert_true(BlogAllPage.filter_results)
            self.goto(base_url)

    def test_libraries_filter(self):
        print("test_libraries()\n")
        """this method randomly takes 10 elements (can be changed) and asserts the child elements of the Libraries 
        filter and if they are clickable """

        # assert libraries button
        self.assert_element(BlogAllPage.libraries)

        # length of the libraries children
        self.click(BlogAllPage.libraries)
        children_amount = len(self.find_elements(BlogAllPage.sub_filters))
        self.click(BlogAllPage.libraries)

        print("Total child elements = " + str(children_amount))

        # creating a list of random 10 elements for the loop
        num_random_elements = 10
        elements = list(range(1, children_amount + 1))
        random_elements = random.sample(elements, num_random_elements)

        # asserting (randomly) that we can click each child element
        for x in range(1, 4):
            self.click(BlogAllPage.libraries)
            print(f"\nChecking {x}")
            self.click_filter_option("Libraries", x)
            self.click(BlogAllPage.apply_library)
            self.assert_true(BlogAllPage.filter_results)
            self.goto(base_url)

    def test_divisions_filter(self):
        print("test_divisions()\n")
        """this method randomly takes 10 child elements of the Divisions filter (can be changed) and asserts them 
        whether they are clickable"""

        # assert divisions button
        self.assert_element(BlogAllPage.divisions)

        # length of the divisions children
        self.click(BlogAllPage.divisions)
        children_amount = len(self.find_elements(BlogAllPage.sub_filters))
        self.click(BlogAllPage.divisions)

        print("Total child elements = " + str(children_amount))

        num_random_elements = 10
        elements = list(range(1, children_amount + 1))
        random_elements = random.sample(elements, num_random_elements)

        # asserting that we can click each child element
        for x in range(1, 4):
            self.click(BlogAllPage.divisions)
            print(f"\nChecking {x}")
            self.click_filter_option("Divisions", x)
            self.click(BlogAllPage.apply_division)
            self.assert_true(BlogAllPage.filter_results)
            print("Child element " + str(x))
            self.goto(base_url)

        print("\n========================================\n")

    def test_audience_filter(self):
        print("test_audience()\n")
        """this method randomly takes 10 elements (can be changed) and asserts the child elements of the Audience 
        filter and if they are clickable """

        # assert Audience button
        self.assert_element(BlogAllPage.audience)

        # click 'Audience' tab
        self.click(BlogAllPage.audience)

        # click 'Adults' filter
        self.click(BlogAllPage.adults)
        self.click(BlogAllPage.apply_audience)
        self.wait(1)
        # wait for the next page, see the results (this is for sync issues)
        self.wait_for_element(BlogAllPage.filter_results)
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
        self.wait_for_element(BlogAllPage.filter_results)
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
        self.wait_for_element(BlogAllPage.filter_results)
        # url text for the filter
        url_text = self.get_current_url()
        print(self.get_current_url())

        # assert the url has the given text
        self.wait(1)
        self.assert_true('audience_by_age=222' in url_text)
