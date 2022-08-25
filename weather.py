import requests
from bs4 import BeautifulSoup
stocks = []
page = requests.get("https://www.jumia.com.ng/macbooks/")

soup = BeautifulSoup(page.content, "html.parser")
week = soup.find(class_ ='-paxs row _no-g _4cl-3cm-shs')
# print(week)
items =week.find_all(class_ ='name')
items_2 = week.find_all(class_="prc")
# print(items)
for i in range(20):
	stocks.append(items[i].get_text() + "  : " + items_2[i].get_text())
print(stocks)

# # print(week)\
# print(items)

# # print(items[0])


# # printt(items[0].find(class_ = "period-name"))


# print(items[0].find(class_ = "period-name")).get_text()


# period_names = [item.find(class_ ="period-name").get_text() for item in items]
# # print(period_names)

# short_description = [item.find(class_ ="short-desc").get_text() for item in items]
# # print(short_description)

# temp = [item.find(class_ ="temp").get_text() for item in items]
# # stringed_temp = str(temp)
# # print(stringed_temp)



# import pandas as pd



# wethear_analysis = pd.DataFrame( {
# 	"period":period_names,
# 	"temperature":temp,
# 	"description":short_description})
# # print(wethear_analysis)


# wethear_analysis.to_csv("weather.csv")
# # print(wethear_analysis.to_csv("weather.csv"))
# None
