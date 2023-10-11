from seleniumbase import BaseCase


class RequestVisitPage(BaseCase):
    home = '(//*[contains(text(), "Home")])[1]'
    locations = '(//*[contains(text(), "Locations")])[3]'

    location_dropdown = '//*[@id="request-visit-library-select"]'
    location_selection = '//*[@name="library"]//option'
    visit_type_dropdown = '//*[@id="request-visit-select-type"]'
    visit_type_selection = '//*[@name="visitType"]//option'
    virtual_visit = '//*[text()="Virtual Visit"]'
    in_person_visit = '//*[text()="In-Person Visit"]'

    reader_advisory = '//*[@id="reader-advisory-wrapper"]/label/span[1]'  # visible after clicking 'Virtual Visit'
    group_tour = '//*[@id="inPersonServices-wrapper"]/label/span[1]'  # visible after clicking 'In-Person Visit'

    school_or_organization = '//*[@id="organization"]'

    # age range
    kids = '//*[@id="age-group-0-wrapper"]/label/span[2]'
    teens = '//*[@id="age-group-1-wrapper"]/label/span[2]'
    adults = '//*[@id="age-group-2-wrapper"]/label/span[2]'

    contact_name = '//*[@id="contactName"]'
    contact_email = '//*[@id="contactEmail"]'

    submit = '//*[@id="request-visit-form-button"]'
    warning = '//*[text()="There was a problem with your submissions. Errors have been highlighted below."]'

    def open_request_visit_page(self):
        # self.open("https://www.nypl.org/locations/request-visit")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/locations/request-visit")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/locations/request-visit")
