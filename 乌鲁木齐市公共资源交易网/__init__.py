import pprint
import time

import requests
headers = {
    'Accept': "application/json, text/javascript, */*; q=0.01",
    'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
    'X-Requested-With': "XMLHttpRequest",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
}
data={
    'ImgGuid': 'undefined',
    'YZM': 'undefined',
    'categoryNum': '001001',
    'jyStatus': "",
    'kw': "",
    'pageIndex': 4,
    'pageSize': 15,
    'siteGuid': "7eb5f7f1-9041-43ad-8e13-8fcb82ea831a"
}
response = requests.post(
    'http://zwfw.wlmq.gov.cn/EWB-FRONT/rest/frontAppCustomAction/getPageInfoListNewYzm',
    headers=headers,
    data=data
).json()
pprint.pprint(response.get('custom').get('infodata'))