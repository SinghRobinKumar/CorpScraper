# CorpScrapper

CorpScrapper is a Python web scraping tool designed to effortlessly download a CSV file of comprehensive company details from [csr.gov.in](https://csr.gov.in/content/csr/global/master/home/ExploreCsrData/company-wise.html).

## Installation

### Prerequisites

* Before you begin, ensure that you have Python 3 installed on your computer. If not, you can download and install it from the official [Python website](https://www.python.org/downloads/).


### ChromeDriver Setup:

Download the ChromeDriver to run the script with Chrome. Ensure that you download the version compatible with your Chrome browser. You can find the latest ChromeDriver releases [here](https://chromedriver.chromium.org/downloads).

Extract the downloaded ChromeDriver archive.
Replace the existing version in the project folder with the one you just downloaded.

### Selenium Installation:

Install Selenium in the project by running the following command in your terminal or command prompt:
```bash
pip install selenium
```

### Note:

Make sure to keep the ChromeDriver version in sync with your Chrome browser for optimal compatibility.
If you encounter any issues, refer to the official [Selenium documentation](https://www.selenium.dev/selenium/docs/api/py/index.html) for troubleshooting and additional information.


## Usage

Open the `companies.json` file in the root directory and add the names of the companies for which you need to download data. Ensure it follows `JSON` file format:

Execute the script using the following command:
```python
python3 script.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
