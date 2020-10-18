import unittest
from app.models import News_Source


class NewsSourceTest(unittest.TestCase):
    '''
    To test behavior of news source class
    '''
    def setUp(self):
        '''
        set up method that will run before every test case 
        '''

        self.new_source = News_Source('abc_news', 'abc news', 'A source for news', 'https://abcnews.go.com', 'general')


    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, News_Source))

    def test_init(self):
        '''
        method that tests if news source objects are initiated correctly
        '''
        self.assertEqual(self.new_source.id, 'abc_news')
        self.assertEqual(self.new_source.name, 'abc news')
        self.assertEqual(self.new_source.description, 'A source for news')
        self.assertEqual(self.new_source.url, 'https://abcnews.go.com')
        self.assertEqual(self.new_source.category, 'general')
        

#f __name__ == '__main__':
  #  unittest.main()