import os

import pytest
import uuid
from dotenv import load_dotenv

from examples.nypl_utility.utility import NyplUtils
from examples.nypl_pages.page_lca import LibraryCardPage
from seleniumbase.common.exceptions import NoSuchElementException

# Load environment variables from .env file
load_dotenv()

# Set the number of times the test should run
run_count = 1  # Modify this value to change how many times the test executes


@pytest.mark.test
@pytest.mark.lca
class LibraryCard(NyplUtils):
    # https://www.nypl.org/library-card/new

    def setUp(self):
        super().setUp()
        print("\n=================================")
        print("RUNNING BEFORE EACH TEST")

        # open locations page
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
            # self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

    def test_library_card_new_1(self):
        # https://www.nypl.org/library-card/new
        print("test_library_card_new()\n")

        for i in range(run_count):
            """Run the test multiple times based on the `run_count` variable"""
            print(f"\n========== Running Iteration {i + 1} of {run_count} ==========\n")

            # open library card page
            self.open_library_card_page()
            print(self.get_current_url())

            # Landing page

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

            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 2 of 5: Address
            # https://www.nypl.org/library-card/location?&newCard=true
            self.wait(2)
            print(self.get_current_url())

            self.send_keys(LibraryCardPage.street_address, "123 East 45th Street")
            self.send_keys(LibraryCardPage.apartment, "3F")
            self.send_keys(LibraryCardPage.city, "New York")
            self.send_keys(LibraryCardPage.state, "NY")
            self.send_keys(LibraryCardPage.zip, "10017")

            #self.assert_element(LibraryCardPage.previous_button)
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
            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 4 of 5: Customize Your Account

            # create a unique username with UUID
            username = f"QaLibUser{uuid.uuid4().hex[:8]}"  # Shortened UUID

            # Retrieve password from environment variables
            password = os.getenv('LCA_PASSWORD')

            # Debug print statements to check if the variables are set
            print(f"\nUsername: {username}")
            print(f"Password: {password}")
            print(f"Email: {email}\n")

            # Ensure username and password are not None
            if not username or not password:
                raise Exception("Environment variables USERNAME and PASSWORD must be set!")

            self.send_keys(LibraryCardPage.username_box, username)
            self.send_keys(LibraryCardPage.password_box, password)
            self.send_keys(LibraryCardPage.verify_password_box, password)
            self.click_with_fallback(LibraryCardPage.show_password)
            self.send_keys(LibraryCardPage.home_library_box, "Stephen A. Schwarzman Building")
            self.click(LibraryCardPage.terms_checkbox)

            print(self.get_current_url())
            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 5 of 5: Confirm Your Information
            #self.assert_element(LibraryCardPage.edit_personal)
            #self.assert_element(LibraryCardPage.edit_address)
            #self.assert_element(LibraryCardPage.edit_create)

            print(self.get_current_url())
            self.click_with_fallback(LibraryCardPage.showPasswordReview)
            self.click(LibraryCardPage.next_button)

    def test_library_card_new_2(self):
        # https://www.nypl.org/library-card/new
        print("test_library_card_new()\n")

        for i in range(run_count):
            """Run the test multiple times based on the `run_count` variable"""
            print(f"\n========== Running Iteration {i + 1} of {run_count} ==========\n")

            # open library card page
            self.open_library_card_page()
            print(self.get_current_url())

            # Landing page

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

            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 2 of 5: Address
            # https://www.nypl.org/library-card/location?&newCard=true
            self.wait(2)
            print(self.get_current_url())

            self.send_keys(LibraryCardPage.street_address, "123 East 45th Street")
            self.send_keys(LibraryCardPage.apartment, "3F")
            self.send_keys(LibraryCardPage.city, "New York")
            self.send_keys(LibraryCardPage.state, "NY")
            self.send_keys(LibraryCardPage.zip, "10017")

            #self.assert_element(LibraryCardPage.previous_button)
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
            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 4 of 5: Customize Your Account

            # create a unique username with UUID
            username = f"QaLibUser{uuid.uuid4().hex[:8]}"  # Shortened UUID

            # Retrieve password from environment variables
            password = os.getenv('LCA_PASSWORD')

            # Debug print statements to check if the variables are set
            print(f"\nUsername: {username}")
            print(f"Password: {password}")
            print(f"Email: {email}\n")

            # Ensure username and password are not None
            if not username or not password:
                raise Exception("Environment variables USERNAME and PASSWORD must be set!")

            self.send_keys(LibraryCardPage.username_box, username)
            self.send_keys(LibraryCardPage.password_box, password)
            self.send_keys(LibraryCardPage.verify_password_box, password)
            self.click_with_fallback(LibraryCardPage.show_password)
            self.send_keys(LibraryCardPage.home_library_box, "Stephen A. Schwarzman Building")
            self.click(LibraryCardPage.terms_checkbox)

            print(self.get_current_url())
            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 5 of 5: Confirm Your Information
            #self.assert_element(LibraryCardPage.edit_personal)
            #self.assert_element(LibraryCardPage.edit_address)
            #self.assert_element(LibraryCardPage.edit_create)

            print(self.get_current_url())
            self.click_with_fallback(LibraryCardPage.showPasswordReview)
            self.click(LibraryCardPage.next_button)

    def test_library_card_new_3(self):
        # https://www.nypl.org/library-card/new
        print("test_library_card_new()\n")

        for i in range(run_count):
            """Run the test multiple times based on the `run_count` variable"""
            print(f"\n========== Running Iteration {i + 1} of {run_count} ==========\n")

            # open library card page
            self.open_library_card_page()
            print(self.get_current_url())

            # Landing page

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

            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 2 of 5: Address
            # https://www.nypl.org/library-card/location?&newCard=true
            self.wait(2)
            print(self.get_current_url())

            self.send_keys(LibraryCardPage.street_address, "123 East 45th Street")
            self.send_keys(LibraryCardPage.apartment, "3F")
            self.send_keys(LibraryCardPage.city, "New York")
            self.send_keys(LibraryCardPage.state, "NY")
            self.send_keys(LibraryCardPage.zip, "10017")

            #self.assert_element(LibraryCardPage.previous_button)
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
            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 4 of 5: Customize Your Account

            # create a unique username with UUID
            username = f"QaLibUser{uuid.uuid4().hex[:8]}"  # Shortened UUID

            # Retrieve password from environment variables
            password = os.getenv('LCA_PASSWORD')

            # Debug print statements to check if the variables are set
            print(f"\nUsername: {username}")
            print(f"Password: {password}")
            print(f"Email: {email}\n")

            # Ensure username and password are not None
            if not username or not password:
                raise Exception("Environment variables USERNAME and PASSWORD must be set!")

            self.send_keys(LibraryCardPage.username_box, username)
            self.send_keys(LibraryCardPage.password_box, password)
            self.send_keys(LibraryCardPage.verify_password_box, password)
            self.click_with_fallback(LibraryCardPage.show_password)
            self.send_keys(LibraryCardPage.home_library_box, "Stephen A. Schwarzman Building")
            self.click(LibraryCardPage.terms_checkbox)

            print(self.get_current_url())
            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 5 of 5: Confirm Your Information
            #self.assert_element(LibraryCardPage.edit_personal)
            #self.assert_element(LibraryCardPage.edit_address)
            #self.assert_element(LibraryCardPage.edit_create)

            print(self.get_current_url())
            self.click_with_fallback(LibraryCardPage.showPasswordReview)
            self.click(LibraryCardPage.next_button)

    def test_library_card_new_4(self):
        # https://www.nypl.org/library-card/new
        print("test_library_card_new()\n")

        for i in range(run_count):
            """Run the test multiple times based on the `run_count` variable"""
            print(f"\n========== Running Iteration {i + 1} of {run_count} ==========\n")

            # open library card page
            self.open_library_card_page()
            print(self.get_current_url())

            # Landing page

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

            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 2 of 5: Address
            # https://www.nypl.org/library-card/location?&newCard=true
            self.wait(2)
            print(self.get_current_url())

            self.send_keys(LibraryCardPage.street_address, "123 East 45th Street")
            self.send_keys(LibraryCardPage.apartment, "3F")
            self.send_keys(LibraryCardPage.city, "New York")
            self.send_keys(LibraryCardPage.state, "NY")
            self.send_keys(LibraryCardPage.zip, "10017")

            #self.assert_element(LibraryCardPage.previous_button)
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
            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 4 of 5: Customize Your Account

            # create a unique username with UUID
            username = f"QaLibUser{uuid.uuid4().hex[:8]}"  # Shortened UUID

            # Retrieve password from environment variables
            password = os.getenv('LCA_PASSWORD')

            # Debug print statements to check if the variables are set
            print(f"\nUsername: {username}")
            print(f"Password: {password}")
            print(f"Email: {email}\n")

            # Ensure username and password are not None
            if not username or not password:
                raise Exception("Environment variables USERNAME and PASSWORD must be set!")

            self.send_keys(LibraryCardPage.username_box, username)
            self.send_keys(LibraryCardPage.password_box, password)
            self.send_keys(LibraryCardPage.verify_password_box, password)
            self.click_with_fallback(LibraryCardPage.show_password)
            self.send_keys(LibraryCardPage.home_library_box, "Stephen A. Schwarzman Building")
            self.click(LibraryCardPage.terms_checkbox)

            print(self.get_current_url())
            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 5 of 5: Confirm Your Information
            #self.assert_element(LibraryCardPage.edit_personal)
            #self.assert_element(LibraryCardPage.edit_address)
            #self.assert_element(LibraryCardPage.edit_create)

            print(self.get_current_url())
            self.click_with_fallback(LibraryCardPage.showPasswordReview)
            self.click(LibraryCardPage.next_button)

    def test_library_card_new_5(self):
        # https://www.nypl.org/library-card/new
        print("test_library_card_new()\n")

        for i in range(run_count):
            """Run the test multiple times based on the `run_count` variable"""
            print(f"\n========== Running Iteration {i + 1} of {run_count} ==========\n")

            # open library card page
            self.open_library_card_page()
            print(self.get_current_url())

            # Landing page

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

            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 2 of 5: Address
            # https://www.nypl.org/library-card/location?&newCard=true
            self.wait(2)
            print(self.get_current_url())

            self.send_keys(LibraryCardPage.street_address, "123 East 45th Street")
            self.send_keys(LibraryCardPage.apartment, "3F")
            self.send_keys(LibraryCardPage.city, "New York")
            self.send_keys(LibraryCardPage.state, "NY")
            self.send_keys(LibraryCardPage.zip, "10017")

            #self.assert_element(LibraryCardPage.previous_button)
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
            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 4 of 5: Customize Your Account

            # create a unique username with UUID
            username = f"QaLibUser{uuid.uuid4().hex[:8]}"  # Shortened UUID

            # Retrieve password from environment variables
            password = os.getenv('LCA_PASSWORD')

            # Debug print statements to check if the variables are set
            print(f"\nUsername: {username}")
            print(f"Password: {password}")
            print(f"Email: {email}\n")

            # Ensure username and password are not None
            if not username or not password:
                raise Exception("Environment variables USERNAME and PASSWORD must be set!")

            self.send_keys(LibraryCardPage.username_box, username)
            self.send_keys(LibraryCardPage.password_box, password)
            self.send_keys(LibraryCardPage.verify_password_box, password)
            self.click_with_fallback(LibraryCardPage.show_password)
            self.send_keys(LibraryCardPage.home_library_box, "Stephen A. Schwarzman Building")
            self.click(LibraryCardPage.terms_checkbox)

            print(self.get_current_url())
            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 5 of 5: Confirm Your Information
            #self.assert_element(LibraryCardPage.edit_personal)
            #self.assert_element(LibraryCardPage.edit_address)
            #self.assert_element(LibraryCardPage.edit_create)

            print(self.get_current_url())
            self.click_with_fallback(LibraryCardPage.showPasswordReview)
            self.click(LibraryCardPage.next_button)

    def test_library_card_new_6(self):
        # https://www.nypl.org/library-card/new
        print("test_library_card_new()\n")

        for i in range(run_count):
            """Run the test multiple times based on the `run_count` variable"""
            print(f"\n========== Running Iteration {i + 1} of {run_count} ==========\n")

            # open library card page
            self.open_library_card_page()
            print(self.get_current_url())

            # Landing page

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

            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 2 of 5: Address
            # https://www.nypl.org/library-card/location?&newCard=true
            self.wait(2)
            print(self.get_current_url())

            self.send_keys(LibraryCardPage.street_address, "123 East 45th Street")
            self.send_keys(LibraryCardPage.apartment, "3F")
            self.send_keys(LibraryCardPage.city, "New York")
            self.send_keys(LibraryCardPage.state, "NY")
            self.send_keys(LibraryCardPage.zip, "10017")

            #self.assert_element(LibraryCardPage.previous_button)
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
            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 4 of 5: Customize Your Account

            # create a unique username with UUID
            username = f"QaLibUser{uuid.uuid4().hex[:8]}"  # Shortened UUID

            # Retrieve password from environment variables
            password = os.getenv('LCA_PASSWORD')

            # Debug print statements to check if the variables are set
            print(f"\nUsername: {username}")
            print(f"Password: {password}")
            print(f"Email: {email}\n")

            # Ensure username and password are not None
            if not username or not password:
                raise Exception("Environment variables USERNAME and PASSWORD must be set!")

            self.send_keys(LibraryCardPage.username_box, username)
            self.send_keys(LibraryCardPage.password_box, password)
            self.send_keys(LibraryCardPage.verify_password_box, password)
            self.click_with_fallback(LibraryCardPage.show_password)
            self.send_keys(LibraryCardPage.home_library_box, "Stephen A. Schwarzman Building")
            self.click(LibraryCardPage.terms_checkbox)

            print(self.get_current_url())
            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 5 of 5: Confirm Your Information
            #self.assert_element(LibraryCardPage.edit_personal)
            #self.assert_element(LibraryCardPage.edit_address)
            #self.assert_element(LibraryCardPage.edit_create)

            print(self.get_current_url())
            self.click_with_fallback(LibraryCardPage.showPasswordReview)
            self.click(LibraryCardPage.next_button)

    def test_library_card_new_7(self):
        # https://www.nypl.org/library-card/new
        print("test_library_card_new()\n")

        for i in range(run_count):
            """Run the test multiple times based on the `run_count` variable"""
            print(f"\n========== Running Iteration {i + 1} of {run_count} ==========\n")

            # open library card page
            self.open_library_card_page()
            print(self.get_current_url())

            # Landing page

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

            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 2 of 5: Address
            # https://www.nypl.org/library-card/location?&newCard=true
            self.wait(2)
            print(self.get_current_url())

            self.send_keys(LibraryCardPage.street_address, "123 East 45th Street")
            self.send_keys(LibraryCardPage.apartment, "3F")
            self.send_keys(LibraryCardPage.city, "New York")
            self.send_keys(LibraryCardPage.state, "NY")
            self.send_keys(LibraryCardPage.zip, "10017")

            #self.assert_element(LibraryCardPage.previous_button)
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
            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 4 of 5: Customize Your Account

            # create a unique username with UUID
            username = f"QaLibUser{uuid.uuid4().hex[:8]}"  # Shortened UUID

            # Retrieve password from environment variables
            password = os.getenv('LCA_PASSWORD')

            # Debug print statements to check if the variables are set
            print(f"\nUsername: {username}")
            print(f"Password: {password}")
            print(f"Email: {email}\n")

            # Ensure username and password are not None
            if not username or not password:
                raise Exception("Environment variables USERNAME and PASSWORD must be set!")

            self.send_keys(LibraryCardPage.username_box, username)
            self.send_keys(LibraryCardPage.password_box, password)
            self.send_keys(LibraryCardPage.verify_password_box, password)
            self.click_with_fallback(LibraryCardPage.show_password)
            self.send_keys(LibraryCardPage.home_library_box, "Stephen A. Schwarzman Building")
            self.click(LibraryCardPage.terms_checkbox)

            print(self.get_current_url())
            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 5 of 5: Confirm Your Information
            #self.assert_element(LibraryCardPage.edit_personal)
            #self.assert_element(LibraryCardPage.edit_address)
            #self.assert_element(LibraryCardPage.edit_create)

            print(self.get_current_url())
            self.click_with_fallback(LibraryCardPage.showPasswordReview)
            self.click(LibraryCardPage.next_button)

    def test_library_card_new_8(self):
        # https://www.nypl.org/library-card/new
        print("test_library_card_new()\n")

        for i in range(run_count):
            """Run the test multiple times based on the `run_count` variable"""
            print(f"\n========== Running Iteration {i + 1} of {run_count} ==========\n")

            # open library card page
            self.open_library_card_page()
            print(self.get_current_url())

            # Landing page

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

            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 2 of 5: Address
            # https://www.nypl.org/library-card/location?&newCard=true
            self.wait(2)
            print(self.get_current_url())

            self.send_keys(LibraryCardPage.street_address, "123 East 45th Street")
            self.send_keys(LibraryCardPage.apartment, "3F")
            self.send_keys(LibraryCardPage.city, "New York")
            self.send_keys(LibraryCardPage.state, "NY")
            self.send_keys(LibraryCardPage.zip, "10017")

            #self.assert_element(LibraryCardPage.previous_button)
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
            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 4 of 5: Customize Your Account

            # create a unique username with UUID
            username = f"QaLibUser{uuid.uuid4().hex[:8]}"  # Shortened UUID

            # Retrieve password from environment variables
            password = os.getenv('LCA_PASSWORD')

            # Debug print statements to check if the variables are set
            print(f"\nUsername: {username}")
            print(f"Password: {password}")
            print(f"Email: {email}\n")

            # Ensure username and password are not None
            if not username or not password:
                raise Exception("Environment variables USERNAME and PASSWORD must be set!")

            self.send_keys(LibraryCardPage.username_box, username)
            self.send_keys(LibraryCardPage.password_box, password)
            self.send_keys(LibraryCardPage.verify_password_box, password)
            self.click_with_fallback(LibraryCardPage.show_password)
            self.send_keys(LibraryCardPage.home_library_box, "Stephen A. Schwarzman Building")
            self.click(LibraryCardPage.terms_checkbox)

            print(self.get_current_url())
            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 5 of 5: Confirm Your Information
            #self.assert_element(LibraryCardPage.edit_personal)
            #self.assert_element(LibraryCardPage.edit_address)
            #self.assert_element(LibraryCardPage.edit_create)

            print(self.get_current_url())
            self.click_with_fallback(LibraryCardPage.showPasswordReview)
            self.click(LibraryCardPage.next_button)

    def test_library_card_new_9(self):
        # https://www.nypl.org/library-card/new
        print("test_library_card_new()\n")

        for i in range(run_count):
            """Run the test multiple times based on the `run_count` variable"""
            print(f"\n========== Running Iteration {i + 1} of {run_count} ==========\n")

            # open library card page
            self.open_library_card_page()
            print(self.get_current_url())

            # Landing page

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

            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 2 of 5: Address
            # https://www.nypl.org/library-card/location?&newCard=true
            self.wait(2)
            print(self.get_current_url())

            self.send_keys(LibraryCardPage.street_address, "123 East 45th Street")
            self.send_keys(LibraryCardPage.apartment, "3F")
            self.send_keys(LibraryCardPage.city, "New York")
            self.send_keys(LibraryCardPage.state, "NY")
            self.send_keys(LibraryCardPage.zip, "10017")

            #self.assert_element(LibraryCardPage.previous_button)
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
            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 4 of 5: Customize Your Account

            # create a unique username with UUID
            username = f"QaLibUser{uuid.uuid4().hex[:8]}"  # Shortened UUID

            # Retrieve password from environment variables
            password = os.getenv('LCA_PASSWORD')

            # Debug print statements to check if the variables are set
            print(f"\nUsername: {username}")
            print(f"Password: {password}")
            print(f"Email: {email}\n")

            # Ensure username and password are not None
            if not username or not password:
                raise Exception("Environment variables USERNAME and PASSWORD must be set!")

            self.send_keys(LibraryCardPage.username_box, username)
            self.send_keys(LibraryCardPage.password_box, password)
            self.send_keys(LibraryCardPage.verify_password_box, password)
            self.click_with_fallback(LibraryCardPage.show_password)
            self.send_keys(LibraryCardPage.home_library_box, "Stephen A. Schwarzman Building")
            self.click(LibraryCardPage.terms_checkbox)

            print(self.get_current_url())
            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 5 of 5: Confirm Your Information
            #self.assert_element(LibraryCardPage.edit_personal)
            #self.assert_element(LibraryCardPage.edit_address)
            #self.assert_element(LibraryCardPage.edit_create)

            print(self.get_current_url())
            self.click_with_fallback(LibraryCardPage.showPasswordReview)
            self.click(LibraryCardPage.next_button)

    def test_library_card_new_10(self):
        # https://www.nypl.org/library-card/new
        print("test_library_card_new()\n")

        for i in range(run_count):
            """Run the test multiple times based on the `run_count` variable"""
            print(f"\n========== Running Iteration {i + 1} of {run_count} ==========\n")

            # open library card page
            self.open_library_card_page()
            print(self.get_current_url())

            # Landing page

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

            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 2 of 5: Address
            # https://www.nypl.org/library-card/location?&newCard=true
            self.wait(2)
            print(self.get_current_url())

            self.send_keys(LibraryCardPage.street_address, "123 East 45th Street")
            self.send_keys(LibraryCardPage.apartment, "3F")
            self.send_keys(LibraryCardPage.city, "New York")
            self.send_keys(LibraryCardPage.state, "NY")
            self.send_keys(LibraryCardPage.zip, "10017")

            #self.assert_element(LibraryCardPage.previous_button)
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
            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 4 of 5: Customize Your Account

            # create a unique username with UUID
            username = f"QaLibUser{uuid.uuid4().hex[:8]}"  # Shortened UUID

            # Retrieve password from environment variables
            password = os.getenv('LCA_PASSWORD')

            # Debug print statements to check if the variables are set
            print(f"\nUsername: {username}")
            print(f"Password: {password}")
            print(f"Email: {email}\n")

            # Ensure username and password are not None
            if not username or not password:
                raise Exception("Environment variables USERNAME and PASSWORD must be set!")

            self.send_keys(LibraryCardPage.username_box, username)
            self.send_keys(LibraryCardPage.password_box, password)
            self.send_keys(LibraryCardPage.verify_password_box, password)
            self.click_with_fallback(LibraryCardPage.show_password)
            self.send_keys(LibraryCardPage.home_library_box, "Stephen A. Schwarzman Building")
            self.click(LibraryCardPage.terms_checkbox)

            print(self.get_current_url())
            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 5 of 5: Confirm Your Information
            #self.assert_element(LibraryCardPage.edit_personal)
            #self.assert_element(LibraryCardPage.edit_address)
            #self.assert_element(LibraryCardPage.edit_create)

            print(self.get_current_url())
            self.click_with_fallback(LibraryCardPage.showPasswordReview)
            self.click(LibraryCardPage.next_button)

    def test_library_card_new_11(self):
        # https://www.nypl.org/library-card/new
        print("test_library_card_new()\n")

        for i in range(run_count):
            """Run the test multiple times based on the `run_count` variable"""
            print(f"\n========== Running Iteration {i + 1} of {run_count} ==========\n")

            # open library card page
            self.open_library_card_page()
            print(self.get_current_url())

            # Landing page

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

            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 2 of 5: Address
            # https://www.nypl.org/library-card/location?&newCard=true
            self.wait(2)
            print(self.get_current_url())

            self.send_keys(LibraryCardPage.street_address, "123 East 45th Street")
            self.send_keys(LibraryCardPage.apartment, "3F")
            self.send_keys(LibraryCardPage.city, "New York")
            self.send_keys(LibraryCardPage.state, "NY")
            self.send_keys(LibraryCardPage.zip, "10017")

            #self.assert_element(LibraryCardPage.previous_button)
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
            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 4 of 5: Customize Your Account

            # create a unique username with UUID
            username = f"QaLibUser{uuid.uuid4().hex[:8]}"  # Shortened UUID

            # Retrieve password from environment variables
            password = os.getenv('LCA_PASSWORD')

            # Debug print statements to check if the variables are set
            print(f"\nUsername: {username}")
            print(f"Password: {password}")
            print(f"Email: {email}\n")

            # Ensure username and password are not None
            if not username or not password:
                raise Exception("Environment variables USERNAME and PASSWORD must be set!")

            self.send_keys(LibraryCardPage.username_box, username)
            self.send_keys(LibraryCardPage.password_box, password)
            self.send_keys(LibraryCardPage.verify_password_box, password)
            self.click_with_fallback(LibraryCardPage.show_password)
            self.send_keys(LibraryCardPage.home_library_box, "Stephen A. Schwarzman Building")
            self.click(LibraryCardPage.terms_checkbox)

            print(self.get_current_url())
            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 5 of 5: Confirm Your Information
            #self.assert_element(LibraryCardPage.edit_personal)
            #self.assert_element(LibraryCardPage.edit_address)
            #self.assert_element(LibraryCardPage.edit_create)

            print(self.get_current_url())
            self.click_with_fallback(LibraryCardPage.showPasswordReview)
            self.click(LibraryCardPage.next_button)

    def test_library_card_new_12(self):
        # https://www.nypl.org/library-card/new
        print("test_library_card_new()\n")

        for i in range(run_count):
            """Run the test multiple times based on the `run_count` variable"""
            print(f"\n========== Running Iteration {i + 1} of {run_count} ==========\n")

            # open library card page
            self.open_library_card_page()
            print(self.get_current_url())

            # Landing page

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

            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 2 of 5: Address
            # https://www.nypl.org/library-card/location?&newCard=true
            self.wait(2)
            print(self.get_current_url())

            self.send_keys(LibraryCardPage.street_address, "123 East 45th Street")
            self.send_keys(LibraryCardPage.apartment, "3F")
            self.send_keys(LibraryCardPage.city, "New York")
            self.send_keys(LibraryCardPage.state, "NY")
            self.send_keys(LibraryCardPage.zip, "10017")

            #self.assert_element(LibraryCardPage.previous_button)
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
            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 4 of 5: Customize Your Account

            # create a unique username with UUID
            username = f"QaLibUser{uuid.uuid4().hex[:8]}"  # Shortened UUID

            # Retrieve password from environment variables
            password = os.getenv('LCA_PASSWORD')

            # Debug print statements to check if the variables are set
            print(f"\nUsername: {username}")
            print(f"Password: {password}")
            print(f"Email: {email}\n")

            # Ensure username and password are not None
            if not username or not password:
                raise Exception("Environment variables USERNAME and PASSWORD must be set!")

            self.send_keys(LibraryCardPage.username_box, username)
            self.send_keys(LibraryCardPage.password_box, password)
            self.send_keys(LibraryCardPage.verify_password_box, password)
            self.click_with_fallback(LibraryCardPage.show_password)
            self.send_keys(LibraryCardPage.home_library_box, "Stephen A. Schwarzman Building")
            self.click(LibraryCardPage.terms_checkbox)

            print(self.get_current_url())
            #self.assert_element(LibraryCardPage.previous_button)
            self.click(LibraryCardPage.next_button)

            # Step 5 of 5: Confirm Your Information
            #self.assert_element(LibraryCardPage.edit_personal)
            #self.assert_element(LibraryCardPage.edit_address)
            #self.assert_element(LibraryCardPage.edit_create)

            print(self.get_current_url())
            self.click_with_fallback(LibraryCardPage.showPasswordReview)
            self.click(LibraryCardPage.next_button)
