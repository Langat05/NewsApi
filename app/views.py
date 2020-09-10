from flask import Flask
from newsapi import NewsApiClient


App = Flask(__name__)

@app.route('/')
def index():
    newsapi = NewsApiClient(api_key="d40c178ee0c6474f963ed683b651a3ab")
    topheadlines = newsapi.get_headlines(sources="abc-news")


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = [articles[i]]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])


