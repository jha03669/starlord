from urllib.request import urlopen
from bs4 import BeautifulSoup
tpp='https://en.wikipedia.org/wiki/'
ur=input('enter name in camel casing:').split()
name='_'.join(ur)
url=tpp+name
page=urlopen(url)
html=page.read()
page.close()
psoup=BeautifulSoup(html,'html.parser')
contain=psoup.findAll('p')
for para in contain:
    if len(para)>1:
        print(para.text)
        break
