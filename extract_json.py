import json
from urllib.request import urlopen
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

res = urlopen('http://py4e-data.dr-chuck.net/comments_686365.json',context=ctx)
data = res.read().decode()
print(data)
print("...................")
data = json.loads(data)
print(len(data['comments']))
sum=0
for user in data['comments']:
    sum+=user['count']
print(sum)