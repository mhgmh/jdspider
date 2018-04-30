import requests

se = requests.session()


data = {
    'title':'1111111111',
    'article_cat':'1002',
    'article_type':'0',
    'is_open':'1',
    'author':'',
    'author_email':'',
    'keywords':'',
    'description':'',
    'sort_order':'50',
    'link_url':'http://',
    'FCKeditor1':'222222222222',
    'category_name':'请选择分类',
    'category_id':'0',
    'brand_name':'',
    'brand_id':'0',
    'search_brand_keyword':'',
    'ru_id':'',
    'keyword':'',
    'submit':'确定',
    'act':'insert',
    'old_title':'',
    'id':''
}


files = {'file': ('1150025-20170519162723338-1669677972.png', open('1150025-20170519162723338-1669677972.png', 'rb'), 'image/png')}

headers = {
    #'content-type':'multipart/form-data; boundary=----WebKitFormBoundaryfxJbv5aHncIqaG3E',
    'cookie':'ECSCP[admin_id]=57; ECSCP[admin_pass]=2d97df17dcf5bde502bb355ef394ec3f; ECSCP[page_size]=15; ECSCP[lastfilterfile]=8A8B0004; ECSCP[lastfilter]=a%253A6%253A%257Bs%253A6%253A%2522cat_id%2522%253Bi%253A0%253Bs%253A12%253A%2522record_count%2522%253Bs%253A1%253A%25222%2522%253Bs%253A9%253A%2522page_size%2522%253Bi%253A15%253Bs%253A4%253A%2522page%2522%253Bi%253A1%253Bs%253A10%253A%2522page_count%2522%253Bd%253A1%253Bs%253A5%253A%2522start%2522%253Bi%253A0%253B%257D; ECSCP[lastfiltersql]=U0VMRUNUICogRlJPTSBgZl83NWhiX2NvbWAuYGRzY19hcnRpY2xlX2NhdGAgICBXSEVSRSAxIEFORCBwYXJlbnRfaWQgPSAwIEdST1VQIEJZIGNhdF9pZCAgT1JERVIgQlkgcGFyZW50X2lkLCBzb3J0X29yZGVyIEFTQyAgTElNSVQgMCwgMTUg; session_id_ip=125.70.189.135_da6f8c28b73595f36f61739e4e840f15; UM_distinctid=162f06c8fa8ac1-035cb996f0e0d6-18760b16-1fa400-162f06c8fa992c; ECS[history]=32253%2C35578%2C32991%2C35588; ECS[list_history]=32253%2C35578%2C32991%2C35588; Z41o_2132_saltkey=cyyJCYcp; Z41o_2132_lastvisit=1524924936; Z41o_2132_atarget=1; Z41o_2132_forum_lastvisit=D_54_1524928536; Z41o_2132_smile=1D1; Z41o_2132_visitedfid=70D57D54; _umdata=0712F33290AB8A6D35EC4A5CB99763D0E0915B5A4CE77DF3C2EBCA1FB723D3FC931B74F9C7FA4AF8CD43AD3E795C914CED07B932745EA27F6F95C32B550F07EF; Z41o_2132_ulastactivity=a1b5vZAKWi%2BnOQcKG9hwKlmimxizl6kMdOaqIfX7MM8Jc8ZtGD%2BD; Z41o_2132_nofavfid=1; Z41o_2132_lastcheckfeed=1%7C1524967860; CNZZDATA1273495606=15381805-1524452069-%7C1524965435; real_ipd=125.70.189.85; dsc_real_ip=125.70.189.85; ECSCP_ID=ce7e0f3463c71ddaefe27cc1bdd1049c0cce11e4; yunsuo_session_verify=ad697c699b1d9f45333513e12e00f37b; adminStartHome=cookieValue; ECS_ID=1d06be7bad0d106355e2cfc29f1760623ff2a526; ECS[visit_times]=3; nb-referrer-hostname=www.75hb.com; nb-start-page-url=https%3A%2F%2Fwww.75hb.com%2F; ECS[display]=grid; dscUrl=articlecat.php%3Fact%3Dlist; dscActionParam=menuplatform%7C02_articlecat_list; province=26; city=322; district=2722; street=0; street_area=0; Hm_lvt_d37804ec3d9bfa562610cdb6525fadd5=1524965436,1524965446,1524965446,1525076937; Hm_lpvt_d37804ec3d9bfa562610cdb6525fadd5=1525077203',
    'origin':'https://www.75hb.com',
    'referer':'https://www.75hb.com/admin/article.php?act=add',
    'upgrade-insecure-requests':'1',
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36 QQBrowser/4.3.4986.400',




}

se.headers.clear()
se.headers.update(headers)

s = se.post('https://www.75hb.com/admin/article.php',files = files,data=data).text
print(s)
