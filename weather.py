import requests
from bs4 import BeautifulSoup
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=34.099695000000054&lon=-118.33539999999999#.XuijGEVKjIU")

soup = BeautifulSoup(page.content, "html.parser")
week = soup.find(id ='seven-day-forecast-body')
items =week.find_all(class_ ='tombstone-container')
# print(week)
print(items)

# print(items[0])


# printt(items[0].find(class_ = "period-name"))


print(items[0].find(class_ = "period-name")).get_text()


period_names = [item.find(class_ ="period-name").get_text() for item in items]
# print(period_names)

short_description = [item.find(class_ ="short-desc").get_text() for item in items]
# print(short_description)

temp = [item.find(class_ ="temp").get_text() for item in items]
# stringed_temp = str(temp)
# print(stringed_temp)



import pandas as pd



wethear_analysis = pd.DataFrame( {
	"period":period_names,
	"temperature":temp,
	"description":short_description})
# print(wethear_analysis)


wethear_analysis.to_csv("weather.csv")
# print(wethear_analysis.to_csv("weather.csv"))
None
