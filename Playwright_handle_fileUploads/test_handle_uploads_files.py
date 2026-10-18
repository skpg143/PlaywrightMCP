from playwright.sync_api import sync_playwright, Page, expect


def test_handle_upload_file(page: Page):

    page.goto("")

    page.locator("").set_input_files("folder/testfile.txt")
    page.locator("").click()

    expect(page.locator("")).to_contain_text("testfile.txt")
    print("File uploading............")
    page.wait_for_timeout(5000)

#######################################################################
# upload multiple file
def test_handle_upload_multiple_files(page: Page):

    files = ["folderName\testFile1.txt", "folderName\testfile2.txt"]
    page.locator("").set_input_files(files)
    page.locator("").click()
    page.wait_for_timeout(5000)

    