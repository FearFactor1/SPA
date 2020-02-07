from urllib.request import  urlopen
from bs4 import BeautifulSoup


html = urlopen("https://stepik.org/media/attachments/lesson/209723/5.html").read().decode('utf-8')
s = str(html)
soup = BeautifulSoup(s, 'html.parser')
t = []
sum = 0
for td in soup('td'):
       sum = sum + int(td.text)
print(sum)
