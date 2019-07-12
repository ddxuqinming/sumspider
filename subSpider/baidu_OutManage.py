import re
import urllib
from bs4 import BeautifulSoup

#baidu 输出器
class baidu_OutManage:
    def __init__(self):
        pass

    def htmlParser(self,byUrl,htmlContent ):
        soup = BeautifulSoup(htmlContent, 'html.parser', from_encoding='utf-8')
        new_urls = self.get_new_urls(byUrl, soup)
        new_datas = self.get_new_datas(byUrl, soup)
        return new_urls, new_datas

    def get_new_urls(self, byUrl, soup):
        newurls = set()
        print(soup)
       # links = soup.find_all('a',href=re.compile(r'\javascript:'))
        links = soup.find(id='page').find_all('a')
        for link in links:
            url=link["href"]
            new_full_url = urllib.parse.urljoin(byUrl, url) #生成完整url
            newurls.add(new_full_url)
        return newurls


    def get_new_datas(self, byUrl, soup):
        print(soup)
        new_datas = []
        lists = soup.find('div', class_='content_left').find_all('div', class_='result')
        for list in lists:
           data={}
           # 获取标题内容
           title_node = list.find('h3').find('a')
           data['title'] = title_node.get_text()
           # 获取内容
           content_node = list.find('div', class_='c-abstract')
           data['content'] = content_node.get_text()
           new_datas.append(data)
        return new_datas

    def show(self,byUrl,new_datas):
        print(new_datas)
