import requests

cookies = {
    'acw_tc': 'ac11000116832188690667029e0108cb9250decca52e00495d3df1bb843d60',
    '_zcy_log_client_uuid': '6867d8a0-ea9b-11ed-9704-0513cc875592',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'acw_tc=ac11000116832188690667029e0108cb9250decca52e00495d3df1bb843d60; _zcy_log_client_uuid=6867d8a0-ea9b-11ed-9704-0513cc875592',
    'Origin': 'http://www.whggzy.com',
    'Pragma': 'no-cache',
    'Referer': 'http://www.whggzy.com/PoliciesAndRegulations/GovernmentProcurement/index.html?utm=sites_group_front.108bd4c4.0.0.091835a0ea9d11edacfa33be4b33262a',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

json_data = {
    'utm': 'sites_group_front.108bd4c4.0.0.091835a0ea9d11edacfa33be4b33262a',
    'categoryCode': 'GovernmentProcurement',
    'pageSize': 15,
    'pageNo': 4,
}

response = requests.post(
    'http://www.whggzy.com/front/search/category',
    cookies=cookies,
    headers=headers,
    json=json_data,
    verify=False,
).json()
print(response)