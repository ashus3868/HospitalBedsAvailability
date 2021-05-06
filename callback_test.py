import requests
from bs4 import BeautifulSoup

# data=requests.post("http://localhost:5005/webhooks/rest/webhook",json={"sender":"ashu","message":"hello"})
data=requests.get('https://youtu.be/VdTviH5Svzc')
print(data.text)

x=BeautifulSoup(data.text)
print(x.findAll('img'))#, attrs={'class':'style-scope yt-img-shadow'}))