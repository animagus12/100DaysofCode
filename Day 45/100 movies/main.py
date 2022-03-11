from unicodedata import name
from urllib import response
from matplotlib.pyplot import cla
import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = (requests.get(URL)).text

soup = BeautifulSoup(response, "html.parser")
movies = soup.find_all(name="h3", class_="title")
for movie in movies[::-1]:
    # print(movie.getText())
    with open("Python/#100DaysOfCode/Day 45/100 movies/movies.txt", "a") as file:
        file.write(f"{movie.string}\n")
