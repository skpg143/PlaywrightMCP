from playwright.sync_api import sync_playwright, Page, expect, Playwright

from PlaywrightBuiltIn_Locator.get_by_text import browser


def test_handle_tab(page: Page, playwright: Playwright):

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    parent_page = context.new_page()
    page.goto("url")

    #Register an event for handle tab
    #parent_page.on(event="page", lambda page: page.wait_for_load_state())

    parent_page.locator("").click()
    parent_page.wait_for_timeout(5000)
    
    all_pages = context.pages
    print(len(all_pages))

    print("parent page / tab", all_pages[0].title())
    print("child page / tab", all_pages[1].title())

    child_page = all_pages[1]
    print("url", child_page.url)




