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
            it['keyword'] = i   #保存关键词到 items
            urls = "https://search.jd.com/Search?keyword={}".format(str(it['keyword']))  #组合关键词连接，传入下一函数使用
            print(urls)
            yield  scrapy.Request(urls,callback=self.readXfrom,meta={'item':it},dont_filter=True)   #传入下一函数，




    def readXfrom(self,response):
        it = response.meta['item']  #读取items
        allti = re.compile('<em>/</em><i>(.*?)</i>', re.S).findall(response.text)[0] #提取出该商品页的页数
        for page in range(int(allti)):  #循环该页数
            url = "https://search.jd.com/Search?keyword={}&enc=utf-8&page={}".format(it['keyword'], str(page + 2))  #组合下一页页数，传入下一函数使用
            print(url)
            yield scrapy.Request(url, callback=self.page_parse,meta={'item':it},dont_filter=True)   #传入下一函数使用






    def page_parse(self,response):
        uids = ""
        jpy = pq(response.text)
        it = response.meta['item']
        ullist = jpy("#J_goodsList > ul > li").items()
        regularlist = re.compile('" href="//item.jd.com/(.*?).html"').findall(response.text)
        for uid in regularlist:
            uids += "https://item.jd.hk/{}.html".format(uid) + "\n"
            it['url'] = uids











