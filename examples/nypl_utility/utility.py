from seleniumbase import BaseCase
from examples.nypl_pages.page_header import HeaderPage
from examples.nypl_pages.page_schwarzman import SchwarzmanPage


class NyplUtils(HeaderPage, SchwarzmanPage):

    # nypl login method for the catalog
    def nypl_login_catalog(self, username, password):
        # click login button
        self.click(self.login)
        # click 'log into the catalog'
        self.click(self.login_catalog)
        # enter username
        self.send_keys(self.username, username)
        # enter password
        self.send_keys(self.password, password)
        # click submit
        self.click(self.submit)

    # nypl login method for the research
    def nypl_login_research(self, username, password):
        # click login button
        self.click(self.login)
        # click log into the research catalog
        self.click(self.login_research_catalog)
        # enter username
        self.send_keys(self.username, username)
        # enter password
        self.send_keys(self.password, password)
        # click submit
        self.click(self.submit)

    # click a link and assert the text in the URL
    def text_assertion(self, link, text):
        self.click(link)
        # assert the text in the URL
        self.assert_true(text in self.get_current_url())
        # go to the previous page
        self.go_back()
