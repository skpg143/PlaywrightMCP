#1.Page screenshot (partial/visible)
import datetime

import homepage
import page
from playwright.sync_api import sync_playwright, Page, expect, Playwright
timestamp = datetime.datetime.now().strftime("%y%m%d%H%M%S")
page.goto("url")

page.screenshot(path=f"screenshots/ homepage - {timestamp}.png")
##########################################################################

#2. Full page screenshot
page.screenshots(path=f"screenshots/homepage - {timestamp}.png", full_page = True)

##########################################################################

#3. Element / specific section of the page
featureproducts = page.locator("")
featureproducts.screenshots(path=f"screenshots / featureproducts - {timestamp}.png")





