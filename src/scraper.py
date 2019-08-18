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

r = requests.get("http://gazetaolsztynska.pl/sport-w-Olsztynie/4-0.html", heders = heders)

soup = BeautifulSoup(r.text, "lxml")


print(r.text)