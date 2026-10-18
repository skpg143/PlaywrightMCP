from pydoc import text

import has
from playwright.sync_api import sync_playwright, Page, expect


def test_handle_input_box(page: Page):
    page.goto("https://www.w3schools.com/html/html_forms.asp")

    #Locate tabl
    table = page.locator("#table")
    expect(table).to_be_visible()

    #1. Count the total number of rows in the table
    rows = table.locator("tr")
    expect(rows).to_equal(4)
    rows_count = rows.count()
    print(f"Total number of rows in the table: {rows_count}")

    #2. Count the total number of columns / header in the table
    columns = rows.locator("th")
    expect(columns).to_equal(3)
    columns_count = columns.count()
    print('Number of columns / headers in a table :', columns_count)

    #3. Read all the data from the table and print it in the console
    second_row_cells = rows.nth(1).locator("td")
    second_row_texts = second_row_cells.all_inner_texts()
    expect(second_row_texts).to_have_text(["Cell 1", "Cell 2", "Cell 3"])
    print("Data from the second row of the table:", second_row_texts)

    for text in second_row_texts:
        print(text)


    #4. Read all the data from the table
    all_row_data = rows.all()
    print("Print all the data from the table rows and columns")
    for row in all_row_data[1:]:
        cols = row.locator('td').all_inner_texts()
        print(cols)

    #5. Printing Book name who's autor name is Mukesh
    print("Printing Books name written by Mukesh ")
    for row in all_row_data[1:]:
        author_name = row.locator('td').nth(1).inner_text()

        if author_name == 'Mukesh':
            book_name = row.locator('td').nth(0).inner_text()
            print(f"{author_name} \t {book_name}")

    #6. Calculate total price of all books
    print("Printing data from all the rows and columns")

    for row in all_row_data[1:]:
        cols = row.locator('td').all_inner_texts()
        print(cols)

        total_price = row.locator('td').nth(3).inner_text()
        total_price += int(total_price)

    print("Total price :", total_price)

#######################################################################################

# Pagination Table
from playwright.sync_api import sync_playwright, Page, Playwright, expect

def test_handle_pagination_tableData(page: Page):

    page.got("url")
    has_more_pages = True

    while has_more_pages:
        rows = page.locator("").all()
        for row in rows:
            print(row.inner_text())

    page.wait_for_timeout(2000)
    next_button = page.locator("")
    is_disabled = next_button.get_attribute("")

    if "disabled" in is_disabled:
        has_more_pages = False
    else:

        next_button.click()

def test_filter_rows(page: Page):
    page.goto("url")
    dropdown = page.locator("")
    dropdown.select_option(label="25")
    rows = page.locator("")
    expect(rows).to_have_count(25)

##############################################################################

# Handling dynamic table when column and row are not constant
from playwright.sync_api import sync_playwright, expect, Playwright, Page

def test_handle_dynamic_tableData(page: Page):

    page.goto("url")

    #Get all the rows from the table
    table = page.locator("")
    rows = table.locator('tr').all()
    CPU_loads = ""

    for row in rows:
        process_name = row.locator('td').nth(0).inner_text()

        if process_name == "Chrome":
            CPU_loads = row.locator("td:has_text('%')").inner_text()
            print("CPU loads of the chrome", CPU_loads)
            break

    expect(page.locator("#chrome-cpu").to_contain_text(CPU_loads))
    page.wait_for_timeout(3000)



