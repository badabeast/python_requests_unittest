import requests
import pprint
r = requests.get('https://github.com/timeline.json')
print(r.text)




for i in range(1,5):
    print(i)