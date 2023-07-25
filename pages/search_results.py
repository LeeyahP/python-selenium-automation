import time

from pages.base_page import Page


class SearchResultsPage(Page):

    def verify_body_text (self, search_query):
        time.sleep(2)
        actual_url = self.driver.current_url
        assert search_query.lower() in actual_url, f"Expected {search_query} in the URL ({actual_url}, but could not find)"
