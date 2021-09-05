# Elvin Rivera
# 9/5/2021
#
# References: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from bs4 import BeautifulSoup

# import lxml

with open("website.html") as file:
    contents = file.read()

# helps beautiful soup understand the contents, depending on site, need lxml.parser
soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)   # <title>Angela's Personal Site</title>
# print(soup.title.name)      # title
# print(soup.title.string)       # Angela's Personal Site
#
# # print(soup.prettify())
#
# print(soup.a)   # returns first anchor tag

# # to get all of the tags a, p, h1, etc.
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# # to get text of tag.
# for tag in all_anchor_tags:
#     # print(tag.getText()) # The App Brewery; My Hobbies ; Contact Me
#     print(tag.get("href")) # returns the LINKS of those above <a href="website"

# heading = soup.find(name="h1", id="name")
# print(heading)      # <h1 id="name">Angela Yu</h1>

# section_heading = soup.find(name="h3", class_="heading")  # use class_
# # print(section_heading.get_text)

company_url = soup.select_one(selector="p a")  # give first matching item, a tag that sits in p tag
print(company_url)

# to get id= , you have to use #
name = soup.select(selector="#name")
print(name)  # <h1 id="name">Angela Yu</h1>

headings = soup.select(".heading")
print(headings)  # [<h3 class="heading">Books and Teaching</h3>, <h3 class="heading">Other Pages</h3>]
