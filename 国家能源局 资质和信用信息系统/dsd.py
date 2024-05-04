import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://zzxy.nea.gov.cn',
    'Referer': 'http://zzxy.nea.gov.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

data = {
    'entername': '',
    'belognea': '',
    'socialcreditno': '',
    'size': '10',
    'current': '1',
}

response = requests.post('http://zzxy.nea.gov.cn/public/login-service/login/getXkgsList', headers=headers, data=data,
                         verify=False).json()
list_da = response.get('data').get('records')
for list in list_da:
    list_entername = list.get('entername')  # 企业名称
    list_socialcreditno = list.get('socialcreditno')  # 社会信用
    list_licenceno = list.get('licenceno')  # 许可证编号
    list_applydetail = list.get('applydetail')  # 申请许可内容
    list_createtime = list.get('createtime')  # 许可发证日期
    list_acceptorgname = list.get('acceptorgname')  # 许可发证机关
    list_licvalidstart = list.get('licvalidstart')  # 有效起始日期
    list_licvalidend = list.get('licvalidend')  #有效到期日期
    print(list_entername,
          list_socialcreditno,
          list_licenceno,
          list_applydetail,
          list_createtime,
          list_acceptorgname,
          list_licvalidstart,
          list_licvalidend)
