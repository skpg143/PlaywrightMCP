from playwright.sync_api import sync_playwright, Page


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page: Page = browser.new_page()
    page.goto("https://example.com")
    page.get_by_test_id("submit-button").click()