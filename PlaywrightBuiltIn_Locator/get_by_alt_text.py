from playwright.sync_api import sync_playwright, Page

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.get_by_alt_text("Google").click()