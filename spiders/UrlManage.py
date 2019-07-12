class UrlManage:
    urls =set()  # 待处理 集合会自动去重复
    urlsEnd = set() # 已处理
    def __init__(self):
        pass

    def  addUrl(self,url):
        if  url not in  self.urls and   url not in  self.urlsEnd:
           self.urls.add(url);
    def addUrls(self,urls):
        for url in urls:
            self.addUrl(url)
    def getNextUrl(self):

        url=self.urls.pop()
        self.urlsEnd.add(url)
        return  url
    def hasUrl(self):
        return len(self.urls)>0
