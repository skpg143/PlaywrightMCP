import csv
import json

import pytest

from playwright.sync_api import sync_playwright, Page, expect, Playwright

search_items = ["laptop", "gift card", "smart phone"]

@pytest.mark.parametrize("item", search_items)
def test_search_item(item, page: Page):
    page.locator("#small-serchitems").fill(item)
    page.locator("input[value='search']").click()

    first_result = page.locator("h2 a").nth(0)
    expect(first_result).to_contain_text(item, ignore_case=True)

##################################################################################
# Data driven testing from external files

#1. Data.json -> for api testing

import pytest
from playwright.sync_api import expect, Page

file = open("testdata / Data.json", "r")
login_data = json.load(file)

@pytest.mark.parametrize("email", "pass", "validity",[(data["email"], data["password"], data["validity"]) for data in login_data])
def test_login_data_driven(email, password, validit, page: Page):

    page.locator('#Email').fill(email)
    page.locator("#password").fill(password)
    page.locator("input[value='Log-in']").click()

    #Validation
    if validit == "valid":
        logout_link = page.locator("a[href='/logout']")
        expect(logout_link).to_be_visible()

    else:
        error_msg = page.locator("")
        expect(error_msg).to_be_visible(timeout=5000)
        expect(page).to_have_url("url")

#######################################################################################

#2. Data.csv -> for web testing
import pytest
from playwright.sync_api import sync_playwright, Page, Playwright, expect

login_data = []
#read csv files
csv_file = open("testdata/data.csv", newline="", encoding='utf-8')
reader = csv.DictReader(csv_file)

for data in reader:
    login_data.append(data["email"], data["password"], data["validity"])

@pytest.mark.parametrize("email", "password", "validity", [(data["email"], data["password"], data["validity"]) for data in login_data])
def test_login_data_driven_csv(email, password, validity, page: Page):

    page.goto("url")
    page.locator("#email").fill(email)
    page.locator("#password").fill("password")
    page.locator("#button").click()

    #validation
    if validity == "valid":
        logout_link = page.locator("")
        expect(logout_link).to_be_visible(timeout=5000)
    else:
        expect(page).to_have_url("url")

################################################################################
#3. Data.xlsx ->

import pytest
from playwright.sync_api import sync_playwright, expect, Playwright, Page

import openpyxl

webwork = openpyxl.load_workbook("testdata/Data.xlsx")
sheet = webwork.active
for row in sheet.iter_rows(min_row=2, values_only=True):
    email, password, validity = row
    login_data.append((str(email or ""), str(password or ""), (validity or "")))

webwork.close()




