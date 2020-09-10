from flask import Flask, render_template
from newsapi import NewsApiClient
import os


app = Flask(__name__)

@app.route('/')
def index():
    newsapi = NewsApiClient(api_key="d40c178ee0c6474f963ed683b651a3ab")
    topheadlines = newsapi.get_top_headlines(sources="abc-news")


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img)    

    return render_template('index.html', context = mylist)

if __name__ == "__main__":
    app.run(debug=True)


