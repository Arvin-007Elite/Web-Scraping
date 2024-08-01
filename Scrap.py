


# library to use Web scraping functions 
from bs4 import BeautifulSoup
# library to handle HTTP requests
# Library to handle Excel files
import requests, openpyxl

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

   


except Exception as e:
    print(e)

    excel.save("Action.xlsx")