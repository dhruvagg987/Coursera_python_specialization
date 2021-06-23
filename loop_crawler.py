from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fp = urlopen("http://py4e-data.dr-chuck.net/known_by_Katia.html",context=ctx).read()
soup = BeautifulSoup(fp,"html.parser")
names = soup('a')
# print(names[0].get('href'))
for i in range(6):
    url = names[17].get('href')
    pg=urlopen(url,context=ctx).read()
    soup=BeautifulSoup(pg,"html.parser")
    names=soup('a')
print(names[17].contents[0])