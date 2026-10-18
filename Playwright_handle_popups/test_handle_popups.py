from playwright.sync_api import sync_playwright, Page, expect, Playwright


def test_handle_popup(page: Page, playwright: Playwright):

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("url")
    #page.on("popup", lambda popup : popup_wait_load_state())
    page.locator("#popup").click()
    page.wait_for_timeout(5000)

    #count number of popup on the page context
    all_popups = context.pages
    print(len(all_popups))

    #capture url of all the popup pages
    for pw in all_popups:
        print("Popup :", pw.url)
        title=pw.title()

        if "playwright" in title:
            page.locator("").click()
            expect(pw).to_have_title("")
            pw.close() #popup window close

    page.wait_for_timeout(5000)
    context.close()
    browser.close()



