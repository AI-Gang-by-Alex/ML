from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

def scrape_reviews():
    opts = Options()
    opts.headless = False
    opts.add_argument("--window-size=1200,800")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=opts)

    driver.get("https://www.sravni.ru/bank/gazprombank/otzyvy/")
    time.sleep(5)

    read_more_buttons = driver.find_elements(By.XPATH, "//a[contains(text(),'Читать')]")
    for btn in read_more_buttons:
        try:
            driver.execute_script("arguments[0].click();", btn)
            time.sleep(1)
        except Exception as e:
            print("Не удалось нажать:", e)

    reviews = []
    review_blocks = driver.find_elements(By.XPATH, "//div[contains(@class,'review-card_text__')]")

    for r in review_blocks:
        try:
            text = r.text.strip()
            reviews.append(text)
        except:
            continue

    print(f"Собрано {len(reviews)} отзывов")
    print(reviews[0])
    driver.quit()


if __name__ == "__main__":
    scrape_reviews()
