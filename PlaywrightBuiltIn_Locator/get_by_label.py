from playwright.sync_api import sync_playwright, Page

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.get_by_lablel("Username").fill("my_username")