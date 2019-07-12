#主入口 2019-7-1
from spiders.spider import Spider
from subSpider.baidu_OutManage import baidu_OutManage
sp1= Spider( )
sp1.homeUrl="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%8D%8E%E8%8D%A3&oq=java%2520%25E4%25B8%2580%25E4%25B8%25AA%25E6%2596%2587%25E4%25BB%25B6%25E5%25A4%259A%25E4%25B8%25AA%25E7%25B1%25BB&rsv_pq=d510f95b000c40c2&rsv_t=1ef9aGtgQAZGt7yqKAxBy1LEtG20boYrbvmUKoY%2B8lqO4kuUzOjs7T17AHY&rqlang=cn&rsv_enter=1&rsv_dl=tb&inputT=2441&rsv_sug3=13&rsv_sug2=0&rsv_sug4=2442"
sp1.out= baidu_OutManage()
sp1.run();





