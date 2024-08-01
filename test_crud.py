# Importing libraries
from bs4 import BeautifulSoup  # Library for web scraping
import requests  # Library for handling HTTP requests
import pandas as pd  # Library for data manipulation and analysis
import sqlite3  # Library for working with SQLite databases

# Initialize movie_list outside the try block to ensure it's always defined
movie_list = {"movie_rank": [], "movie_name": [], "movie_year": [], "movie_rate": []}

try:
    # Fetching data from the URL
    response = requests.get("https://www.imdb.com/chart/top/")
    soup = BeautifulSoup(response.text, 'html.parser')
    movies = soup.find('tbody', class_='lister-list').find_all('tr')
    
    # Extracting data from each movie element
    for movie in movies:
        # Extracting rank
        rank_text = movie.find('td', class_="titleColumn").get_text(strip=True).split('.')[0]
        rank = int(rank_text)
        
        # Extracting movie name
        movie_name = movie.find('td', class_="titleColumn").a.text
        
        # Extracting movie rating
        rate = movie.find('td', class_="ratingColumn").strong.text
        
        # Extracting movie year
        year = movie.find('td', class_="titleColumn").span.text.replace('(', "").replace(')', "")
        
        # Appending extracted data to movie_list
        movie_list["movie_rank"].append(rank)
        movie_list["movie_name"].append(movie_name)
        movie_list["movie_year"].append(year)
        movie_list["movie_rate"].append(rate)
        
except Exception as e:
    print(e)

# Creating DataFrame from movie_list
df = pd.DataFrame(data=movie_list)
print(df.head())

# Connection to SQLite3
connection = sqlite3.connect("test.db")
cursor = connection.cursor()

# Creating movies table in the database if it doesn't exist
qry = "CREATE TABLE IF NOT EXISTS movies(movie_rank INTEGER, movie_name TEXT, movie_year TEXT, movie_rate TEXT)"
cursor.execute(qry)

# Inserting values into the movies table
for i in range(len(df)):
    cursor.execute("INSERT INTO movies VALUES (?,?,?,?)", df.iloc[i])

# Committing the transaction and closing the connection
connection.commit()
connection.close()


#  test db will be stored in folder 
# if u put sql cmnd , it will display all datas
