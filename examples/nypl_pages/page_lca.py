from seleniumbase import BaseCase


class LibraryCardPage(BaseCase):
    # First page
    # languages
    arabic = '//a[contains(text(), "Arabic")]'
    bengali = '//a[contains(text(), "Bengali")]'
    chinese = '//a[contains(text(), "Chinese")]'
    english = '//a[contains(text(), "English")]'
    french = '//a[contains(text(), "French")]'
    haitian = '//a[contains(text(), "Haitian")]'
    korean = '//a[contains(text(), "Korean")]'
    polish = '//a[contains(text(), "Polish")]'
    russian = '//a[contains(text(), "Russian")]'
    spanish = '//a[contains(text(), "Spanish")]'
    urdu = '//a[contains(text(), "Urdu")]'

    # 'get started' button
    get_started = '//a[contains(text(), "Get Started")]'

    # Step 1 of 5: Personal Information
    first_name = "//*[@id='firstName']"
    last_name = "//*[@id='lastName']"
    date_of_birth = "//*[@id='birthdate']"
    email = "//*[@id='email']"

    # Step 2 of 5: Address
    street_address = "//*[@id='line1-home']"
    apartment = "//*[@id='line2-home']"
    city = "//*[@id='city-home']"
    state = "//*[@id='state-home']"
    zip = "//*[@id='zip-home']"

    # Step 3 of 5: Address Verification
    address_verification_1 = "//*[@id='mainContent']//*[contains(text(), 'Please select the correct address')]"
    address_verification_2 = "//*[@id='mainContent']//*[contains(text(), 'Home Address')]"

    # Alternate Address
    alternate_address = "(//*[@id='mainContent']//*[contains(text(), 'Alternate Address')])[1]"
    work_address = "//*[@id='line1-work']"
    work_apartment = "//*[@id='line2-work']"
    work_city = "//*[@id='city-work']"
    work_state = "//*[@id='state-work']"
    work_zip = "//*[@id='zip-work']"

    # Step 4 of 5: Customize Your Account
    username_box = "//*[@id='username']"
    password_box = "//*[@id='password']"
    verify_password_box = "//*[@id='verifyPassword']"
    home_library_box = "//*[@id='librarylist-autosuggest']"
    terms_checkbox = "//*[@id='acceptTerms']"
    show_password = "//*[@id='showPassword']"  # exclusively for Step 4

    # Step 5 of 5: Confirm Your Information
    edit_personal = "//*[@id='editSectionButton-Personal Information']"
    edit_address = "//*[@id='editAddressButton']"
    edit_create = "//*[@id='editSectionButton-Create Your Account']"
    showPasswordReview = '//*[@id="showPasswordReview"]'  # exclusive for Step 5

    # Step 6
    congrats_text = "//*[@id='mainContent']//*[contains(text(), 'Congratulations')]"
    barcode = "//*[@id='barcodeCanvas']"
    barcode_number = "//*[@id='barcodeCanvas']//following-sibling::*"
    member_name = "//*[@id='mainContent']//*[contains(text(), 'MEMBER NAME')]//div"
    issued_date = "//*[@id='mainContent']//*[contains(text(), 'ISSUED')]//div"
    all_links = '(//*[@id="mainContent"]//a)'

    previous_button = '//a[contains(text(), "Previous")]'
    next_button = "//input[@type='submit']"

    def open_library_card_page(self, category=''):
        # self.open("https://www.nypl.org/library-card/new")

        base_url = "https://www.nypl.org/library-card/new"
        qa_base_url = "https://qa-www.nypl.org/library-card/new"

        url = f"{base_url}{category}"
        qa_url = f"{qa_base_url}{category}"

        # Open the appropriate URL based on the environment
        if self.env == "qa":
            print(f"Running on QA Env: Opening {category} page with URL: {qa_url}")
            self.open(qa_url)
        else:
            print(f"Running on Production Env: Opening {category} page with URL: {url}")
            self.open(url)
