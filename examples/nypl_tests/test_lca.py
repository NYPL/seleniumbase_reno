import os

import pytest
import uuid
from dotenv import load_dotenv
from selenium.webdriver import Keys

from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_lca import LibraryCardPage
from selenium.common.exceptions import NoSuchElementException

# Load environment variables from .env file
load_dotenv()


# @pytest.mark.test
# @pytest.mark.skip
@pytest.mark.only_firefox
@pytest.mark.smoke
class LibraryCard(NyplUtils):
    # https://www.nypl.org/library-card/new

    # def setUp(self):
    #     super().setUp()
    #     print("\n=================================")
    #     print("RUNNING BEFORE EACH TEST")
    #
    #     # open locations page
    #     self.open_library_card_page()

    def setUp(self):
        self.uc = True  # or False for CDP mode
        self.chromium_arg = "--user-data-dir=/tmp/clean-profile"
        self.chromium_arg = "--disable-extensions"
        self.chromium_arg = "--no-first-run"
        self.chromium_arg = "--no-default-browser-check"
        self.chromium_arg = "--disable-popup-blocking"
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        self.open_library_card_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        print("=================================")
        super().tearDown()

    def alternate_address(self):
        """Reusable method to fill Alternate Address fields"""
        if self.is_element_visible(LibraryCardPage.alternate_address):
            self.send_keys(LibraryCardPage.work_address, "123 East 45th Street")
            self.send_keys(LibraryCardPage.work_apartment, "3F")
            self.send_keys(LibraryCardPage.work_city, "New York")
            self.send_keys(LibraryCardPage.work_state, "NY")
            self.send_keys(LibraryCardPage.work_zip, "10017")

            print(self.get_current_url())
            self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

    @pytest.mark.smoke
    def test_library_card_new(self):

        print("Driver path:", self.driver.service.path)

        # https://www.nypl.org/library-card/new
        print("test_library_card_new()\n")

        print(self.get_current_url())
        self.execute_script("console.log(navigator.userAgent)")
        print(self.driver.execute_script("return navigator.userAgent"))

        # Landing page

        # assert languages
        self.assert_element(LibraryCardPage.arabic)
        self.assert_element(LibraryCardPage.bengali)
        self.assert_element(LibraryCardPage.chinese)
        self.assert_element(LibraryCardPage.english)
        self.assert_element(LibraryCardPage.french)
        self.assert_element(LibraryCardPage.haitian)
        self.assert_element(LibraryCardPage.korean)
        self.assert_element(LibraryCardPage.polish)
        self.assert_element(LibraryCardPage.russian)
        self.assert_element(LibraryCardPage.spanish)
        self.assert_element(LibraryCardPage.urdu)

        # click & assert "Get Started" button
        self.click(LibraryCardPage.get_started)

        # Step 1 of 5: Personal Information
        # https://www.nypl.org/library-card/personal?newCard=true
        print(self.get_current_url())

        # create a unique email with UUID
        email = f"joedoe_nypl_lca_qa_{uuid.uuid4().hex[:8]}@gmail.com"

        self.send_keys(LibraryCardPage.first_name, "Joe")
        self.send_keys(LibraryCardPage.last_name, "Doe")
        self.send_keys(LibraryCardPage.date_of_birth, "05/15/2001")
        self.send_keys(LibraryCardPage.email, email)

        self.assert_element(LibraryCardPage.previous_button)
        self.click(LibraryCardPage.next_button)

        # Step 2 of 5: Address
        # https://www.nypl.org/library-card/location?&newCard=true
        # self.wait(2)
        print(self.get_current_url())

        self.send_keys(LibraryCardPage.street_address, "123 East 45th Street")
        self.send_keys(LibraryCardPage.apartment, "3F")
        self.send_keys(LibraryCardPage.city, "New York")
        self.send_keys(LibraryCardPage.state, "NY")
        self.send_keys(LibraryCardPage.zip, "10017")

        self.assert_element(LibraryCardPage.previous_button)
        self.click(LibraryCardPage.next_button)

        # Alternate Address
        self.alternate_address()  # check if alternate address page visible

        # Attempt Address Verification up to 3 times
        max_attempts = 3

        for attempt in range(1, max_attempts + 1):
            try:
                # Step 3 of 5: Address Verification
                self.assert_element(LibraryCardPage.address_verification_1)
                self.assert_element(LibraryCardPage.address_verification_2)

                break  # Exit loop if successful

            except NoSuchElementException:
                print(f"⚠️ Address verification elements not found (Attempt {attempt}/{max_attempts})")

                if attempt < max_attempts:
                    print("⏳ Retrying after waiting...")
                    self.wait(3)

                    # Retry Alternate Address step before the next attempt
                    self.alternate_address()
                else:
                    print("❌ Address verification failed after 3 attempts. Raising exception.")
                    raise  # Fails test after all attempts

        print(self.get_current_url())
        self.assert_element(LibraryCardPage.previous_button)
        self.click(LibraryCardPage.next_button)

        # Step 4 of 5: Customize Your Account

        # create a unique username with UUID
        username = f"QaLibUser{uuid.uuid4().hex[:8]}"  # Shortened UUID

        # Retrieve password from environment variables
        password = os.getenv('LCA_PASSWORD')

        # Debug print statements to check if the variables are set
        # print(f"\nUsername: {username}")
        # print(f"Password: {password}")
        # print(f"Email: {email}\n")

        # Ensure username and password are not None
        if not username or not password:
            raise Exception("Environment variables USERNAME and PASSWORD must be set!")

        self.send_keys(LibraryCardPage.username_box, username)
        self.send_keys(LibraryCardPage.password_box, password)
        self.send_keys(LibraryCardPage.verify_password_box, password)
        self.click_with_fallback(LibraryCardPage.show_password)

        print(self.get_current_url())

        # todo: update the new home library dropdown
        # self.send_keys(LibraryCardPage.home_library_box, "Stephen A. Schwarzman Building")
        # self.send_keys(LibraryCardPage.home_library_box, Keys.ENTER)
        self.click(LibraryCardPage.terms_checkbox)

        print(self.get_current_url())
        # Right before the assertion
        print("Dumping current page source:")
        page_source = self.driver.page_source
        with open("page_dump_account.html", "w", encoding="utf-8") as f:
            f.write(page_source)

        self.assert_element(LibraryCardPage.previous_button)
        self.click(LibraryCardPage.next_button)

        # Step 5 of 5: Confirm Your Information
        self.assert_element(LibraryCardPage.edit_personal)
        self.assert_element(LibraryCardPage.edit_address)
        self.assert_element(LibraryCardPage.edit_create)

        print(self.get_current_url())
        self.click_with_fallback(LibraryCardPage.showPasswordReview)
        self.click(LibraryCardPage.next_button)

        # Congrats Page

        self.assert_element(LibraryCardPage.congrats_text)  # asserting Congrats text

        # asserting Barcode number
        self.assert_element(LibraryCardPage.barcode)
        barcode_number = self.get_text(LibraryCardPage.barcode_number)  # getting the barcode string to assert below
        self.assert_true("255" in barcode_number, "Barcode does not have a valid number\n")  # asserting barcode no

        # asserting Member Name
        member_name = self.get_text(LibraryCardPage.member_name)
        member_name_length = len(member_name.strip())
        print("Member name: " + member_name, ", Name length: " + str(member_name_length))
        self.assert_true(member_name_length >= 2, "Member name is too short or missing\n")

        # asserting Issue Date
        issued_date = self.get_text(LibraryCardPage.issued_date)
        issued_date_length = len(issued_date.strip())
        print("\nIssued date: " + issued_date, ", Date length: " + str(issued_date_length))
        self.assert_true(issued_date_length >= 6, "Issued date is too short or missing")

        print(self.get_current_url())

        # assert all links on the confirmation page
        self.assert_links_valid(LibraryCardPage.all_links)
