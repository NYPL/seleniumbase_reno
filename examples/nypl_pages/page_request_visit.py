from seleniumbase import BaseCase


class RequestVisitPage(BaseCase):
    home = '(//*[contains(text(), "Home")])[1]'
    locations = '(//*[contains(text(), "Locations")])[3]'

    location_dropdown = '//*[@id="request-visit-library-select"]'
    location_selection = '//*[@name="library"]//option'
    visit_type_dropdown = '//*[@id="request-visit-select-type"]//..'
    visit_type_selection = '//*[@name="visitType"]//option'
    virtual_visit = '//*[text()="Virtual Visit"]'
    in_person_visit = '//*[text()="In-Person Visit"]'

    reader_advisory = '//*[@id="services-container"]//*[contains(text(), "Reader Advisory")]'  # visible after clicking 'Virtual Visit'
    group_tour = '//*[@id="request-type"]//*[contains(text(), "Group Tour")]'  # visible after clicking 'In-Person Visit'

    school_or_organization = '//*[@id="organization"]'

    # age range
    kids = "(//*[@data-testid='ds-checkbox']//*[contains(., 'Kids')])[1]"
    teens = "(//*[@data-testid='ds-checkbox']//*[contains(., 'Teens')])[1]"
    adults = "(//*[@data-testid='ds-checkbox']//*[contains(., 'Adults')])[1]"

    contact_name = '//*[@id="contactName"]'
    contact_email = '//*[@id="contactEmail"]'

    submit = '//*[@id="request-visit-form-button"]'
    warning = '//*[text()="There was a problem with your submissions. Errors have been highlighted below."]'

    def open_request_visit_page(self):
        prod_url = "https://www.nypl.org/locations/request-visit"
        qa_url = "https://qa-www.nypl.org/locations/request-visit"

        if self.env == "qa":
            print("Running on QA Env")
            self.open(qa_url)

        else:
            print("Running on Production Env")
            self.open(prod_url)
