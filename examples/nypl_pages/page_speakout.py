from seleniumbase import BaseCase


class SpeakoutPage(BaseCase):

    # Step 1 of 5: Personal Information
    first_name = "//*[@id='firstName']"
    last_name = "//*[@id='lastName']"
    date_of_birth = "//*[@id='birthdate']"

    # Step 2 of 5: Address
    street_address = "//*[@id='addressLine1']"  # address line 1
    apartment = "//*[@id='addressLine2']"  # address line 2
    city = "//*[@id='locality']"
    state = "//*[@id='administrativeArea']"
    postal = "//*[@id='postalCode']"
    email = "//*[@id='email']"
    favorite_location = "//*[@id='favoriteLocation']"

    send_letter = "//*[@type='submit']"
    district_rep = '//*[contains(text(), "Your letter will go to")]'  # district representative

    def open_speakout_page(self, category=''):
        # self.open("https://www.nypl.org/speakout")

        base_url = "https://www.nypl.org/speakout"
        # qa_base_url = "https://qa-www.nypl.org/speakout"
        qa_base_url = "https://scout-git-reno-4508-locations-dropdown-nypl.vercel.app/speakout"

        url = f"{base_url}{category}"
        qa_url = f"{qa_base_url}{category}"

        # Open the appropriate URL based on the environment
        if self.env == "qa":
            print(f"Running on QA Env: Opening {category} page with URL: {qa_url}")
            self.open(qa_url)
        else:
            print(f"Running on Production Env: Opening {category} page with URL: {url}")
            self.open(url)
