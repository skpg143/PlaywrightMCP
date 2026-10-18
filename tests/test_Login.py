from playwright.sync_api import sync_playwright

def test_login():
    print("Test started", flush=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print("Browser launched", flush=True)

        page.goto("https://www.google.com/")
        print(2 + 3, flush=True)

        page.wait_for_timeout(5000)  # Wait for 5 seconds to see the page
        browser.close()
