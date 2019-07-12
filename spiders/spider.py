from spiders.DownloadManage import DownloadManage
from spiders.OutManage import OutManage
from spiders.UrlManage import UrlManage

class Spider:
    homeUrl=''
    def __init__(self):
        self.urls = UrlManage()
        self.downloader=DownloadManage()
        self.out=OutManage()


    def run(self):
        self.urls.addUrl(self.homeUrl)
        i=0
        while self.urls.hasUrl():
           url = self.urls.getNextUrl()
           html = self.downloader.download(url)
           newurls,newData =self.out.htmlParser(url,html)
           self.urls.addUrls(newurls)
           self.out.show(url,newData)
           i=i+1
           if i>50:
               break;
