from playwright.sync_api import sync_playwright, Page, expect, Playwright

from PlaywrightBuiltIn_Locator.get_by_text import browser


def test_record_video(page: Page, playwright: Playwright):

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(record_video_dir="video/", record_video_size = {"width" : 1024, "height" : 768})
    page.context.new_page()

    ############### Login code here #####################
    context.close()
    browser.close()