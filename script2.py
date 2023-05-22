import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import json


# Start Chrome Driver
# chromedriver = '/root/Dev/chromedriver'

# set browser log
dc = DesiredCapabilities.CHROME
dc["goog:loggingPrefs"] = {"browser": "ALL"}
s = Service("./chromedriver")
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(
    chrome_options=chrome_options, service=s, desired_capabilities=dc
)
driver.maximize_window()

URL = (
    "https://csr.gov.in/content/csr/global/master/home/ExploreCsrData/company-wise.html"
)
driver.get(URL)


with open("companies.json") as companies:
   companys= json.load(companies)

for i in range(len(companys)):
    try:
        company_name = companys[i].get("Name")
        cin = companys[i].get("CIN")
        # print(f"Name: {company_name} , CIN: {cin}")s
        sno=companys[i].get("S. No.")
        driver.get(URL)

        CIDXpath = "//tr[@data-cin='{0}']".format(cin)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "SearchBox"))
        )
        driver.find_element(By.ID, "SearchBox").send_keys(company_name)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CIDXpath))
        )
        driver.implicitly_wait(10)

        driver.find_element(By.XPATH, CIDXpath).click()
        # print("Element Found !!!!!")

        driver.execute_script("console.log(result)")

        # obtain with get_log()
        for e in driver.get_log("browser"):
          
            splitMessage = e.get("message")
            captchaMessage = splitMessage.split(" ")
            captchaValue = captchaMessage[2]
            # print(captchaValue)

        # FOR GETTING THE ADDED VALUES IN THE CAPTCHA
        if captchaMessage[0] == "console-api":
            driver.find_element(By.ID, "customCaptchaInput").send_keys(captchaValue)
            driver.implicitly_wait(5)
            driver.find_element(By.ID, "check").click()
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, "//span[text()='Download Report']").click()

            print(f"<=======S.NO: {sno} , Name: {company_name} , CIN: {cin} Download Started========>")
            time.sleep(180)
            print(f"<=======S.NO: {sno} , Name: {company_name} , CIN: {cin} Download Completed========>")
            print("\n")
            driver.refresh();

    except Exception as e:
        # print("Exception:  ", e)
        print(f"<======S.NO: {sno} , Name: {company_name} , CIN: {cin} Download Failed========>")
        print("\n")

