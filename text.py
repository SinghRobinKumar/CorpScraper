import time
from multiprocessing import Pool
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

companys = [
    {
        "CIN": "U71290DL1996PTC081376",
        "Name": "S V CREDITLINE PRIVATE LIMITED",
    },
    {
        "CIN": "U71290DL1996PTC081376",
        "Name": "S V CREDITLINE PRIVATE LIMITED",
    },
]


def check_ip(companys):
    # set browser log
    dc = DesiredCapabilities.CHROME
    dc["goog:loggingPrefs"] = {"browser": "ALL"}
    s = Service("./chromedriver")
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(
        chrome_options=chrome_options, service=s, desired_capabilities=dc
    )
    driver.get(
        "https://csr.gov.in/content/csr/global/master/home/ExploreCsrData/company-wise.html"
    )

    try:
        cin = companys.get("CIN")
        company_name = companys.get("Name")
        CIDXpath = "//tr[@data-cin='{0}']".format(cin)

        driver.find_element(By.ID, "SearchBox").send_keys(company_name)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CIDXpath))
        )
        driver.find_element(By.XPATH, CIDXpath).click()

        print("Element Found !!!!!")

        driver.execute_script("console.log(result)")
        # obtain with get_log()
        for e in driver.get_log("browser"):
            # print(e)
            # print(e.get("message"))
            splitMessage = e.get("message")
            captchaMessage = splitMessage.split(" ")
            captchaValue = captchaMessage[2]
            print(captchaValue)

            # FOR GETTING THE ADDED VALUES IN THE CAPTCHA
            if captchaMessage[0] == "console-api":
                print("It is Int")
                driver.find_element(By.ID, "customCaptchaInput").send_keys(captchaValue)
                driver.implicitly_wait(3)
                driver.find_element(By.ID, "check").click()
                driver.find_element(
                    By.XPATH, "//span[text()='Download Report']"
                ).click()

                # TIME BEFORE THE CHOME CLOSES IN SECONDS
                time.sleep(600)
                driver.quit()

    except Exception as e:

        print("Exception:  ", e)


with Pool() as pool:
    pool.map(check_ip, companys)
