import playwright.sync_api
from playwright.sync_api import sync_playwright, Page, expect, Playwright


def test_capture_tracingData(page: Page, playwright: Playwright):

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    #start tracing
    context.tracing.start(screenshots=True, snapshots=True)
    page = context.new_page()

    ##### login code here###################################

    #stop tracing
    context.tracing.stop(path="trace.zip")
    context.close()
    browser.close()

