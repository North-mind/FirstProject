import requests
from user_agent import generate_user_agent, generate_navigator
from pprint import pprint
from bs4 import BeautifulSoup

#bibloteki
#user agent - pip
#BeautifulSoup - pip
#lxml - pip


# user_Agent = generate_user_agent()
# heders = {"user-agent": user_Agent}

ARTICLELIST =[]

class Article:
    def __init__(self, Title, Date, Teaser, Content):
        self.Title = Title
        self.Date = Date
        self.Teaser = Teaser
        self.Content = Content

def GetListArticleOnPage(xUriPageArticle):
   
    pRequest = requests.get(xUriPageArticle)
    
    if(pRequest.status_code > 200): 
        return ""
        
    pSoup = BeautifulSoup(pRequest.text, "lxml")
    pContainer = pSoup.body.find('div',{'class': 'block-fullnews'})
    pArticleContentList =pContainer.find_all('li')

    return pArticleContentList

def GetArticlesFromArticleList(xArticleList):
    
    for pArticle in xArticleList:
        try:
            pTitle = pArticle.find('a',{'class': 'fl'}).get('title')
            pA_Attributes = pArticle.find_all('a')
            pData = pArticle.find('p',{'class': 'block-fullnews-date'}).text
            pTeaser = pA_Attributes[2].text
            pContentLink = pArticle.find('a',{'class': 'fl'}).get('href')
            pContenArticle = GetContentArticle(pContentLink)
            pArticle = Article(pTitle,pData,pTeaser,pContenArticle)
            ARTICLELIST.append(pArticle)
        except:
            print("bat article shema")
   


def GetContentArticle(xUrl):

    foo ="http://sport.wm.pl" in xUrl
    if(foo == False):
        print("Bad url to content")
        return "Bad url to content"

    pRequest = requests.get(xUrl) 
    
    if(pRequest.status_code > 200): 
        return ""

    pSoup = BeautifulSoup(pRequest.text, "lxml")
    pContentAricle = pSoup.body.find('div',{'class': 'art-text intextAd'}).text
    
    return pContentAricle
 
def PaginationArticle():
    for PginIndex in range(320):
        pCurrentPageArticleLists = GetListArticleOnPage("http://gazetaolsztynska.pl/sport-w-Olsztynie/4-"+str(PginIndex)+ ".html")
        print("current page", PginIndex)
        GetArticlesFromArticleList(pCurrentPageArticleLists)
        print("Artykułow w liscie jest:", len(ARTICLELIST))

    # pCurrentPageArticleLists = GetListArticleOnPage("http://gazetaolsztynska.pl/sport-w-Olsztynie/4-4.html")
    # GetArticlesFromArticleList(pCurrentPageArticleLists)
    # print(end)

PaginationArticle()

