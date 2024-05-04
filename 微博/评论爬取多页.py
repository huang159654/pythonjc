import csv
import threading
import time
from random import random

import requests
from datetime import datetime #时间转换
lock = threading.Lock()
f=open('v_147.csv',mode='a',encoding='utf_8_sig',newline='')
csv_writer=csv.DictWriter(f,fieldnames=[
    '评论id',
    '用户名',
    '评价',
    '用户点赞',
    '楼层',
    'id',
    '评论时间',
    'ip地址',
])
csv_writer.writeheader()
headers={
    #当出现无法报错的情况时，就是需要更换cookie，或者更换next='count=10'，也就是 max_id返回的这个参数，
    'cookie': 'UOR=www.baidu.com,weibo.com,www.baidu.com; SINAGLOBAL=2649348612320.8965.1683123322503; XSRF-TOKEN=Esh3O_pyGuemuWbImpjxEg_i; SSOLoginState=1684306503; _s_tentry=weibo.com; Apache=3879985320386.9004.1684412843149; ULV=1684412843250:4:4:2:3879985320386.9004.1684412843149:1684137851028; MEIQIA_TRACK_ID=2Py8D3iO5ERjFy4p4XveSohCCbT; MEIQIA_VISIT_ID=2Py8D5U0pLf0VGN2Idzc6ud8scb; WBPSESS=LRG5opETtpCx6hjj5OrpxsIue_hf0zCivLYWxpShWfkMijk3IM20fE4MW_g2ZYeeD2aNiEHSFkTzLwCJ8eDVyApga2gUpgrRLFtpyO04O4QIlb2g1kLj9YS-oyb2txvWvHjmys8m5R8QjCEGKGXLEA==; UPSTREAM-V-WEIBO-COM=35846f552801987f8c1e8f7cec0e2230; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5iFY70K82Pxs3e8U2VB8g25JpX5KMhUgL.FoMRe0zRe0n0eo52dJLoIEzLxK-LB-qLBo.LxK-LB-qLBo.LxK-LB-qLBoLkeo5Ee05f; ALF=1687080186; SCF=AiY6_xhGYt00HPRl7b6wPZDN_qdWxa2lmLM5DQP4y-HReKeDAeTmmlcPr1iADhYPbpjFVAQUgiDSjwgRf4sq4gI.; SUB=_2A25JY0-tDeRhGeFG6FAZ8ybPyTyIHXVqGSZlrDV8PUNbmtANLVWmkW9NedA6PVVdri7WwryJTNaSkYJONS0HiByH',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}
#https://weibo.com/2803301701/N3aW86En4例子
#2803301701这个是博主的id
#N3aW86En4这个是文章的id
#https://weibo.com/ajax/statuses/buildComments?is_reload=&id=4907570281585158&is_show_bulletin=3&is_mix=0&{next}&uid=2803301701&fetch_level=0
#想要换个微博，修改微博文章的id是id=4907570281585158，修改后面的数字就行，换博主的的id是uid=2803301701，修改后面的数字就行
def get_count(next='max_cursor=0'):
    # time.sleep(random.randint(10, 20))
    #is_mix这个是翻页的一个参数
    url=f'https://weibo.com/ajax/statuses/buildComments?is_reload=&id=4907570281585158&is_show_bulletin=3&is_mix=0&{next}&uid=2803301701&fetch_level=0'
    response=requests.get(url=url,headers=headers).json()
    max_id_0=response['max_id']
    data = response['data']
    for i in data:
        try:
            json_ID=i.get('id')# 评论id
            json_name_1=i['user']['screen_name']#用户名
            json_na_me= i['text_raw']#评价
            json_give = i.get('like_counts')#用户点赞
            json_floor_number=i.get('floor_number')#楼层
            json_ID_1 = i['user'].get('id')#id
            Comment_time = i['created_at']
            d = Comment_time
            json_time = datetime.strptime(d, '%a %b %d %X %z %Y')  # 评论时间
            json_name = i['user'].get('location')#ip地址
            dit = {'评论id':json_ID,
                   '用户名':json_name_1,
                   '评价':json_na_me,
                   '用户点赞':json_give,
                   '楼层':json_floor_number,
                   'id':json_ID_1,
                   '评论时间':json_time,
                   'ip地址':json_name
                   }
            print(json_ID,
                  json_name_1,
                  json_na_me,
                  json_give,
                  json_floor_number,
                  json_time,
                  json_name,
                  json_ID_1
                  )
            csv_writer.writerow(dit)
        except Exception as e:
            e
    max_id ='max_id='+str(max_id_0)
    get_count(max_id)
if __name__ == '__main__':
    get_count()