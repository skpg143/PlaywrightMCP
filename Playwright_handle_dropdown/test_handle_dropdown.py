from itertools import count

from playwright.sync_api import sync_playwright, Page, expect


def test_handle_dropdown(page: Page):

    #1. select by label
    page.locator("select#dropdown").select_option("India")

    #2. select by value
    page.locator("select#dropdown").select_option("Germany")

    #3. select by index
    page.locator("select#dropdown").select_option(index=3)

    #check number in dropdown
    dropdown_options = page.locator("select#dropdown option")
    expect(dropdown_options).to_have_count(4)

    option_text = [text.strip() for text in dropdown_options.all_text_contents()]
    print(option_text)

    #print cuntries using for loop
    for option in option_text:
        print(option)
    page.wait_for_timeout(2000)

###################################################################################
# Multi select dropdown
def test_handle_multi_select_dropdown(page: Page):
    #1. select by label
    page.locator("select#multi-select").select_option(["India", "Germany"])

    #2. select by value
    page.locator("select#multi-select").select_option(["Spain", "Italy"])

    #3. select by index
    page.locator("select#multi-select").select_option([0, 1])

    #check number in dropdown
    dropdown_options = page.locator("select#multi-select option")
    expect(dropdown_options).to_have_count(4)

    option_text = [text.strip() for text in dropdown_options.all_text_contents()]
    print(option_text)

    #print cuntries using for loop
    for option in option_text:
        print(option)
    page.wait_for_timeout(2000)

#########################################################################################
# Bootstrap dropdown / hiden dropdown
def test_handle_bootstrap_dropdown(page: Page):
    page.goto("https://www.hyrtutorials.com/p/bootstrap-dropdown-demo.html")

    #login step
    page.locator("div#dropdownname").fill("John Doe")
    page.locator("div#dropdownemail").fill("john@gmail.com")
    page.locator("button#dropdownButton").click()
    page.wait_for_timeout(2000)

    #click on pim
    page.get_by_text("PIM").click()
    page.locator("").nth(2).click()
    page.wait_for_timeout(2000)

    #capture all the options in the dropdown
    dropdown_options = page.locator("ul.dropdown-menu li a")
    count = dropdown_options.count()
    print("Number of options in the dropdown:", count)
    expect(dropdown_options).to_have_count(count)
    page.wait_for_timeout(2000)

    #print all the options in the dropdown
    print("all the options in the dropdown:", dropdown_options.all_text_contents())

    #print all the options in the dropdown using for loop
    for i in range(count):
        print(dropdown_options.nth(i).text_content())

    #select / click on specific option in the dropdown
    for i in range(count):
        option_text = dropdown_options.nth(i).inner_text()
        if option_text == "manager":
            dropdown_options.nth(i).click()
            print("Selected option:", option_text)
            break

    select_value = page.locator("div#dropdownButton").input_value()
    print("Selected value in the dropdown:", select_value)


