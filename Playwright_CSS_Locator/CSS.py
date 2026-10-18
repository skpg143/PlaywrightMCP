
#1. button[name='start'], button[name='stop']
#2. button[name^='st'] => Starts-with
#3. button[name*='st'] => contains()

################ Dynamic xpath #########################
# page.locator("//button[@name='start' or @name='stop']")
# page.locator("//button[starts-with(@name,'st')]")
# page.locator("//button[contains(@name,'st')]")
# page.locator(text()="Start" or text()="Stop")

################ Xpath and CSS in Selenium #########################
#a. Abslute xpath / Full xpath
#b. Relative xpath / Partial xpath
#c. contains() => xpath
#page.locator("h2/a[contains(@href, 'computer')]")
#print("First computer product", product.first.text_content())
#print("First computer product", product.last.text_content())
#print("First computer product", product.nth(3).text_content())

#4. Start-with() => xpath
#page.locator("h2/a[starts-with(@href, 'Build')]")

#5. xpath with last() => xpath
#page.locator("//div[@class=""]")//li[last()]")

#6. xpath with position() => xpath
#page.locator("//div[@class=""]")//li[position()=3]")
