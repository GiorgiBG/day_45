import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
found = response.text
soup = BeautifulSoup(found, "html.parser")
movie_title = soup.find_all("h3", class_="title")
with open("movie_title.txt", "a") as file:
    for title in movie_title:
        file.write(f"{title.get_text()}\n")