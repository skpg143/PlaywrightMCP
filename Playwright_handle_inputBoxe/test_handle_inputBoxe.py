from playwright.sync_api import sync_playwright, Page, expect


def test_handle_input_box(page: Page):

    page.goto("https://www.w3schools.com/html/html_forms.asp")
    text_box = page.locator("#email")

    #visibility of the element and enabled or not
    expect(text_box).to_be_visible()
    expect(text_box).to_be_enabled()

    #check the attribute of the element
    expect(text_box).to_have_attribute("name", "email")

    #get the attribute of the element
    maxlength = text_box.get_attribute("maxlength")
    print(f"Max length of the input box is: {maxlength}")

    #fill the text box with some value
    text_box.fill("test@example.com")

    #get the input value from the input box
    entervalue = text_box.input_value()
    print(f"Entered value in the input box is: {entervalue}")
    page.wait_for_timeout(2000)  # Wait for 2 seconds to see the filled value