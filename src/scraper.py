import requests
from user_agent import generate_user_agent, generate_navigator
from pprint import pprint
from bs4 import BeautifulSoup

#bibloteki
#user agent - pip
#BeautifulSoup - pip
#lxml - pip


user_Agent = generate_user_agent()
heders = {"user-agent": user_Agent}

r = requests.get("http://gazetaolsztynska.pl/sport-w-Olsztynie/4-0.html")

soup = BeautifulSoup(r.text, "lxml")

body = soup.body
ContainerNews = body.find('div',{'class': 'block-fullnews'})
ListNew = ContainerNews.find_all('li')

header = ListNew[0].find('a',{'class': 'fl'}).get('title')
a2 = ListNew[0].find_all('a')
data = ListNew[0].find('p',{'class': 'block-fullnews-date'}).text
ContentLink = ListNew[0].find('a',{'class': 'fl'}).get('href')
zajawka = a2[2].text
print("stop")