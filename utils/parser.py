from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

def open_site():
    opts = Options()
    opts.headless = False
    opts.add_argument("--window-size=1200,800")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=opts)
    driver.get("https://www.banki.ru/services/responses/bank/gazprombank/")

    time.sleep(5)
    print("Title:", driver.title)
    print("URL:", driver.current_url)
    driver.quit()

if __name__ == "__main__":
    open_site()
