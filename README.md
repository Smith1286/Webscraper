# Webscraper
from bs4 import BeautifulSoup
import requests 


url = "https://weather.com/weather/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
#print(soup.link)

for link in soup.find_all('a'):
