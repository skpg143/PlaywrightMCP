from playwright.sync_api import sync_playwright, Page

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page: Page = browser.new_page()
    page.goto("https://www.w3schools.com/html/html_forms.asp")
    page.get_by_placeholder("Enter your name").click()