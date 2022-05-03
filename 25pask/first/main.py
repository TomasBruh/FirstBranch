import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

DRIVER_PATH = r"C:\Users\Tomas\Downloads\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(executable_path=DRIVER_PATH)

# URL = "https://www.python.org"
# driver.get(URL)
# query_field = driver.find_element(By.NAME, "q")
# query_field.send_keys("for")
# query_field.send_keys(Keys.ENTER)
#
# titles = driver.find_elements(By.TAG_NAME, "h3")
#
# for title in titles:
#     print(title.text)
# menu = driver.find_element(By.XPATH, "/html/body/div/div[3]/div/section/div[3]/div[2]/div/ul")
# events = menu.find_elements(By.CSS_SELECTOR, "li a")
# for event in events:
#     print(event.text)

URL = "https://nkkm.lt"
driver.maximize_window()
driver.get(URL)

driver.find_element(By.ID, "menu-item-401").click()

driver.find_element(By.XPATH, "html/body/div[1]/div/div/article/div/div/div/div/div[2]/div/div/div[3]/ul/li[2]/a")\
    .click()
time.sleep(1)
query_field = driver.find_element(By.XPATH, '//*[@id="wpcf7-f1233-p392-o2"]/form/p[1]/label/span[2]/input')
query_field.send_keys("Tomas")

query_field = driver.find_element(By.XPATH, '//*[@id="wpcf7-f1233-p392-o2"]/form/p[2]/label/span[2]/input')
query_field.send_keys("Max")

query_field = driver.find_element(By.XPATH, '//*[@id="wpcf7-f1233-p392-o2"]/form/p[3]/label/span[2]/input')
query_field.send_keys("16")

query_field = driver.find_element(By.XPATH, '//*[@id="wpcf7-f1233-p392-o2"]/form/p[4]/label/span[2]/input')
query_field.send_keys("866005011")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
query_field = driver.find_element(By.XPATH, '//*[@id="wpcf7-f1233-p392-o2"]/form/p[5]/label/span[2]/input')
query_field.send_keys("tomas.nkkm@gmail.com")

driver.find_element(By.XPATH, '//*[@id="wpcf7-f1233-p392-o2"]/form/div[2]/div/span/span/span[2]/input').click()
driver.find_element(By.XPATH, '//*[@id="wpcf7-f1233-p392-o2"]/form/p[6]/span/span/span/input').click()
driver.find_element(By.XPATH, '//*[@id="wpcf7-f1233-p392-o2"]/form/div[2]/div/span/span/span[1]/input').click()


# driver.quit()
