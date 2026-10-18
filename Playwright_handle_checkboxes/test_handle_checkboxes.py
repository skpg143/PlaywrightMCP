import pytest

from playwright.sync_api import sync_playwright, Page, expect


def test_handle_checkboxes(page: Page):
    #1.select specific checkbox(Sunday)
    sunday_checkbox = page.get_by_label("Sunday")
    sunday_checkbox.check()
    expect(sunday_checkbox).to_be_checked()
    page.wait_for_timeout(5000)

#####################################################################
    #2.count number of checkboxes
    #Step1
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    checkboxes = []

    #Step2
    for day in days:
        checkbox = page.get_by_label(day)
        checkboxes.append(checkbox)

    #OR

    checkboxes = [page.get_by_label(day) for day in days]
    print(f"Number of checkboxes: {len(checkboxes)}")


###########################################################################
    #3.select all checkboxes
    for checkbox in checkboxes:
        checkbox.check()
        expect(checkbox).to_be_checked()

    page.wait_for_timeout(5000)

###########################################################################
    #4.select / check last three checkboxes
    for checkbox in checkboxes[-3:]:
        checkbox.check()
        expect(checkbox).to_be_checked()

    page.wait_for_timeout(5000)

###########################################################################
    #5.toggle checkboxes (some check and some uncheck)
    for checkbox in checkboxes:
        if checkbox.is_checked():
            checkbox.uncheck()
            expect(checkbox).not_to_be_checked()
        else:
            checkbox.check()
            expect(checkbox).to_be_checked()

    page.wait_for_timeout(5000)

############################################################################
    #6.Randomly select checkboxes
    index=[1,3,5]
    for i in index:
        checkbox = checkboxes[i]
        checkbox.check()
        expect(checkbox[i]).to_be_checked()

    page.wait_for_timeout(5000)

#####################################################################
    #7.select checkboxes behalf of the label / input value
    weekday = "Sunday"
    for lable in days:
        if lable == weekday:
            checkbox = page.get_by_label(lable)
            checkbox.check()
            expect(checkbox).to_be_checked()

    page.wait_for_timeout(5000)





