from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

def scrape_gazprombank_reviews():
    opts = Options()
    opts.headless = False
    opts.add_argument("--window-size=1200,800")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=opts)

    driver.get("https://www.banki.ru/services/responses/bank/gazprombank/")
    time.sleep(5)
    review_blocks = driver.find_elements(By.XPATH, "//div[@data-test='responses__response']")

    reviews = []

    for r in review_blocks:
        try:
            text = r.find_element(By.XPATH, ".//div[contains(@class,'StyledItemText')]//a").text
        except:
            text = ""

        try:
            date = r.find_element(By.XPATH, ".//span[contains(@class,'StyledItemSmallText')]").text
        except:
            date = ""

        try:
            rating = r.find_element(By.XPATH, ".//div[contains(@class,'Grade__sc')]").text
        except:
            rating = ""

        reviews.append({
            "text": text,
            "date": date,
            "rating": rating
        })

    driver.quit()

    df = pd.DataFrame(reviews)
    df.to_csv("gazprombank_reviews.csv", index=False, encoding="utf-8-sig")
    print(f"Собрано {len(reviews)} отзывов. Сохранено в 'gazprombank_reviews.csv'.")

if __name__ == "__main__":
    scrape_gazprombank_reviews()
