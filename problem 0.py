import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=iceland")

pyresponce = json.load(response)

#print pyresponce["results"]

results = pyresponce["results"]

for i in range(10):
    print results[i]["text"]
