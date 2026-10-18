from playwright.sync_api import Page, sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.get_by_title("title")