import requests
import scrapy

# need function 
url = input("Please enter url:")
r = requests.get(url)

print("Status code:")
print("\t *", r.status_code)

h = requests.head(url)
print("Header:")
print("**********")

for line in h.headers:
    print("\t", line, ":", h.headers[line])
print("**********")

headers = {
    'User-Agent' : 'Mobile'
}

url2 = input("Please enter url:")
modified_ua = requests.get(url2, headers=headers)
print(modified_ua.text)

print("end of part 5 \n**************************")

class NewSpider(scrapy.Spider):
 name = "new spider"
 start_urls = [input("pls enter a url")]
 def parse(self,response):
  css_selector = 'img'
  for x in response.css(css_selector):
       url = x.get()
       if any(extension in url for extension in ['jpg']):
        newsel = '@src'
        yield{
          'Image Link' : x.xpath(newsel).extract_first(),
        }
        
        Page_selector = '.next a ::attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
          yield scrapy.Request(
          response.urljoin(next_page),
          callback=self.parse
          )

#all done 
