import json
import pprint
import re

import requests
url = 'https://www.douyin.com/video/7329556357676305679'
# 请求头headers
headers = {
    # 用户信息, 常用于检测是否登陆
    'cookie': 'douyin.com; ttwid=1%7C6TyurTiOZ9ArhVMdRPp72_00DvwDxo8IiI-w8mhaCXQ%7C1659840618%7C1332b7a941a3e4323f0ee6d2d2ed4021db2cea0a7d0e8c5aab9f905fc552d1ca; s_v_web_id=verify_l6iq90r6_xg0L92HI_tCHn_4npy_B0bC_Ot9GMntECkCI; passport_csrf_token=ac2e8b324ab69605caacc8af697bf24c; passport_csrf_token_default=ac2e8b324ab69605caacc8af697bf24c; n_mh=MPHRKGEs6Mdv8j9-lYQ_xItbJLeVCy02zT61y_-m6jI; sso_uid_tt=f51c3a425d052238e550a828e9c0f537; sso_uid_tt_ss=f51c3a425d052238e550a828e9c0f537; toutiao_sso_user=aa6309907d9f46a14b77eafe40c24b67; toutiao_sso_user_ss=aa6309907d9f46a14b77eafe40c24b67; sid_ucp_sso_v1=1.0.0-KDA5NzA1MTFhMDAwYTVjNTE4MmY0NDI1MmQ5NzZhNjMzZjNmMmUxMGYKHgjI-YDN2PQHELu_nJgGGO8xIAwwybbi-gU4BkD0BxoCaGwiIGFhNjMwOTkwN2Q5ZjQ2YTE0Yjc3ZWFmZTQwYzI0YjY3; ssid_ucp_sso_v1=1.0.0-KDA5NzA1MTFhMDAwYTVjNTE4MmY0NDI1MmQ5NzZhNjMzZjNmMmUxMGYKHgjI-YDN2PQHELu_nJgGGO8xIAwwybbi-gU4BkD0BxoCaGwiIGFhNjMwOTkwN2Q5ZjQ2YTE0Yjc3ZWFmZTQwYzI0YjY3; odin_tt=d8ecbe34606e268af2bb58b0f343bb9fc753d8f25a3d6f1829834eca531b21b75c9d03ca23a7d5825bf74e35ac2fd7527f684aea1bfe081c7cc0aee078517c24; sid_guard=aa6309907d9f46a14b77eafe40c24b67%7C1661411261%7C5184000%7CMon%2C+24-Oct-2022+07%3A07%3A41+GMT; uid_tt=f51c3a425d052238e550a828e9c0f537; uid_tt_ss=f51c3a425d052238e550a828e9c0f537; sid_tt=aa6309907d9f46a14b77eafe40c24b67; sessionid=aa6309907d9f46a14b77eafe40c24b67; sessionid_ss=aa6309907d9f46a14b77eafe40c24b67; sid_ucp_v1=1.0.0-KGFlZTRlOGRkOWM0MjUxZGY3NWMyNDY3Mjk3N2QxNTM0ZjlmM2MwZmIKHgjI-YDN2PQHEL2_nJgGGO8xIAwwybbi-gU4BkD0BxoCaGwiIGFhNjMwOTkwN2Q5ZjQ2YTE0Yjc3ZWFmZTQwYzI0YjY3; ssid_ucp_v1=1.0.0-KGFlZTRlOGRkOWM0MjUxZGY3NWMyNDY3Mjk3N2QxNTM0ZjlmM2MwZmIKHgjI-YDN2PQHEL2_nJgGGO8xIAwwybbi-gU4BkD0BxoCaGwiIGFhNjMwOTkwN2Q5ZjQ2YTE0Yjc3ZWFmZTQwYzI0YjY3; download_guide=%223%2F20220914%22; live_can_add_dy_2_desktop=%220%22; strategyABtestKey=1663655909.538; SEARCH_RESULT_LIST_TYPE=%22single%22; douyin.com; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAABOhvAjIm3vns-R1X1jh5dt-kQ5s_ihMeO9UG_JpkDRw%2F1663689600000%2F0%2F0%2F1663657444543%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAABOhvAjIm3vns-R1X1jh5dt-kQ5s_ihMeO9UG_JpkDRw%2F1663689600000%2F0%2F1663656844544%2F0%22; FRIEND_NUMBER_RED_POINT_INFO=%22MS4wLjABAAAABOhvAjIm3vns-R1X1jh5dt-kQ5s_ihMeO9UG_JpkDRw%2F1663689600000%2F1663656953443%2F0%2F0%22; csrf_session_id=46bfbd21ede7be15abfa08d4032eddf2; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1664261931745%2C%22type%22%3A0%7D; tt_scid=5YmVqzyQCq9kBa89xQ6CUXS0jUTftTFYy8l7unxRuS0.jYg7LH62vP4JHM0Wj3rdbee0; __ac_nonce=0632969b80016ee221534; __ac_signature=_02B4Z6wo00f01Wg3PHwAAIDB6DXGPBkI1iloFzjAADkobC4WDViooOamLMlazYqsnVm2lEDD38rlD63AWI8CGuJkPR38ZFb9kcY.l-wBv86Epa62K.IbylonCQBwzRlrAwC9bqaH5rrA8UTZ76; home_can_add_dy_2_desktop=%221%22; msToken=rnNfaCW0IavMRcg28spsyXhAz763PL-cgs-V-JgkATv1tWPdWal0AjTg1Rz7nhYzxu3V2aZQBXcOCoouyMZFp32spDYY8Hn4su0Hu6Vc_-Eng8Lh3WqmCHOwbGlF-wY=; msToken=FWcj23pq3NEEhkZjlW4WyOJe0vP6qpvKsbLr5_nylKinsLBUFSaqatc5DSHDtXWgu7W69z_XTyM0VrBiv6CJ009AX6usYjAoH-w86KmhhiF4r1pt0bol_5T67u8hEc4=',
    'User-Agent': 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
# 发送请求
response = requests.get(url=url, headers=headers)

# <Response [200]> 响应对象 表示请求成功  200 状态码
# 2. 获取网页源代码
"""
3. 解析数据, 提取我们想要视频标题以及视频播放url地址
    正则表达式 ---> re.findall()

    从什么地方<字符串> 去找什么数据<正则命令匹配数据>

正则表达式提取出来的数据, 返回列表数据类型 [0] 根据列表索引位置, 提取内容 0 索引位置是0 也就是第一个元素
保存数据, 文件名, 字符串数据类型
() 表示精确匹配 你想要数据
. 表示可以匹配任意字符 <除了\n换行符>
* 表示可以匹配前一个字符0个或者无数个
? 非贪婪匹配模式
.*? 可以匹配任意字符 <除了\n换行符>  我要匹配换行符怎么办? 加re.S

"""
# 提取标题
# title = re.findall('<title data-rh="true">(.*?)</title>', response.text, re.S)[0]
#
# # # 替换特殊字符
# title = re.sub(r'[\/.*":?<>|\n]', '', title)
# print(title)
# 视频
html_data = re.findall('<script id="RENDER_DATA" type="application/json">(.*?)</script>', response.text)[0]
# 解码 requests.utils.unquote  编码 requests.utils.quote
html_data = requests.utils.unquote(html_data)
# 把完整json字符数据格式转换字典数据类型
json_data = json.loads(html_data)
pprint.pprint(json_data)
# # 字典取值 键值对取值 ---> 根据冒号左边的内容[键], 提取冒号右边的内容[值]
# video_url = 'https:' + json_data['74931a6b75e09238f154ab1577c994c9']['aweme']['detail']['video']['bitRateList'][0]['playAddr'][0]['src']
# print(video_url)
# # 保存数据
# video_content = requests.get(url=video_url, headers=headers).content  # 对于视频播放链接发送请求获取二进制数据内容
# # video\\ 文件夹 title 文件名 .mp4文件后缀 wb二进制保存 as 重命名为 f
# with open('video\\' + title + '.mp4', mode='wb') as f:
#     # 写入数据
#     f.write(video_content)
# print(title)