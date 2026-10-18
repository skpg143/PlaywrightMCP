from playwright.sync_api import  sync_playwright, Page, expect

def test_handle_radioButton(page: Page):

    page.goto("https://www.ironspider.ca/forms/checkradio.htm")

    male_radio_button = page.locator("Male")

    #visible of the element and enable or not
    expect(male_radio_button).to_be_visible()
    expect(male_radio_button).to_be_enabled()
    
    #male radio button should not be checked
    expect(male_radio_button).not_to_be_checked()

    #select male radio button-action
    male_radio_button.check()
    expect(male_radio_button).to_be_checked()

