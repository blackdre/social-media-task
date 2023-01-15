import requests
import json
twitter = requests.get(
    'https://takehome.io/twitter')
print(twitter.json())
