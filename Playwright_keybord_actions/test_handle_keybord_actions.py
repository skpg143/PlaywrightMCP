from playwright.sync_api import sync_playwright, Page, expect


def test_handle_focus_on(page: Page):

    page.goto("")
    input1 = page.locator("")

    #focus on input
    input1.focus()

    #enter the text in the input
    page.locator("").fill("welcome")

    #ctr + A select all element
    page.keyboard.press("ctr + A")

    #ctr + c copy the element
    page.keyboard.press("ctr + c")

    #press tab two times to navigate / focus o input2
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")

    #ctr + v paste the element
    page.keyboard.press("ctr + v")







