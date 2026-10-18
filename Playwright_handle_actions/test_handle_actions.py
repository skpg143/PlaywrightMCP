from playwright.sync_api import sync_playwright, Page, expect

def test_handle_mouseHover_action(page: Page):

    page.goto("url")
    point_me = page.locator("")
    point_me.hover()
    page.wait_for_timeout(5000)

#Right click
def test_handle_rightClick_action(page: Page):

    button = page.locator("")
    button.click()
    page.wait_for_timeout(5000)

#Double click
def test_handle_doubleClick_action(page: Page):

    button = page.locator("")
    button.dblclick()
    page.wait_for_timeout(5000)

#Drag and drop
def test_handle_dragAndDrop_action(page: Page):
     source = page.locator("")
     target = page.locator("")
     source.drag_to(target)
     page.wait_for_timeout(5000)