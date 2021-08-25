from scrapy.http import HtmlResponse
import grp12
import requests
import unittest
from unittest import TestCase

session = requests.Session()

class test_part5(TestCase):
    def test_sc(self):
        response = requests.get(grp12.url)
        self.assertEqual(response.status_code, 200)

    def mua(self):
        responseua = grp12.modified_ua
        self.assertEqual(responseua.request.headers, {'User-Agent': 'Mobile', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'})

if __name__ == '__main__':
    unittest.main()



