from playwright.sync_api import sync_playwright, Page

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.w3schools.com/html/html_forms.asp")
    page.get_by_text("Google Search").click()