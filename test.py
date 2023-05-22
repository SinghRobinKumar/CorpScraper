import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import json


dc = DesiredCapabilities.CHROME
dc["goog:loggingPrefs"] = {"browser": "ALL"}
s = Service("./chromedriver")
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(
    options=chrome_options, service=s, desired_capabilities=dc
)
driver.maximize_window()

URL = (
    "https://csr.gov.in/content/csr/global/master/home/ExploreCsrData/company-wise.html"
)
driver.get(URL)

companys = [
     {
     "S. No.": 1708,
     "CIN": "U40106DL2008PTC241157",
     "Name": "CLP WIND FARMS (INDIA) PRIVATE LIMITED",
     "CSR Spent \n(In Crores)": 0.167
    },
    {
     "S. No.": 1709,
     "CIN": "U15511RJ2005SGC020336",
     "Name": "RAJASTHAN STATE BEVERAGES CORPORATION LIMITED",
     "CSR Spent \n(In Crores)": 0.1666992
    },
    {
     "S. No.": 1710,
     "CIN": "U51101DL2009PTC195494",
     "Name": "UNIQUE LIFESTYLE PRIVATE LIMITED",
     "CSR Spent \n(In Crores)": 0.16644
    },
    {
     "S. No.": 1711,
     "CIN": "U65991TN1941PLC001437",
     "Name": "AMBADI ENTERPRISES LIMITED",
     "CSR Spent \n(In Crores)": 0.1663
    },
    {
     "S. No.": 1712,
     "CIN": "U18101MH1964PTC013015",
     "Name": "USHA GARMENTS MANUFACTURING COMPANY PRIVATE LIMITED",
     "CSR Spent \n(In Crores)": 0.1662
    },
]


for i in range(len(companys)):
    start = time.time()
    try:
        company_name = companys[i].get("Name")
        cin = companys[i].get("CIN")
        sno=companys[i].get("S. No.")
        driver.get(URL)

        # company_name = "S V CREDITLINE PRIVATE LIMITED"
        # cin = "U71290DL1996PTC081376"

        CIDXpath = "//tr[@data-cin='{0}']".format(cin)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "SearchBox"))
        )
        driver.find_element(By.ID, "SearchBox").send_keys(company_name)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CIDXpath))
        )
        driver.find_element(By.XPATH, CIDXpath).click()
        print("Element Found !!!!!")

        driver.execute_script("console.log(result)")

        # obtain with get_log()
        for e in driver.get_log("browser"):
          
            splitMessage = e.get("message")
            captchaMessage = splitMessage.split(" ")
            captchaValue = captchaMessage[2]
            print(captchaValue)

        # FOR GETTING THE ADDED VALUES IN THE CAPTCHA
        if captchaMessage[0] == "console-api":
            driver.find_element(By.ID, "customCaptchaInput").send_keys(captchaValue)
            driver.implicitly_wait(3)
            driver.find_element(By.ID, "check").click()
            driver.implicitly_wait(3)
            driver.find_element(By.XPATH, "//span[text()='Download Report']").click()

            print(f"<=======S.NO {sno} Download Started========>")


            WebDriverWait(driver,250).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='downloadButtonWrapper']/div/span")))
            # time.sleep(250)
            print(f"<=======S.NO {sno} Download Completed========>")
            end = time.time()
            print(f"{end - start} Secs")
            driver.refresh();

    except Exception as e:
        # print("Exception:  ", e)
        print(f"<=======S.NO {sno} Download Failed========>")
