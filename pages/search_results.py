from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC


class SearchResultsPage(Page):

    def verify_body_text(self, search_query):
        self.wait.until(EC.url_contains(search_query))