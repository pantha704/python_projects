import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features"
                            "/best-movies-2/")
data = response.text

soup = BeautifulSoup(data, 'html.parser')

movies = soup.find_all(name="h3", class_="title")

list = [movie.text for movie in movies][::-1]
print(list)


with open("movies.txt", 'w', encoding="utf-8") as file:
    for movie in list:
        file.write(movie)
        file.write("\n\n")