{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b7dc3738",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\FJ795RQ\\AppData\\Local\\Temp/ipykernel_2620/1571026234.py:16: DeprecationWarning: executable_path has been deprecated, please pass in a Service object\n",
      "  driver = webdriver.Chrome(executable_path='C:\\\\Users\\\\FJ795RQ\\\\Downloads\\\\chromedriver_win32\\\\chromedriver.exe');\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "reportpopup :  <selenium.webdriver.remote.webelement.WebElement (session=\"90d31b19e9cef8d445087cf0b5599167\", element=\"ba36cb7b-ee6e-4689-b75f-4fa9bf8f313d\")>\n",
      "Successfully reportpopup :  CDwindow-DA77AED3160291E72E9EC1506CED31AB\n",
      "yeardropdownsel :  <selenium.webdriver.remote.webelement.WebElement (session=\"90d31b19e9cef8d445087cf0b5599167\", element=\"46fa1082-ad3d-4a5b-8c2a-e07d611f22a7\")>\n",
      "Successfully yeardropdownsel :  CDwindow-DA77AED3160291E72E9EC1506CED31AB\n",
      "statedropdownsel :  <selenium.webdriver.remote.webelement.WebElement (session=\"90d31b19e9cef8d445087cf0b5599167\", element=\"21a739fd-4c28-4c42-8747-35ffd8b8b4c1\")>\n",
      "Successfully statedropdownsel :  CDwindow-DA77AED3160291E72E9EC1506CED31AB\n",
      "handles :  CDwindow-DA77AED3160291E72E9EC1506CED31AB\n",
      "\n",
      "Successfully report downloaded\n"
     ]
    }
   ],
   "source": [
    "#!/usr/bin/env python\n",
    "# coding: utf-8\n",
    "# In[19]:\n",
    "#Import the Selenium Webdriver, BY element and Time\n",
    "from selenium import webdriver\n",
    "from selenium.webdriver.common.by import By\n",
    "\n",
    "import time\n",
    "#Setup the chrome driver executable path and destination folder path for scraped data from website\n",
    "options = webdriver.ChromeOptions()\n",
    "\n",
    "prefs = {\"download.default_directory\" : \"C:\\\\Users\\\\FJ795RQ\\\\Downloads\"};\n",
    "\n",
    "options.add_experimental_option(\"prefs\",prefs);\n",
    "\n",
    "driver = webdriver.Chrome(executable_path='C:\\\\Users\\\\FJ795RQ\\\\Downloads\\\\chromedriver_win32\\\\chromedriver.exe');\n",
    "\n",
    "# Navigate the Education ministry website URL to selenium driver from where data needs to be scraped\n",
    "driver.get('https://dashboard.udiseplus.gov.in/#/reportDashboard/sReport');\n",
    "main_page = driver.current_window_handle\n",
    "#print('Main page :', main_page)\n",
    "\n",
    "#downloadcsv= driver.find_element(By.XPATH, \"//td[@class='sNo']/span[text()='1']//following-sibling::td[2]/img[@src='assets/images/edit-tools.svg']\");\n",
    "#Open report popup\n",
    "reportpopup= driver.find_element(By.XPATH, \"/html/body/app-root/app-report-dashboard/mat-sidenav-container/mat-sidenav-content/app-static-report/div/mat-card-content/div[2]/div[1]/div/div/div/div/div[2]/table/tr[1]/td[5]/img[2]\")\n",
    "print('reportpopup : ', reportpopup)\n",
    "\n",
    "#print('reportpopup : ', reportpopup)\n",
    "reportpopup.click()\n",
    "print(\"Successfully reportpopup : \", driver.current_window_handle)\n",
    "time.sleep(5);\n",
    "yeardropdownsel= driver.find_element(By.XPATH, \"/html/body/ngb-modal-window/div/div/div[2]/div[1]/div/div/div[1]/div/div/select/option[1]\")\n",
    "print('yeardropdownsel : ', yeardropdownsel)\n",
    "yeardropdownsel.click()\n",
    "print(\"Successfully yeardropdownsel : \", driver.current_window_handle)\n",
    "time.sleep(5);\n",
    "statedropdownsel= driver.find_element(By.XPATH, \"/html/body/ngb-modal-window/div/div/div[2]/div[1]/div/div/div[2]/div/div/select/option[4]\")\n",
    "print('statedropdownsel : ', statedropdownsel)\n",
    "statedropdownsel.click()\n",
    "print(\"Successfully statedropdownsel : \", driver.current_window_handle)\n",
    "time.sleep(5);\n",
    "# Handling the report popup\n",
    "for handle in driver.window_handles:\n",
    "    print(\"handles : \", handle)\n",
    "    print()\n",
    "    if handle != main_page:\n",
    "        report_page = handle\n",
    "        break\n",
    "#driver.switch_to.window(report_page)\n",
    "time.sleep(5);\n",
    "# Data Download from the report available on website of education ministry\n",
    "report= driver.find_element(By.XPATH, \"/html/body/ngb-modal-window/div/div/div[1]/div/div[1]/div/div[2]/ul/li[3]/img\")\n",
    "#print('report : ', report)\n",
    "report.click()\n",
    "print(\"Successfully report downloaded\")\n",
    "\n",
    "time.sleep(5);\n",
    "driver.close();\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "42127119",
   "metadata": {},
   "outputs": [
    {
     "ename": "InvalidSessionIdException",
     "evalue": "Message: invalid session id\nStacktrace:\nBacktrace:\n\tOrdinal0 [0x0111DF13+2219795]\n\tOrdinal0 [0x010B2841+1779777]\n\tOrdinal0 [0x00FC4100+803072]\n\tOrdinal0 [0x00FE7A20+948768]\n\tOrdinal0 [0x0100E6F0+1107696]\n\tOrdinal0 [0x0100C536+1099062]\n\tOrdinal0 [0x0100C0A8+1097896]\n\tOrdinal0 [0x00FA51F7+676343]\n\tOrdinal0 [0x00FA5863+677987]\n\tOrdinal0 [0x00FA5C9A+679066]\n\tGetHandleVerifier [0x01412CB2+3040210]\n\tGetHandleVerifier [0x01402BB4+2974420]\n\tGetHandleVerifier [0x011B6A0A+565546]\n\tGetHandleVerifier [0x011B5680+560544]\n\tOrdinal0 [0x010B9A5C+1808988]\n\tOrdinal0 [0x00FA5071+675953]\n\tOrdinal0 [0x00FA4A21+674337]\n\tGetHandleVerifier [0x0143886C+3194764]\n\tBaseThreadInitThunk [0x768BFA29+25]\n\tRtlGetAppContainerNamedObjectPath [0x77497B5E+286]\n\tRtlGetAppContainerNamedObjectPath [0x77497B2E+238]\n",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mInvalidSessionIdException\u001b[0m                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_2620/1254957224.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mprint\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mdriver\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_element\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mBy\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mXPATH\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"/html/body/ngb-modal-window/div/div/div[2]/div[1]/div/div/div[1]/div/div/select/option[1]\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_attribute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"value\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\selenium\\webdriver\\remote\\webdriver.py\u001b[0m in \u001b[0;36mfind_element\u001b[1;34m(self, by, value)\u001b[0m\n\u001b[0;32m    853\u001b[0m             \u001b[0mvalue\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m'[name=\"%s\"]'\u001b[0m \u001b[1;33m%\u001b[0m \u001b[0mvalue\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    854\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 855\u001b[1;33m         return self.execute(Command.FIND_ELEMENT, {\n\u001b[0m\u001b[0;32m    856\u001b[0m             \u001b[1;34m'using'\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mby\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    857\u001b[0m             'value': value})['value']\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\selenium\\webdriver\\remote\\webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[1;34m(self, driver_command, params)\u001b[0m\n\u001b[0;32m    426\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    427\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 428\u001b[1;33m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    429\u001b[0m             response['value'] = self._unwrap_value(\n\u001b[0;32m    430\u001b[0m                 response.get('value', None))\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\selenium\\webdriver\\remote\\errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[1;34m(self, response)\u001b[0m\n\u001b[0;32m    241\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'alert'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'text'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    242\u001b[0m             \u001b[1;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[1;33m)\u001b[0m  \u001b[1;31m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 243\u001b[1;33m         \u001b[1;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mInvalidSessionIdException\u001b[0m: Message: invalid session id\nStacktrace:\nBacktrace:\n\tOrdinal0 [0x0111DF13+2219795]\n\tOrdinal0 [0x010B2841+1779777]\n\tOrdinal0 [0x00FC4100+803072]\n\tOrdinal0 [0x00FE7A20+948768]\n\tOrdinal0 [0x0100E6F0+1107696]\n\tOrdinal0 [0x0100C536+1099062]\n\tOrdinal0 [0x0100C0A8+1097896]\n\tOrdinal0 [0x00FA51F7+676343]\n\tOrdinal0 [0x00FA5863+677987]\n\tOrdinal0 [0x00FA5C9A+679066]\n\tGetHandleVerifier [0x01412CB2+3040210]\n\tGetHandleVerifier [0x01402BB4+2974420]\n\tGetHandleVerifier [0x011B6A0A+565546]\n\tGetHandleVerifier [0x011B5680+560544]\n\tOrdinal0 [0x010B9A5C+1808988]\n\tOrdinal0 [0x00FA5071+675953]\n\tOrdinal0 [0x00FA4A21+674337]\n\tGetHandleVerifier [0x0143886C+3194764]\n\tBaseThreadInitThunk [0x768BFA29+25]\n\tRtlGetAppContainerNamedObjectPath [0x77497B5E+286]\n\tRtlGetAppContainerNamedObjectPath [0x77497B2E+238]\n"
     ]
    }
   ],
   "source": [
    "print (driver.find_element(By.XPATH, \"/html/body/ngb-modal-window/div/div/div[2]/div[1]/div/div/div[1]/div/div/select/option[1]\").get_attribute(\"value\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5f12535f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "59b9b8e3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
