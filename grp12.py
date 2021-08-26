import requests
import scrapy
import unittest
from unittest import TestCase
import json

url = 'https://brickset.com/sets/year-2009'
req = requests.get(url)

print("Status code:")
print("\t *", req.status_code)
x=input("smth")
h = requests.head(url)
print("Header:")
print("**********")

for line in h.headers:
    print("\t", line, ":", h.headers[line])
print("**********")
y=input("smmth")
headers = {
    'User-Agent': 'Mobile'
}
modified_ua = requests.get(url, headers=headers)
print(modified_ua.request.headers)
print("**************")
z = input("smth")
class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['https://brickset.com/sets/year-2009']

    def parse(self, response):
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):
            urls = brickset.get()
            if any(extension in urls for extension in ['.jpg']):
                IMAGE_SELECTOR = 'img ::attr(src)'
                yield {
                 'Image Link': brickset.css(IMAGE_SELECTOR).extract_first(),
                }

        Page_selector = '.next a ::attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
          yield scrapy.Request(
          response.urljoin(next_page),
          callback=self.parse
          )

class test_part5(TestCase):
    def test_sc(self):
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

    def mua(self):
        responseua = modified_ua
        self.assertEqual(responseua.request.headers, {'User-Agent': 'Mobile', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'})

class test_file(TestCase):
    def test_json(self):
        f = open("resultss.json",)
        data_jpg = json.loads(f.read())
        self.assertEqual(data_jpg[1], {'Image Link': 'https://images.brickset.com/sets/small/3594-1.jpg?200811140307'})
        f.close()