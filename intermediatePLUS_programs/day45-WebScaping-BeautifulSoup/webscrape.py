# Elvin Rivera
# 9/5/21
#
# Desc: practice webscraping live website: https://news.ycombinator.com/

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)

# getting tags... find. then getText
# article_tag = soup.find(name="a", class_="storylink")

articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")  # get specific value of attribute
    article_links.append(link)

# same as for loop above
# for score in all of scores, we create list using each of score and call getText to get each of them
article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]   # can't call getText on list

# print(article_texts)
# print(article_links)
# print(article_upvote)
# print(int(article_upvote[0].split()[0]))    # get list 1st item, split by spaces (), return first item from split list, turn to int

# find highest voted article
largest_number = max(article_upvote)
largest_index = article_upvote.index(largest_number)
print(article_texts[largest_index], ": ", article_links[largest_index], )