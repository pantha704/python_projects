from bs4 import BeautifulSoup

# # import lxml
# import chardet

import requests


response = requests.get(url="https://news.ycombinator.com/news")
data = response.text
# print(data)

soup = BeautifulSoup(data, 'html.parser')
articles = soup.select(".titleline a")
article_texts = []
article_links = []
for article in articles:
    text = article.text
    article_texts.append(text)
    link = article.get("href")
    article_links.append(link)

article_scores = [int(score.text.split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_scores)
max_score = max(article_scores)
index = article_scores.index(max_score)
print(article_texts[index])
print(article_links[index])
print(article_scores[index])










# def read_file(file_name):
#     file = open(file_name, "rb")
#     contents = file.read()
#     encoding = chardet.detect(contents)["encoding"]
#     decoded_contents = contents.decode(encoding)
#     return decoded_contents
#
#
# contents = read_file("website.html")
# # with open("website.html") as file:
# #     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')  # for xml use 'lxml' instead of 'html.parser'
# # print(soup.title)
# # print(soup.title.name)  # to print the name of the tag 'title'
#
# all_tags = soup.find_all(name="a")
# for tags in all_tags:
#     print(tags.text)


