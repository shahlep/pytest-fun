from pytest import mark


@mark.body
class BodyTest:

    @mark.smoke
    @mark.ui
    def test_can_navigate_to_playwright_docs(self, firefox_browser):
        firefox_browser.get("https://demo.playwright.dev/todomvc")
        firefox_browser.close()
        assert True
