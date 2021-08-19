#part8
import scrapy
from scrapy.http import HtmlResponse
import grp12
import unittest
from betamax import Betamax
from betamax.fixtures.unittest import BetamaxTestCase

with Betamax.configure() as config:
    config.cassette_library_dir = 'cassettes'
    config.preserve_exact_body_bytes = True
    
class TestExample(BetamaxTestCase):
    
    def test_parse(self):
        new_spider = grp12.New_Spider()
        
        response = self.session.get(new_spider.start_urls)
        
        scrapy_response = HtmlResponse(body=response.content,url=new_spider.start_urls)
        
        result = new_spider.parse(scrapy_response)
        
        self.assertEqual({'Image Link': u'image1.jpg'}, result.next())
        self.assertEqual({'Image Link': u'image2.jpg'}, result.next())
        self.assertEqual({'Image Link': u'image3.jpg'}, result.next())
        self.assertEqual({'Image Link': u'image4.jpg'}, result.next())
        self.assertEqual({'Image Link': u'image5.jpg'}, result.next())
        
        with self.assertRaises(StopIteration):
            result.next()
