from urllib.request import urlopen
import xml.etree.ElementTree as et
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

resp = urlopen("http://py4e-data.dr-chuck.net/comments_686364.xml",context=ctx)
data = resp.read()
# data = data.decode()
tree = et.fromstring(data)
counts = tree.findall('.//count')
sum=0
for count in counts:
    sum += int(count.text)
print(sum)