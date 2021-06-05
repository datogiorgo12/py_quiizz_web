import requests
from bs4 import BeautifulSoup
from time import sleep
for i in range(1,4):
    url = f'https://pczone.ge/product-category/%E1%83%99%E1%83%9D%E1%83%9B%E1%83%9E%E1%83%98%E1%83%A3%E1%83%A2%E1%83%94%E1%83%A0%E1%83%94%E1%83%91%E1%83%98/intel-core-i3/page/{i}/'
    r = requests.get(url)
    print(r)
    # print(r.text)
    content = r.text
    soup = BeautifulSoup(content,'html.parser')
    ul = soup.find('ul',{'class':'products columns-4'})
    f = open('file.csv', 'a')
    for x in ul.find_all("li"):
        print(x.h2.text)
        content = f.write(x.h2.text+'\n')
    sleep(15)