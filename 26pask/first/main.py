from selenium import webdriver
from selenium.webdriver.common.by import By
from item_class import Item

DRIVER_PATH = r"C:\Users\Tomas\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.maximize_window()

URLS = ["https://www.skytech.lt/", "https://gameroom.lt/lt/", "https://www.inida.lt/"]

searchable = "KM"
info_dic = dict

driver.get(URLS[0])
query = driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[5]/table/tbody/tr/td[2]/div/form/div[1]/input[1]")
query.send_keys(searchable)
driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[5]/table/tbody/tr/td[2]/div/form/div[1]/input[2]').click()
raw_data = driver.find_elements(By.CSS_SELECTOR, "div.contentbox-center-wrap tbody tr.productListing")
skyTech = []
for data_item in raw_data:
    name = data_item.find_element(By.CSS_SELECTOR, "a")
    price = data_item.find_element(By.CSS_SELECTOR, "td strong")
    skyTech.append(Item(name, price))

driver.get(URLS[1])
query = driver.find_element(By.XPATH, '/html/body/div[2]/header/section/div/div/div[3]/div/form/div/input')
query.send_keys(searchable)
driver.find_element(By.XPATH, '/html/body/div[2]/header/section/div/div/div[3]/div/form/div/button/i').click()
raw_data = driver.find_elements(By.CSS_SELECTOR, "ul.product_list li")
print(len(raw_data))
# driver.quit()
