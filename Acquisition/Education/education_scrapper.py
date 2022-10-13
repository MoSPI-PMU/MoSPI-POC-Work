#!/usr/bin/env python
# coding: utf-8
# In[19]:
#Import the Selenium Webdriver, BY element and Time
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

#Setup the chrome driver executable path and destination folder path for scraped data from website
options = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "C:\\Users\\FJ795RQ\POC\\Downloads"};
options.add_experimental_option("prefs",prefs);
driver = webdriver.Chrome(executable_path='C:\\Users\\FJ795RQ\POC\\chromedriver_win32\\chromedriver.exe', chrome_options=options);

    
def education_scrapper(year, state):
    
    #Navigate the Education ministry website URL to selenium driver from where data needs to be scraped
    driver.get('https://dashboard.udiseplus.gov.in/#/reportDashboard/sReport');
    main_page = driver.current_window_handle

    #Open report popup
    reportpopup= driver.find_element(By.XPATH, "/html/body/app-root/app-report-dashboard/mat-sidenav-container/mat-sidenav-content/app-static-report/div/mat-card-content/div[2]/div[1]/div/div/div/div/div[2]/table/tr[1]/td[5]/img[2]")
    reportpopup.click()
    time.sleep(5);

    # Handling the report popup
    for handle in driver.window_handles:
        #print("handles : ", handle)
        #print()
        if handle != main_page:
            report_page = handle
            break
    #driver.switch_to.window(report_page)
    time.sleep(1);

    # Specific year and state download 
    
    yr_childElements= driver.find_elements(By.XPATH, "/html/body/ngb-modal-window/div/div/div[2]/div[1]/div/div/div[1]/div/div/select/*")
    print("Number of years : ", len(yr_childElements)+1)
    
    state_childElements= driver.find_elements(By.XPATH, "/html/body/ngb-modal-window/div/div/div[2]/div[1]/div/div/div[2]/div/div/select/*")
    print("Number of states : ", len(state_childElements)+1)
    
    for i_year in range(1, len(yr_childElements)+1):
        
        year_epath = "/html/body/ngb-modal-window/div/div/div[2]/div[1]/div/div/div[1]/div/div/select/option[{0}]".format(i_year)
        yeardropdown = driver.find_element(By.XPATH, year_epath)
        if yeardropdown.text == year :
            print("Year found : ", yeardropdown.text)
            yeardropdown.click()
            time.sleep(1);
            break
    
    for j_state in range(1, len(state_childElements)+1):

        state_epath = "//html/body/ngb-modal-window/div/div/div[2]/div[1]/div/div/div[2]/div/div/select/option[{0}]".format(j_state)
        statedropdown = driver.find_element(By.XPATH, state_epath)
        #print(statedropdown.text)
        if statedropdown.text == state :
            print("State found : ", statedropdown.text)
            statedropdown.click()
            time.sleep(1)
            break
        
    # Click on image to download report
    report= driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/div[1]/div/div[1]/div/div[2]/ul/li[3]/img")
    report.click()
    print("Successful report downloaded for Year {0} and State {1}".format(yeardropdown.text, statedropdown.text))
    
    time.sleep(5);
    driver.close();
    
    '''
    # All data download
    
    yr_childElements= driver.find_elements(By.XPATH, "/html/body/ngb-modal-window/div/div/div[2]/div[1]/div/div/div[1]/div/div/select/*")
    print("Number of years : ", len(yr_childElements)+1)
    
    state_childElements= driver.find_elements(By.XPATH, "/html/body/ngb-modal-window/div/div/div[2]/div[1]/div/div/div[2]/div/div/select/*")
    print("Number of states : ", len(state_childElements)+1)
    
    for i_year in range(1, len(yr_childElements)+1):
        
        year_epath = "/html/body/ngb-modal-window/div/div/div[2]/div[1]/div/div/div[1]/div/div/select/option[{0}]".format(i_year)
        yeardropdown = driver.find_element(By.XPATH, year_epath)
        print(yeardropdown.text)
        #yeardropdown.click()
        #time.sleep(5);

        for j_state in range(1, len(state_childElements)+1):

            state_epath = "//html/body/ngb-modal-window/div/div/div[2]/div[1]/div/div/div[2]/div/div/select/option[{0}]".format(j_state)
            statedropdown = driver.find_element(By.XPATH, state_epath)
            print(statedropdown.text)
            #statedropdown.click()
            #time.sleep(5);

            # Click on image to download report
            report= driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/div[1]/div/div[1]/div/div[2]/ul/li[3]/img")
            #report.click()
            #print("Successful report downloaded for Year {0} and State {1}".format(yeardropdown.text, statedropdown.text))
    '''
 
