import requests
from bs4 import BeautifulSoup
url = "https://weather.com/weather/tenday/l/a5281dc95bc87ca246255ad20368985c8541d27810254ec2fe79c518b648c507"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
# print(soup.find_all('a'))
week = soup.find_all("span",class_="DailyContent--temp--3d4dn")
# print(week)

# for items_in_list in week:
#     print(items_in_list.text)

print(f"Today's temp is {week[0].text}. The overnight temp will be {week[1].text}. ")
print(f"Tomorrows's temp will be {week[2].text} with an overnight temp will be {week[3].text}. ")

