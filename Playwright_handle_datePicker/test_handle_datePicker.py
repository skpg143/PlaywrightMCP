from playwright.sync_api import sync_playwright, Page, expect


def test_handle_datePicker(page: Page):

    page.goto("url")

    #Selecting month and year from the data picker
    target_month = ""
    target_year = ""
    is_future = ""
    while True:
        current_month = page.locator("").text_content()
        current_year = page.locator("").text_content()

        if current_month == target_month and current_year == target_year:
            break

        if is_future == True:
            page.locator("").click()

        else:

            page.locator("").click()

    #select all date from the date picker
    all_dates = page.locator("").all()
    target_date=""
    for dt in all_dates:
        date_text = dt.inner_text()

        if date_text == target_date:
            dt.click()
            break

#############################################################################
#JQuery Date Picker
def test_jquery_datepicker(page: Page, year, month, is_future):

    page.goto("url")

    date_input = page.locator("")
    #Approach1
    date_input.fill("10/15/2025")

    #Approach2
    is_future = False
    year = "2024"
    month = "October"
    date = "15"
    date_input.click()
    test_jquery_datepicker(page, year, month, is_future)
    print("select date ==>", date_input.input_value())
    page.wait_for_timeout(5000)

###############################################################################
# Bootstrap checkin Date Picker / make my trip date picker
month=""
year=""
def select_checkin_date(page: Page, year, month, day):
    while True:
        checkin_month_year = page.locator("").nth(0).inner_text()
        current_month, current_year = checkin_month_year.split("")
        if current_month == month and current_year == year:
            break

        else:
            page.locator("").click()

    all_dates = page.locator("").nth(0).locator('td').all()
    for date in all_dates:
        if date.inner_text() == 'day':
            date.click()
            break

########################################################################3
# Checkout date picker

def test_select_checkout_date(page: Page, year, month, day):

    while True:

        checkout_month_year = page.locator("").nth(1).inner_text()
        current_month, current_year = checkout_month_year.split(" ")

        if current_month == month and current_year == year:
            break

        else:
            page.locator("").click()

##########################################################################

# Booking date picker
def test_booking_datePicker(page: Page):
    
    page.goto("url")
    page.get_by_test_id("").click()

    test_select_checkout_date(page, '2005', "October",  "10")
    test_select_checkout_date(page, '2005', "November", '5')

    checkin_text = page.locator("").inner_text()
    checkout_text = page.locator("").inner_text()

    print("Checkin text:", checkout_text)
    print("checkout text:", checkout_text)

    expect(page.locator("")).to_contain_text("checkin_text")
    expect(page.locator("")).to_contain_text("checkout_text")
    page.wait_for_timeout(5000)







