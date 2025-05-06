import os
import uuid
import pytest
from dotenv import load_dotenv
from selenium.webdriver import Keys
from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_lca_2 import LibraryCardPageNew
from seleniumbase.common.exceptions import NoSuchElementException

load_dotenv()


@pytest.mark.test
@pytest.mark.smoke
@pytest.mark.qa
class LibraryCard(NyplUtils):

    def setUp(self):
        super().setUp()
        print("\n=============================================================\n")
        self.open_library_card_page()

    def tearDown(self):
        print("\n=============================================================\n")

        super().tearDown()

    def alternate_address(self):
        if self.is_element_visible(LibraryCardPageNew.alternate_address):
            self.send_keys(LibraryCardPageNew.work_address, "123 East 45th Street")
            self.send_keys(LibraryCardPageNew.work_apartment, "3F")
            self.send_keys(LibraryCardPageNew.work_city, "New York")
            self.send_keys(LibraryCardPageNew.work_state, "NY")
            self.send_keys(LibraryCardPageNew.work_zip, "10017")
            print(self.get_current_url())
            self.assert_element(LibraryCardPageNew.previous_button)
            self.click(LibraryCardPageNew.next_button)

    def fill_basic_form(self):
        print("Step 0: Landing page")
        print(self.get_current_url())
        self.click(LibraryCardPageNew.get_started)

        print("Step 1 of 5: Personal Information")
        print(self.get_current_url())
        email = f"joedoe_nypl_lca_qa_{uuid.uuid4().hex[:8]}@gmail.com"
        self.send_keys(LibraryCardPageNew.first_name, "Joe")
        self.send_keys(LibraryCardPageNew.last_name, "Doe")
        self.send_keys(LibraryCardPageNew.date_of_birth, "05/15/2001")
        self.send_keys(LibraryCardPageNew.email, email)
        self.assert_element(LibraryCardPageNew.previous_button)
        self.click(LibraryCardPageNew.next_button)

        print("Step 2 of 5: Address")
        self.wait(2)
        print(self.get_current_url())
        self.send_keys(LibraryCardPageNew.street_address, "123 East 45th Street")
        self.send_keys(LibraryCardPageNew.apartment, "3F")
        self.send_keys(LibraryCardPageNew.city, "New York")
        self.send_keys(LibraryCardPageNew.state, "NY")
        self.send_keys(LibraryCardPageNew.zip, "10017")
        self.assert_element(LibraryCardPageNew.previous_button)
        self.click(LibraryCardPageNew.next_button)

        print("Step 2.5: Alternate Address (if applicable)")
        self.alternate_address()

        print("Step 3 of 5: Address Verification")
        for attempt in range(1, 4):
            try:
                self.assert_element(LibraryCardPageNew.address_verification_1)
                self.assert_element(LibraryCardPageNew.address_verification_2)
                break
            except NoSuchElementException:
                print(f"⚠️ Address verification elements not found (Attempt {attempt}/3)")
                if attempt < 3:
                    print("⏳ Retrying after waiting...")
                    self.wait(3)
                    self.alternate_address()
                else:
                    print("❌ Address verification failed after 3 attempts. Raising exception.")
                    raise

        print(self.get_current_url())
        self.assert_element(LibraryCardPageNew.previous_button)
        self.click(LibraryCardPageNew.next_button)

        print("Step 4 of 5: Customize Your Account")
        username = f"QaLibUser{uuid.uuid4().hex[:8]}"
        password = os.getenv("LCA_PASSWORD")

        if not username or not password:
            raise Exception("Environment variables USERNAME and PASSWORD must be set!")

        self.send_keys(LibraryCardPageNew.username_box, username)

        if "invalid_password" in self._testMethodName:
            print("Using invalid password for this test")
            self.send_keys(LibraryCardPageNew.password_box, LibraryCardPageNew.invalid_password)
            self.send_keys(LibraryCardPageNew.verify_password_box, LibraryCardPageNew.invalid_password)
        else:
            self.send_keys(LibraryCardPageNew.password_box, password)
            self.send_keys(LibraryCardPageNew.verify_password_box, password)

        self.click_with_fallback(LibraryCardPageNew.show_password)
        self.send_keys(LibraryCardPageNew.home_library_box, "Stephen A. Schwarzman Building")
        self.click(LibraryCardPageNew.terms_checkbox)

        print(self.get_current_url())
        self.assert_element(LibraryCardPageNew.previous_button)
        self.click(LibraryCardPageNew.next_button)

        print("Step 5 of 5: Confirm Your Information")
        self.assert_element(LibraryCardPageNew.edit_personal)
        self.assert_element(LibraryCardPageNew.edit_address)
        self.assert_element(LibraryCardPageNew.edit_create)
        print(self.get_current_url())
        self.click_with_fallback(LibraryCardPageNew.showPasswordReview)
        self.click(LibraryCardPageNew.next_button)

        if self._testMethodName == "test_library_card_04_invalid_password":
            print("Step 6: Verifying form submission error")
            self.assert_element(LibraryCardPageNew.form_submission_error_fr)
            return
        elif self._testMethodName == "test_library_card_05_invalid_password":
            print("Step 6: Verifying form submission error")
            self.assert_element(LibraryCardPageNew.form_submission_error_ar)
            return

        print("Congrats Page")
        self.assert_element(LibraryCardPageNew.congrats_text)
        self.assert_element(LibraryCardPageNew.barcode)
        barcode_number = self.get_text(LibraryCardPageNew.barcode_number)
        self.assert_true("255" in barcode_number, "Barcode does not have a valid number")

        member_name = self.get_text(LibraryCardPageNew.member_name)
        print("Member name: " + member_name + ", Name length: " + str(len(member_name.strip())))
        self.assert_true(len(member_name.strip()) >= 2, "Member name is too short or missing")

        issued_date = self.get_text(LibraryCardPageNew.issued_date)
        print("\nIssued date: " + issued_date + ", Date length: " + str(len(issued_date.strip())))
        self.assert_true(len(issued_date.strip()) >= 6, "Issued date is too short or missing")

        print(self.get_current_url())
        self.assert_links_valid(LibraryCardPageNew.all_links)

    def test_library_card_01_english(self):
        print("library card english")
        self.fill_basic_form()

    def test_library_card_02_arabic(self):
        print("library card arabic")
        self.click(LibraryCardPageNew.arabic)
        self.fill_basic_form()

    def test_library_card_03_french(self):
        print("library card french")
        self.click(LibraryCardPageNew.french)
        self.fill_basic_form()

    def test_library_card_04_invalid_password(self):
        print("library card invalid password french")
        # This test verifies the error message appears in the selected language after an invalid password submission.
        self.click(LibraryCardPageNew.french)
        self.fill_basic_form()

    def test_library_card_05_invalid_password(self):
        print("library card invalid password arabic")
        # This test verifies the error message appears in the selected language after an invalid password submission.
        self.click(LibraryCardPageNew.arabic)
        self.fill_basic_form()

