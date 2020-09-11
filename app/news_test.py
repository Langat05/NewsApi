class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,title, description, url, urlToImage):
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage

import unittest
from models import news , articles
News = news.news

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('title','Corona virus vaccines have been found','"http://www.bbc.co.uk/news','image')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))
        
    def test_check_instance_variables(self):
        self.assertEquals(self.new_news.title,'title')
        self.assertEquals(self.new_news.description,'description')
        self.assertEquals(self.new_news.url,"url")
        self.assertEquals(self.new_news.urlToImage,'urlToImage')
       