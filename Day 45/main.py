from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article in articles: 
    article_texts.append(article.getText())
    article_links.append(article.get("href"))
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)
highest_upvote = article_upvotes.index(max(article_upvotes))
print(article_texts[highest_upvote])
print(article_links[highest_upvote])





# with open("C:/Users/subhr/OneDrive/Documents/Programs/Python/#100DaysOfCode/Day 45/website.html", encoding="utf8") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)
# print(soup.li)
# all_anchor_tags = soup.find_all(name='a')

# print(all_anchor_tags)

# for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))
    # pass

# heading = soup.find(name="h1", id="name")
# print(heading.string)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.string)

# company_url = soup.select_one(selector="p a")
# print(company_url.get("href"))

# name = soup.select_one(selector="#name")
# print(name.getText())

# heading = soup.select(selector=".heading")
# print(heading)

