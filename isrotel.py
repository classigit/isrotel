from datetime import date, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

drivers_path = 'C:\chromedriver_win32\chromedriver.exe'
xpath = '//*[@id="main-results"]/div[2]/div/div[4]/div/section/div[2]/div[2]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/span[1]'

options = Options()
options.add_argument('start-maximized')

driver = webdriver.Chrome(drivers_path, options=options)
vacation_days = 2
days_to_check = 1
stub_date = date(2022, 1, 16) - timedelta(days=1)  # -day because it'll be increased in the loop
for i in range(days_to_check):
    stub_date = stub_date + timedelta(days=1)
    start = stub_date
    end = stub_date + timedelta(days=vacation_days)

    start = start.strftime("%d-%m-%Y")
    end = end.strftime("%d-%m-%Y")
    url = f"https://www.isrotel.co.il/searchresult/%D7%97%D7%93%D7%A8-%D7%91%D7%9E%D7%9C%D7%95%D7%9F/?SearchQuery=CF/{start}/{end}/2-0-0/-1"
    driver.get(url)
    try:
        WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, xpath)))
    except:
        print('timeout')
        continue
    price = driver.find_element(By.XPATH, xpath).text
    print(f"{price=} {start}-{end}")
driver.close()
