import unittest
from app.models import Articles

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('BBC News','EU acts against Poland judiciary reforms', 'Unprecedented disciplinary measures are taken as the EU says the reforms threaten the rule of law.', 'https://ichef.bbci.co.uk/news/1024/cpsprodpb/F046/production/_98901516_2efffed4-d4a6-486a-8a78-112232b92faa.jpg','http://www.bbc.co.uk/news/world-europe-42420150', '2017-12-20T13:36:14Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))



if __name__ ==  '__main__':
    unittest.main()
