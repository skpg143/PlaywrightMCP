# configure allure report

#step1: Install allure pytest plugin
#pip install allure-pytest

#step2: Install allure commond-line tool(to view & generate reports)
#.zip file for window and .tgz for mac

#step3: Configure Allure in Pytest.ini
#[pytest]
#addopts= --headed
#          --browser=chromium
#          --alluredir=reports/allure-results

#step4: Attached screenshots on test failures (conftest.py)
#step5: create and run your test case
#step6: Generate & view the allure report

###################################################################
#Viewing the reports
#generate the report at runtime
# allure serve reports/allure-results

#Genrate the report permanent
# allure generate reports/allure-results

#Generate the report with time
# pytest .\folder\test_sample.py --html=myreport.html --self-contained-html --capture=true-sys or ="myreport-$(Get-Date-Format 'yyy-dd-HH-mm-ss').html"

