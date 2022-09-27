#!/usr/bin/env python
# coding: utf-8
# In[19]:
#Import the Selenium Webdriver, BY element and Time
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
#Setup the chrome driver executable path and destination folder path for scraped data from website
options = webdriver.ChromeOptions()

prefs = {"download.default_directory" : "C:\\Users\\FJ795RQ\\Downloads"};

options.add_experimental_option("prefs",prefs);

driver = webdriver.Chrome(executable_path='C:\\Users\\FJ795RQ\\Downloads\\chromedriver_win32\\chromedriver.exe');

# Navigate the Education ministry website URL to selenium driver from where data needs to be scraped
driver.get('https://dashboard.udiseplus.gov.in/#/reportDashboard/sReport');
main_page = driver.current_window_handle
#print('Main page :', main_page)

#downloadcsv= driver.find_element(By.XPATH, "//td[@class='sNo']/span[text()='1']//following-sibling::td[2]/img[@src='assets/images/edit-tools.svg']");
#Open report popup
reportpopup= driver.find_element(By.XPATH, "/html/body/app-root/app-report-dashboard/mat-sidenav-container/mat-sidenav-content/app-static-report/div/mat-card-content/div[2]/div[1]/div/div/div/div/div[2]/table/tr[1]/td[5]/img[2]")
print('reportpopup : ', reportpopup)

#print('reportpopup : ', reportpopup)
reportpopup.click()
print("Successfully reportpopup : ", driver.current_window_handle)

# Handling the report popup
for handle in driver.window_handles:
    print("handles : ", handle)
    print()
    if handle != main_page:
        report_page = handle
        break
#driver.switch_to.window(report_page)
time.sleep(5);
# Data Download from the report available on website of education ministry
report= driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/div[1]/div/div[1]/div/div[2]/ul/li[3]/img")
#print('report : ', report)
report.click()
print("Successfully report downloaded")

time.sleep(5);
driver.close();





