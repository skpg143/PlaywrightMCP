from playwright.sync_api import sync_playwright, Page, expect


def test_handle_dialog(page: Page):

    page.goto("url")
    #handle alert
    page.on("dialog", lambda dialog: dialog.accept())
    page.wait_for_timeout(5000)
    page.locator("").click()
    page.wait_for_timeout(5000)

#confirmation dialog
def test_confirmation_dialog(page: Page):

    page.goto("")
    page.on("dialog", lambda dialog: dialog.dismiss())
    page.wait_for_timeout(5000)
    page.locator("").click()
    page.wait_for_timeout(5000)
    text = page.locator("").inner_text()
    print("Output txt: ", text)
    expect(page.locator("").to_contain_text(""))
    page.wait_for_timeout(5000)

#Prompt dialog
def test_prompt_dialog(page: Page):

    page.goto("url")
    page.on("dialog", lambda dialog: dialog.accept('Sandy'))
    page.locator("").click()
    txt = page.locator("").inner_text()
    print(txt)
    expect(txt).to_have_text("Sandy")
    page.wait_for_timeout(5000)

