import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import re
url='https://comment.bilibili.com/372148217.xml'
response=requests.get(url)
response.encoding='utf8'
# print(response)
soup=BeautifulSoup(response.text,'lxml')
d=soup.find_all('d')
#dlst=[]
n=0
for i in d:
    sa=str(i)
    list_1=re.findall('<d p="(.*?),0,.*?">(.*?)</d>',sa)[0]
    timeStamp_1=list_1[0].split(',')[4]
    timeStamp=int(timeStamp_1)
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)#10位时间戳转换为日期
    name_text=i.text
    print(otherStyleTime,name_text)

    # n+=1
    # danmuku={}  #将单条数据装进字典
    # # danmuku["弹某"]=i.text
    # # danmuku["网t址"]=url
    # danmuku["时i间"]=i.#需要先导入datetime库
    # #dlst.append(danmuku)#将所有字典装进一个列表
    # print('获取了%i条数据' % n)
    # print(danmuku)
