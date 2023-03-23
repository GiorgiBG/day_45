from bs4 import BeautifulSoup
import requests

# with open("website.html") as URL:
#     contents = URL.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# #print(soup.title.string)
# paragraph = soup.find_all("ul")
# for text in paragraph:
#     print(text.getText())


found = requests.get("https://news.ycombinator.com/")

URL = found.text
soup = BeautifulSoup( URL, "html.parser")
title_lists = soup.find("td", class_="title")
# for answer in title_lists:
#     link = answer.a
#     print(link)

found_article = soup.find_all("span", class_="titleline")
article_text = [article.get_text() for article in found_article]
print(article_text)

article_link = [found_link.a['href'] for found_link in found_article]
print(article_link)

article_upvote = [int(score.get_text().split()[0]) for score in soup.find_all("span", class_="score")]
max_vot0e_article_index = article_upvote.index(max(article_upvote))
print(f" article name: {article_text[max_vot0e_article_index]} \n article link: {article_link[max_vot0e_article_index]} \n article code: {article_upvote[max_vot0e_article_index]}")
