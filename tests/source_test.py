import unittest
from .models import Sources

class SourcesTest(unittest.TestCase):
    '''
    Test class to test behaviours of the Sources class
    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test case
        '''
        self.new_source = Sources('abc-news-au','ABC News (AU)', 'Australia\'s most trusted source of local, national and world news. Comprehensive, independent, in-depth analysis, the latest business, sport, weather and more.',"http://www.abc.net.au/news","general")

    def test_instance(self):
        '''
        Test case to check if self.new_source is an instance of Source
        '''
        self.assertTrue(isinstance(self.new_source,Sources))
