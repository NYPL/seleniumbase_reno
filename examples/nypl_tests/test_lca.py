import os
import uuid
import pytest
from dotenv import load_dotenv
from selenium.webdriver import Keys
from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_lca import LibraryCardPage
from selenium.common.exceptions import NoSuchElementException


load_dotenv()


# @pytest.mark.test
# @pytest.mark.smoke
@pytest.mark.test
class LibraryCard(NyplUtils):

    def setUp(self):
        super().setUp()
        # self.set_window_size(1440, 960)  # Set browser to Full HD size
        print("\n=============================================================\n")
        self.open_library_card_page()

    def tearDown(self):
        print("\n=============================================================\n")

        super().tearDown()

    def alternate_address(self):
        if self.is_element_visible(LibraryCardPage.alternate_address):
            self.send_keys(LibraryCardPage.work_address, "123 East 45th Street")
            self.send_keys(LibraryCardPage.work_apartment, "3F")
            self.send_keys(LibraryCardPage.work_city, "New York")
            self.send_keys(LibraryCardPage.work_state, "NY")
            self.send_keys(LibraryCardPage.work_zip, "10017")
            print(self.get_current_url())
            self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

    # login web element locator for the Congrats page depending on the selected language
    def get_login_locator(self):
        if "arabic" in self._testMethodName:
            return LibraryCardPage.log_into_your_account_ar
        elif "french" in self._testMethodName:
            return LibraryCardPage.log_into_your_account_fr
        return LibraryCardPage.log_into_your_account_en

    # basic form for any language
    def fill_basic_form(self):
        print("Step 0: Landing page")
        print(self.get_current_url())
        self.click(LibraryCardPage.get_started)

        print("Step 1 of 5: Personal Information")
        print(self.get_current_url())
        email = f"joedoe_nypl_lca_qa_{uuid.uuid4().hex[:8]}@gmail.com"
        self.send_keys(LibraryCardPage.first_name, "Joe")
        self.send_keys(LibraryCardPage.last_name, "Doe")
        self.send_keys(LibraryCardPage.date_of_birth, "05/15/2001")
        self.send_keys(LibraryCardPage.email, email)
        self.assert_element(LibraryCardPage.previous_button)
        self.click(LibraryCardPage.next_button)

        print("Step 2 of 5: Address")
        self.wait(2)
        print(self.get_current_url())
        self.send_keys(LibraryCardPage.street_address, "123 East 45th Street")
        self.send_keys(LibraryCardPage.apartment, "3F")
        self.send_keys(LibraryCardPage.city, "New York")
        self.send_keys(LibraryCardPage.state, "NY")
        self.send_keys(LibraryCardPage.zip, "10017")
        self.assert_element(LibraryCardPage.previous_button)
        self.click(LibraryCardPage.next_button)

        print("Step 2.5: Alternate Address (if applicable)")
        self.alternate_address()

        print("Step 3 of 5: Address Verification")
        for attempt in range(1, 4):
            try:
                self.assert_element(LibraryCardPage.address_verification_1)
                self.assert_element(LibraryCardPage.address_verification_2)
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
        self.assert_element(LibraryCardPage.previous_button)
        self.click(LibraryCardPage.next_button)

        print("Step 4 of 5: Customize Your Account")
        username = f"QaLibUser{uuid.uuid4().hex[:8]}"
        password = os.getenv("LCA_PASSWORD")

        if not password:
            raise Exception("Environment variable LCA_PASSWORD must be set!")

        self.send_keys(LibraryCardPage.username_box, username)

        if "invalid_password" in self._testMethodName:
            print("Using invalid password for this test")
            self.send_keys(LibraryCardPage.password_box, LibraryCardPage.invalid_password)
            self.send_keys(LibraryCardPage.verify_password_box, LibraryCardPage.invalid_password)
        else:
            self.send_keys(LibraryCardPage.password_box, password)
            self.send_keys(LibraryCardPage.verify_password_box, password)

        self.click_with_fallback(LibraryCardPage.show_password)
        # todo: update below home library assertion with a dropdown choice
        # self.send_keys(LibraryCardPage.home_library_box, "Stephen A. Schwarzman Building")
        self.click(LibraryCardPage.terms_checkbox)

        print(self.get_current_url())
        self.assert_element(LibraryCardPage.previous_button)
        self.click(LibraryCardPage.next_button)

        print("Step 5 of 5: Confirm Your Information")
        self.assert_element(LibraryCardPage.edit_personal)
        self.assert_element(LibraryCardPage.edit_address)
        self.assert_element(LibraryCardPage.edit_create)
        print(self.get_current_url())
        self.click_with_fallback(LibraryCardPage.showPasswordReview)
        self.click(LibraryCardPage.next_button)

        if self._testMethodName == "test_library_card_04_invalid_password":
            print("Step 6: Verifying form submission error")
            try:
                self.assert_element(LibraryCardPage.form_submission_error_fr)
            except NoSuchElementException as e:
                print(f"Retrying after error not found (FR): {e}")
                self.wait(2)
                self.assert_element(LibraryCardPage.form_submission_error_fr)
            return

        elif self._testMethodName == "test_library_card_05_invalid_password":
            print("Step 6: Verifying form submission error")
            try:
                self.assert_element(LibraryCardPage.form_submission_error_ar)
            except NoSuchElementException as e:
                print(f"Retrying after error not found (AR): {e}")
                self.wait(2)
                self.assert_element(LibraryCardPage.form_submission_error_ar)
            return
        print("Congrats Page")
        # asserting "Congratulations" text and Barcode
        try:
            self.assert_element(LibraryCardPage.congrats_text)
        except NoSuchElementException as e:
            print(f"Retrying after element not found: {e}")
            self.wait(2)
            self.assert_element(LibraryCardPage.congrats_text)

        try:
            self.assert_element(LibraryCardPage.barcode)
        except NoSuchElementException as e:
            print(f"Retrying after element not found: {e}")
            self.wait(2)
            self.assert_element(LibraryCardPage.barcode)

        barcode_number = self.get_text(LibraryCardPage.barcode_number)
        print("Barcode no: " + barcode_number)
        self.assert_true("255" in barcode_number, "Barcode does not have a valid number")

        member_name = self.get_text(LibraryCardPage.member_name)
        print("Member name: " + member_name + ", Name length: " + str(len(member_name.strip())))
        self.assert_true(len(member_name.strip()) >= 2, "Member name is too short or missing")

        issued_date = self.get_text(LibraryCardPage.issued_date)
        print("\nIssued date: " + issued_date + ", Date length: " + str(len(issued_date.strip())))
        self.assert_true(len(issued_date.strip()) >= 6, "Issued date is too short or missing")

        # assert the login link after new account creation
        # Choose correct login link locator based on the test case
        login_locator = self.get_login_locator()


        # Get login link with retry logic
        try:
            login_link = self.get_attribute(login_locator, "href")
        except NoSuchElementException as e:
            print(f"Retrying after login link element not found: {e}")
            self.wait(2)
            login_link = self.get_attribute(login_locator, "href")

        print(f"Login link: {login_link}")

        # Assert environment-correctness of the link
        try:
            if self.env == "qa":
                self.assert_true("qa" in login_link or "dev" in login_link,
                                 f"Expected QA or dev in login link, got: {login_link}")
            else:
                self.assert_true("qa" not in login_link and "dev" not in login_link,
                                 f"Unexpected 'qa' or 'dev' in prod login link: {login_link}")
        except NoSuchElementException as e:
            print(f"Retrying assertion on login link due to error: {e}")
            self.wait(2)
            if self.env == "qa":
                self.assert_true("qa" in login_link or "dev" in login_link,
                                 f"Expected QA or dev in login link, got: {login_link}")
            else:
                self.assert_true("qa" not in login_link and "dev" not in login_link,
                                 f"Unexpected 'qa' or 'dev' in prod login link: {login_link}")

        print(self.get_current_url())
        self.assert_links_valid(LibraryCardPage.all_links)

    def test_library_card_01_english(self):
        print("library card english")
        self.fill_basic_form()

    def test_library_card_02_arabic(self):
        print("library card arabic")
        self.goto('https://www.nypl.org/library-card/new?lang=ar')
        self.fill_basic_form()

    def test_library_card_03_french(self):
        print("library card french")
        self.goto('https://www.nypl.org/library-card/new?lang=fr')
        self.fill_basic_form()

    def test_library_card_04_invalid_password(self):
        print("library card invalid password french")
        # This test verifies the error message appears in the selected language after an invalid password submission.
        self.goto('https://www.nypl.org/library-card/new?lang=fr')
        self.fill_basic_form()

    def test_library_card_05_invalid_password(self):
        print("library card invalid password arabic")
        # This test verifies the error message appears in the selected language after an invalid password submission.
        self.goto('https://www.nypl.org/library-card/new?lang=ar')
        self.fill_basic_form()

