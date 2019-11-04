import requests 
from bs4 import BeautifulSoup 
import csv 
  
URL = "https://www.google.com/search?q=webscrapping"
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'lxml') 

print(soup.find(""))