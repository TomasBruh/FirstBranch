from bs4 import BeautifulSoup
import requests

URL = "https://www.apple.com"

response = requests.get("https://www.apple.com")
apple = response.text

soup = BeautifulSoup(apple, "html.parser")
menu = soup.select(selector=".ac-gn-list .ac-gn-link-text")
menu_links = soup.select(selector=".ac-gn-list li a")

for item in menu:
    print(item.getText())

for item in menu_links:
    if item.get("href").__contains__("https"):
        print(item.get("href"))
    else:
        print(URL + item.get("href"))
print(menu)
