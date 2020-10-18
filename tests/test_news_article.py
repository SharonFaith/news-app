import unittest
#from models import news_article
from app.models import News_Article
#News_Article = news_article.News_Article

class NewsArticlesTest(unittest.TestCase):
    '''
    To test behavior of news articles class
    '''
    def setUp(self):
        '''
        set up method that will run before every test case 
        '''

        self.new_article = News_Article('abc_news', 'urlToImage', 'title of the article', 'description of the article', 'time of publishing', 'url of article')


    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, News_Article))


    def test_init(self):
        '''
        method that tests if news article objects are initiated correctly
        '''
        self.assertEqual(self.new_article.id, 'abc_news')
        self.assertEqual(self.new_article.image_url, 'urlToImage')
        self.assertEqual(self.new_article.title, 'title of the article')
        self.assertEqual(self.new_article.description, 'description of the article')
        self.assertEqual(self.new_article.time, 'time of publishing')
        self.assertEqual(self.new_article.url, 'url of article')
        

#if __name__ == '__main__':
 #   unittest.main()