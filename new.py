import re
f=open('text.txt','r')
sm=0
for l in f:
    sm+=sum(list(map(int,re.findall('[0-9]+',l))))
print(sm)