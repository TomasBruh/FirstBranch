from bs4 import BeautifulSoup
import requests

URL = "https://autogidas.lt/"

response = requests.get(URL)
autogidas = response.text

soup = BeautifulSoup(autogidas, "html.parser")
menu = soup.select(selector=".body .footer .other-projects .other-project .other-project-text .other-project-title jsl10n")

for item in menu:
    print(item.getText())

