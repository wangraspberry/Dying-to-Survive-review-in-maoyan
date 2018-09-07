import requests
from pyquery import PyQuery as pq
import time

url = 'http://maoyan.com/films/1200486'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
html = requests.get(url,headers=headers).text
doc = pq(html)
items = doc('.comment-container').items()

for item in items:
    author = item.find('.name').text()
    answer = item.find('.comment-content').text()
    print(author)
    print(answer)
    file = open('explore.txt','a',encoding='utf-8')
    file.write('\n'.join([author,answer]))
    file.write('\n'+'='*50+'\n')
    file.close()
