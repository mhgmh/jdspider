import requests
from lxml import etree as et
from pyquery import PyQuery as pq
import re

se = requests.session()

class New_project(object):

    def release_now(url):
        name = ''
        imgurl = ''
        headers = {
            'Host':'item.secoo.com',
            'Referer':'http://list.secoo.com/bags/30-0-0-0-0-1-0-0-1-10-0-0.shtml',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36 QQBrowser/4.3.4986.400',
        }

        se.headers.clear()
        se.headers.update(headers)
        content = str(se.get(url).content,'utf-8')
        jpy = pq(content)
        f = et.HTML(content)
        title = str(f.xpath("//div[@class='proName']/h2/text()")[0])    #产品标题
        tds = jpy('#showAdds > div.showAddsRight.fr > div.s-left-box > div.product-detail-div.clearfix > div.t-info > table > tbody > tr > td').items()
        for td in tds:
            name += td('div.zxx_con').text() + "\n"
        ps = str(jpy('#showAdds > div.showAddsRight.fr > div.s-left-box > div.product-detail-div.clearfix > div > p'))
        img = re.compile('data-original="(.*?)"',re.S).findall(ps)
        for i in img:
            imgurl += '<img src="{}" alt="" />'.format(i)+"\n"

        try:
            introduce = str(f.xpath("//div[@class='brand-col2 fr']/div[@class='b-con']/text()")[0]).replace(' ',"").replace('\n','')+'\n'       #描述信息
        except IndexError :
            return   title ,name + '\n' + imgurl
        return title , introduce + '\n' + name  + '\n' + imgurl












file =  New_project.release_now('http://item.secoo.com/30761133.shtml?source=list')


