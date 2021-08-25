import requests
import scrapy

url = 'https://brickset.com/sets/year-2009'
req = requests.get(url)
print(req.text)

print("Status code:")
print("\t *", req.status_code)

h = requests.head(url)
print("Header:")
print("**********")

for line in h.headers:
    print("\t", line, ":", h.headers[line])
print("**********")

headers = {
    'User-Agent': 'Mobile'
}
modified_ua = requests.get(url, headers=headers)
print(modified_ua.request.headers)
print("**************")

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

