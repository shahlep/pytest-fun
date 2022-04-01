from pytest import mark


class EntertainmentTest:
    @mark.entertainment
    @mark.ui
    def test_can_navigate_to_playwright_docs(self, firefox_browser):
        firefox_browser.get("https://playwright.dev/python/docs/intro")
        firefox_browser.close()
        assert True
