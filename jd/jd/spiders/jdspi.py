# -*- coding: utf-8 -*-
import scrapy
import requests
from pyquery import  PyQuery as pq
import re
from ..items import JdItem
se = requests.session()

class JdspiSpider(scrapy.Spider):
    name = 'jdspi'
    allowed_domains = ['jd.com']
    start_urls = ['http://jd.com/']

    def parse(self, response):
        keys = open("keyword.txt").read().split("\n")   #提取搜索需要的关键词，以txt文档模式保存,提取出来后，用split("\n") 按换行分割
        it = JdItem()
        for i in keys:
            self.key = i   #保存关键词到 items
            urls = "https://search.jd.com/Search?keyword={}".format(str(self.key))  #组合关键词连接，传入下一函数使用
            self.url = urls
            yield  scrapy.Request(self.url,callback=self.readXfrom,meta={'item':it})   #传入下一函数，




    def readXfrom(self,response):
        page = 0
        s = 1
        title = re.compile('<strong class="search-key">"(.*?)"</strong>',re.S).findall(response.text)[0]
        it = response.meta['item']  #读取items
        allti = re.compile('<em>/</em><i>(.*?)</i>', re.S).findall(response.text)[0] #提取出该商品页的页数
        for page in range(0,int(allti),2):  #循环该页数
            url = "https://search.jd.com/Search?keyword="+title+"&enc=utf-8&page="+str(page+1)+"&s="+str(s)+"&click=0"  #组合下一页页数，传入下一函数使
            s = s+60
            headers = {

                'Cookie':'qrsc=3; __jdv=122270672|direct|-|none|-|1524143448455; PCSYCityID=1962; ipLoc-djd=1-72-2799-0; __jda=122270672.1853676787.1521628618.1524143448.1524328703.5; __jdb=122270672.5.1853676787|5.1524328703; __jdc=122270672; rkv=V0000; xtest=6093.cf6b6759; __jdu=1853676787; 3AB9D23F7A4B3C9B=J3N2WZRSTUZEJIMNOLJ57MWSXZVMDYYOSKGQKGTTFZJ7LF7Y5UYFIM6EB73R6TDJLIFGALJJOM5N245UWT547ZYFQA',
                'Host':'search.jd.com',
                'Upgrade-Insecure-Requests':'1',
                'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36 QQBrowser/4.2.4763.400',

            }

            yield scrapy.Request(url, callback=self.page_parse,headers=headers,encoding='utf-8',meta={'item':it})   #传入下一函数使用






    def page_parse(self,response):
        uids = ""
        it = response.meta['item']
        regularlist = re.compile('target="_blank" href="//item.jd.com/(.*?).html#comment').findall(response.text)
        for uid in regularlist:
            uids += "https://item.jd.hk/{}.html".format(uid) + "\n"
            print(uids)
            it['url'] = uids

            f = open("urls.txt",'a',encoding='utf-8')
            f.write(uids)
            f.close()
            yield it










