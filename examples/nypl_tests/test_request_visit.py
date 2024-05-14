from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_request_visit import RequestVisitPage

import random


class RequestVisitTest(NyplUtils):
    # https://www.nypl.org/locations/request-visit
    # todo: left here 04/12

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open main page
        self.open_request_visit_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def test_request_visit_main(self):
        print("test_request_visit_main()\n")

        # assert title
        self.assert_title('Locations: Schedule a Visit | The New York Public Library')

        # assert images on the page
        self.image_assertion()

        # assert breadcrumbs
        self.assert_element(RequestVisitPage.home)
        self.assert_element(RequestVisitPage.locations)

        # assert library amount in the dropdown
        library_amount = len(self.find_elements(RequestVisitPage.location_selection))
        print("Library amount for dropdown: " + str(library_amount))
        self.assert_true(library_amount > 10, "Library amount not greater than " + str(library_amount))

        visit_type_amount = len(self.find_elements(RequestVisitPage.visit_type_selection)) - 1
        print("Visit Type amount for dropdown: " + str(visit_type_amount))
        self.assert_true(visit_type_amount > 1, "Visit Type amount not greater than " + str(visit_type_amount))

    def test_request_visit_positive(self):
        print("test_request_visit_positive()\n")

        # asserting a filled up submission would go through successfully

        # asserting 2 visit types in a loop (Virtual and In-Person)
        for y in range(1, 3):
            x = random.randint(1, 89)  # choosing a random library in range 1-89 inc.
            self.click(RequestVisitPage.location_dropdown)
            self.click(RequestVisitPage.location_selection + "[ " + str(x) + "]")

            #self.click(RequestVisitPage.visit_type_dropdown)
            if y == 2:  # Only for 'In-Person Visit'  # if the selection is 'In-Person Visit', execute next
                self.click(RequestVisitPage.in_person_visit)
                self.click(RequestVisitPage.group_tour)
            else:
                # school or organization
                self.click(RequestVisitPage.virtual_visit)
                self.click(RequestVisitPage.reader_advisory)  # when the selection is 'Virtual Visit'

            self.send_keys(RequestVisitPage.school_or_organization, "Midtown High School")
            self.click(RequestVisitPage.kids)
            self.click(RequestVisitPage.teens)
            self.click(RequestVisitPage.adults)

            self.send_keys(RequestVisitPage.contact_name, "Peter Parker")
            self.send_keys(RequestVisitPage.contact_email, 'peterparker@nypl.org')

            # assert the URL after the submission that it has 'confirmation'
            self.click(RequestVisitPage.submit)
            self.wait_for_text("Thank You!")
            # self.wait(2)
            print(self.get_current_url())
            self.assert_true("confirmation" in self.get_current_url())
            if y == 1:
                print("Virtual Visit type\n")
            else:
                print("In-Person Visit\n")

            # open main page
            self.open_request_visit_page()

    def test_request_visit_negative(self):
        print("test_request_visit_negative()\n")

        # negative testing. checking if the page displays error when we submit without any entry
        self.click(RequestVisitPage.submit)
        warning_text = "There was a problem with your submissions. Errors have been highlighted below."
        self.assert_true(warning_text in RequestVisitPage.warning, warning_text + "!= " + RequestVisitPage.warning)
