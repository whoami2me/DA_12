# Use the Request and scrapy Library
import requests
import scrapy
from unittest import TestCase

# Set the Target Website
url = 'https://brickset.com/sets/year-2009'
req = requests.get(url)

# This will get the status code
print("Status code:")
print("\t *", req.status_code)

# This will get only just the headers
h = requests.head(url)
print("Header:")
print("**********")

# To print line by line
for line in h.headers:
    print("\t", line, ":", h.headers[line])
print("**********")

# This will modify the headers user-agent
headers = {
    'User-Agent': 'Mobile'
}
modified_ua = requests.get(url, headers=headers)
print(modified_ua.request.headers)
print("**********")

# creating scrapy spider 
class BrickSetSpider(scrapy.Spider):
    # name of the spider 
    name = "brickset_spider"
    # set the target url
    start_urls = ['https://brickset.com/sets/year-2009']
    # parsing function to extract jpg files 
    def parse(self, response):
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):
            urls = brickset.get()
            #extract only jpg files
            if any(extension in urls for extension in ['.jpg']): 
                IMAGE_SELECTOR = 'img ::attr(src)'
                yield {
                 'Image Link': brickset.css(IMAGE_SELECTOR).extract_first(),
                }
       
# To recurse to next page
        Page_selector = '.next a ::attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
          yield scrapy.Request(
          response.urljoin(next_page),
          callback=self.parse
          )
        
# Test Case 
class test_part(TestCase):
    #function to test status code of 200
    def test_sc(self):
        sample_url = 'https://brickset.com/sets/year-2009'
        response = requests.get(sample_url)
        self.assertEqual(response.status_code, 200)
    
    # testing of modified user agent to mobile 
    def test_mua(self):
        sample_url2 = 'https://brickset.com/sets/year-2009'
        headers = {'User-Agent': 'Mobile'}
        responseua = requests.get(sample_url2, headers=headers)
        self.assertEqual(responseua.request.headers, {'User-Agent': 'Mobile', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'})
