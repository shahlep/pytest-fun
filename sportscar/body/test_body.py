from pytest import mark


@mark.body
class BodyTest:

    @mark.smoke
    @mark.ui
    def test_can_navigate_to_playwright_docs(self, chrome_browser):
        chrome_browser.get("https://playwright.dev/python/docs/intro")
        chrome_browser.close()
        assert True
