import requests

url = input("Please enter url:")
req = requests.get(url)

print("Status code:")
print("\t *", req.status_code)

header = requests.head(url)
print("Header:")
print("**********")

for line in header.headers:
    print("\t", line, ":", head.headers[line])
print("**********")

headers = {
    'User-Agent' : 'Mobile'
}

# Test it on an external site
url2 = input("Please enter url2:")
modified_ua = requests.get(url2, headers=headers)
print(modified_ua.text)












