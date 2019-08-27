#Webscraper
from bs4 import BeautifulSoup
import requests

class Article():
    def __init__(self, newsId, title, url, discipline, description, source, date, author, competition, commentsCount):
        self.newsId = newsId
        self.title = title
        self.url = url
        self.discipline = discipline
        self.description = description
        self.source = source
        self.date = date
        self.author = author
        self.competition = competition
        self.commentsCount = commentsCount
        
def reformatingArticle(articleHTMLCode):
    soup = BeautifulSoup(articleHTMLCode, "html.parser")
    divContent =   " ".join([div.text for div in soup.find_all('div')])
    pContent = " ".join([p.text for p in soup.find_all('p') if "lang" not in p.attrs])
    spanContent = " ".join([span.text for span in soup.find_all('span')])
    return spanContent+ " "+pContent +" "+ divContent
  
allArticles = []

def getDetails(newsDict):
    for news in newsDict['news']:
        #print(news)
        try:
            newsId = news['id']
            title = news['title'] 
            url = news['url'] 
            discipline = news['discipline'] 
            description = news['description'] 
            source = news['source'] 
            date = news['added_datetime'] 
            author = news ['author'] 
            competition = news['competition']
            commentsCount = news['comments_count']
            
            allArticles.append(
                Article(
                    newsId, 
                    title, 
                    url, 
                    discipline, 
                    reformatingArticle(description), 
                    #description,
                    source, 
                    date, 
                    author, 
                    competition, 
                    commentsCount
                )
            )
        except:
            print("Article Schema Error")
        
def getJsons():
    webPagesIndex = 1
    while True:
        print(webPagesIndex)
        articlesPage = requests.get('https://www.meczyki.pl/front/news/get-list?page={}'.format(webPagesIndex)).json()
        #request always return some result, but since some value list is empty
        if articlesPage['news'] != []:
            getDetails(articlesPage)
            webPagesIndex += 1
        else:
            return False

getJsons()

