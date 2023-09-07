from bs4 import BeautifulSoup


with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)

# print(soup.prettify())

# print(soup.p)


all_anchor_tag = soup.findAll(name="a")
# print(all_anchor_tag)


for tag in all_anchor_tag:
    # print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)