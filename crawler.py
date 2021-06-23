from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urlopen("http://py4e-data.dr-chuck.net/comments_686362.html",context=ctx).read()
soup = BeautifulSoup(html,"html.parser")
tags = soup('span')
sum=0
for tag in tags:
    sum+ =int(tag.contents[0])
print(sum)