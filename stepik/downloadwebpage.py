from urllib.request import  urlopen
import re
from collections import Counter

html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8')
regex = '<code>(.*?)</code>'
s = str(html)
l = sorted(re.findall(regex, s))
b = Counter(l)
print(b)

