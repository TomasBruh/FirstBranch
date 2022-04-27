from bs4 import BeautifulSoup

with open("index.html", encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content, "lxml")

heading = soup.find(name="h1").get_text()

name = soup.find(name="h2", id="name").getText()

surname = soup.find(name="h2", id="surname").getText()

all_a_tag = soup.findAll(name="a")
# for tag in all_a_tag:
#     print(tag.get("href"))

company_url = soup.select_one(selector="p a").get("href")

all_food = soup.select(selector="#list .item")
for food in all_food:
    print(food.getText())

print(all_food)
