# library to use Web scraping functions 
from bs4 import BeautifulSoup
# library to handle HTTP requests
# Library to handle Excel files
import requests, openpyxl
import re

# we want to store these print datas in excel , so 
# using excel function , defualtly 1 sheet will be active , to use that use active function

excel = openpyxl.Workbook()
sheet = excel.active
# creating a  title for the sheet

sheet.title = "Movie-list"
# insert columns into sheet
sheet.append(["Rank" , "Movie-Name", "Year of release", "IMDB - Rating"])


# we will try and catch  block to recieve requests  , if not using try catch , if the url is wrong , error will come to avoid and find the exception , this is used !
# if the website has problem  , it will tell the errors , if not using ,program will crash ,  it will show erros at our side !

try:
 # stores all html content of the url website.
 response=requests.get("https://www.imdb.com/chart/top/")
#  response = requests.get("https://www.allelitewrestling.com/")
 soup = BeautifulSoup(response.text,'html.parser')
 # to print whole site !
#  print(soup)

# to specifically print tag and its info
# we r getting the tag name , class name , in that which tag? where the specific text is inside !
 movies = soup.find('tbody',class_ = 'lister-list').find_all('tr')
# print all tr values in a loop
 for movie in movies:
    print(movie) # prints 1st value 
    # to pint specific value of that area details
    # i want to display rank alone , but whole data is printing , 
    # so to remove empty spaces , strip is used , and to split the dot 
    # after rank  - 1. , to remove dot and display only 1 which is 0 index is used !
    rank = movie.find('td',class_ = "titleColumn".get_text(strip=True).split('.',[0]))
    # the value is in td tag , titleColumn classname , and in a tag's text
    movie_name = movie.find('td',class_ = "titleColumn").a.text
    rate = movie.find('td',class_ = "ratingColumn").strong.text
    # here the year prints text with brackets , so to remove that replace is used !
    year = movie.find('td',class_ = "titleColumn").span.text.replace('('," ")
    year = year.replace(')', " ")
    # if we want to print only digits and replace others
    # year = re.sub("\D"," " , year)

    # print(rank,movie_name,year,rate)
    # now all Datas will print 

# merging the printed details to sheets
    sheet.append([rank,movie_name,year,rate])
   


except Exception as e:
    print(e)

    excel.save("Movies.xlsx")

    # after doing , instead of excel , we can use DB
    # for using that remove all excel lines !!