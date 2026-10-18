import os.path

from playwright.sync_api import sync_playwright, Page, expect


def test_handle_downloads_files(page: Page):

    page.goto("")
    page.locator("").fill("welcome")
    page.locator("").click()

    page.on("download", lambda download : download.save_as("downloads/testfile.txt"))
    page.wait_for_timeout(5000)

    if os.path.exists("downloads/testfile.txt"):
        print("File exists")

    else:
        print("File not exist")
