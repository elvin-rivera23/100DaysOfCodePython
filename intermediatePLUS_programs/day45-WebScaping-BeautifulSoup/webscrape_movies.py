# Elvin Rivera
# 9/5/2021
#
# Description: create a .txt file with the top 100 movies, starting from 1, based on the empire website
# link: https://www.empireonline.com/movies/features/best-movies-2/

import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text        # raw html text

soup = BeautifulSoup(website_html, "html.parser")
# print(soup.prettify())

all_movies = soup.find_all(name="h3", class_="jsx-4245974604")
# print(all_movies)
movie_titles = [movie.getText() for movie in all_movies]
# start, stop, step (-1)
# for n in range(len(movie_titles) -1, -1, -1
#   print(movie_titles[n])
movies = (movie_titles[::-1])   # splicing the list will reverse the order 100->1 , 1->100


with open("movies.text", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")