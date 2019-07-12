import re
import urllib
from bs4 import BeautifulSoup

class OutManage:
    def __init__(self):
        pass

    def htmlParser(self,byUrl,htmlContent ):
        soup = BeautifulSoup(htmlContent, 'html.parser', from_encoding='utf-8')
        new_urls = self.get_new_urls(byUrl, soup)
        new_datas = self.get_new_datas(byUrl, soup)
        return new_urls, new_datas

    def get_new_urls(self, byUrl, soup):
        newurls = set()
       # links = soup.find_all('a',href=re.compile(r'\javascript:'))
        links = soup.find_all('a')
        for link in links:
            url=link["href"]
            new_full_url = urllib.parse.urljoin(byUrl, url) #生成完整url
            newurls.add(new_full_url)
        return newurls


    def get_new_datas(self, byUrl, soup):
        new_datas = []
        lists = soup.find('div', class_='right-body').find_all('div', class_='iteam')
        for list in lists:
           data={}
           # 获取标题内容
           title_node = list.find('h5')
           data['title'] = title_node.get_text()
           # 获取img
           img_node = list.find('div', class_='iteam-img').find('img')
           data['img'] = img_node['src']
           new_datas.append(data)
        return new_datas

    def show(self,byUrl,new_datas):
        print(new_datas)
