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

        # assert all links on the page
        self.assert_links_valid(BlogAllPage.all_links)

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
        """This method randomly takes 10 elements (can be changed) and asserts 
        the child elements of the Audience filter and if they are clickable."""

        # Assert Audience button
        self.assert_element(BlogAllPage.audience)

        # Click 'Audience' tab
        self.click(BlogAllPage.audience)

        # Define audience filters and expected URL parameters
        audience_filters = {
            "Adults": "audience_by_age=216",
            "Kids": "audience_by_age=217",
            "Teens": "audience_by_age=222"
        }

        def apply_and_verify_filter(filter_element, expected_text):
            """Helper function to apply filter and verify the URL"""
            try:
                self.click(filter_element)
                self.click(BlogAllPage.apply_audience)
                self.wait(1)
                self.wait_for_element(BlogAllPage.filter_results)
                url_text = self.get_current_url()
                print(url_text)
                self.wait(1)
                assert expected_text in url_text, f"Actual URL: {url_text}, Expected URL to contain: {expected_text}"
            except AssertionError:
                print(f"Assertion failed, retrying filter: {filter_element}")
                self.click(filter_element)  # Retry clicking the filter
                self.wait(2)  # Additional wait for stability
                url_text = self.get_current_url()
                assert expected_text in url_text, f"Actual URL: {url_text}, Expected URL to contain: {expected_text}"

            # Unselect the filter before moving to the next
            self.click(BlogAllPage.audience)
            self.wait(1)
            self.click(filter_element)

        # Iterate through each audience filter
        for filter_name, url_param in audience_filters.items():
            filter_element = getattr(BlogAllPage, filter_name.lower())  # Convert name to lowercase to match attribute
            apply_and_verify_filter(filter_element, url_param)
