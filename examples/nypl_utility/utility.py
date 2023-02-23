from seleniumbase import BaseCase
from examples.nypl_pages.page_header import Header


class NyplUtils(Header):

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
