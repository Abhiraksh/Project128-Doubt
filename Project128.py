from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests
import csv

starData = []

URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

browser = requests.get(URL)

soup = BeautifulSoup(browser.text, "html.parser")

starTable = soup.find_all("table")

tableRow = starTable[7].find_all("tr")

print(tableRow)

time.sleep(10)



# headers = ["Brown_Dwarf","Constellation","Right_Acension","Declination","App_Mag","Distance_in_Light_Years",
#     "Spectral_Type","Mass","Radius","Discovery_Year"]

# def scrape():
#     for i in tableRow:
#         for tdTag in soup.find_all("td", attrs={"class", "new"}):
#             td_tags = tdTag.find_all("td")
#             tempList = []
#             for index, td_tag in enumerate(td_tags):
#                 if index == 0:
#                     tempList.append(td_tag.find_all("a")[0].contents[0])
#                 else:
#                     try:
#                         tempList.append(td_tag.contents[0])
#                     except:
#                         tempList.append("")

#             # Get Hyperlink Tag
#             hyperlink_li_tag = td_tags[0]

#             tempList.append("https://en.wikipedia.org/wiki/List_of_brown_dwarfs"+ hyperlink_li_tag.find_all("a", href=True)[0]["href"])
            
#             starData.append(tempList)
# scrape()


# with open("starData.csv", "w") as f:
#         csvwriter = csv.writer(f)
#         csvwriter.writerow(headers)
#         csvwriter.writerows(starData)