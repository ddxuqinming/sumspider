import  urllib.request

class DownloadManage:
    def __init__(self):
        pass
    def download(self,url):
        if url is None:
            return


        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
        }

        request = urllib.request.Request(url, headers=header)
        response = urllib.request.urlopen(url)
        if response.getcode() != 200:   # 如果返回的状态码不是200代表异常
            return "no"
        html= response.read()
        return html


test=DownloadManage()
test.download("http://ex.warom.com/product/Index.aspx?TypeId=82bb2fcb-435b-478d-8e60-b2881cf9f7be")