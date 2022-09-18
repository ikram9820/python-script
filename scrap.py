import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

path = 'https://www.alamy.com/stock-photo/dump-truck-construction.html?imgt=1&sortBy=relevant'
driver.get(path)


for i in range(5):
    time.sleep(2)
    print(f"page {i} data")
    imgs = driver.find_elements(By.XPATH,"//div[@class='absolute group']/img")

    print('page loaded')

    for img in imgs:
        src = img.get_attribute('src')
        print(src)
        
    next = driver.find_element(By.LINK_TEXT,'Next page')
    next.click()

time.sleep(5)
driver.quit()