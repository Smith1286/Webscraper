# Webscraper
from bs4 import BeautifulSoup
import requests 


url = "https://weather.com/weather/tenday/l/Columbus+OH?canonicalCityId=2ffaa69fa967e48c4de4cbc55c096da95012f22610ecafe26bf12b5a603e5021"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
#print(soup.link)

for link in soup.find_all('a'):
