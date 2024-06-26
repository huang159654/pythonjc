import json
import re

import requests
import parsel
headers = {
    'authority': 'www.douyin.com',
    'cookie': 'douyin.com; passport_csrf_token=fb76764f2ca0bd15388b18696beb79db; passport_csrf_token_default=fb76764f2ca0bd15388b18696beb79db; s_v_web_id=verify_lhb8qed6_XPV4UjRe_e4y2_4Xn4_9ZTi_VZ2h5zzWGObv; store-region-src=uid; store-region=cn-fj; my_rd=1; ttwid=1%7CD5j1F0r9DNCs-j9bF3WTfyyMo6p_uQAX1M0dfSzCtyk%7C1684674109%7C89814cf60c3c0073fc4aca373f0f569d05b50d8c1e55145a32b8fecaa106e19a; publish_badge_show_info=%220%2C0%2C0%2C1684674478870%22; passport_assist_user=Cj-6jrlFxNZL5D9iv4d9dpxNU3FG7k_7lHW2jis7dBT4HoxpWFwjhef1MZr2Vxv1ZjYIwTT2rKZo_8H62YOchdAaSAo8e8765ORxOQZ-Fo0qTtmQVFGKaxqsEFAlIeU6ikO4O1BwAL9OCdxDoufp4Q-a9ALKPkPUmBCRm8q8yQ32EJXcsQ0Yia_WVCIBA2LDvps%3D; n_mh=MPHRKGEs6Mdv8j9-lYQ_xItbJLeVCy02zT61y_-m6jI; sso_uid_tt=938efb297bac1a4dc7592bf409709cf5; sso_uid_tt_ss=938efb297bac1a4dc7592bf409709cf5; toutiao_sso_user=5952a8dc54a41a9b85b6bdaa9d35fac9; toutiao_sso_user_ss=5952a8dc54a41a9b85b6bdaa9d35fac9; sid_ucp_sso_v1=1.0.0-KDA4NDgxNzJiYWFjZTgzNWJjOWM2M2EyMTYwNTRiYWRmOTA1NDhhYmYKHgjI-YDN2PQHEMWvqKMGGO8xIAwwybbi-gU4BkD0BxoCbHEiIDU5NTJhOGRjNTRhNDFhOWI4NWI2YmRhYTlkMzVmYWM5; ssid_ucp_sso_v1=1.0.0-KDA4NDgxNzJiYWFjZTgzNWJjOWM2M2EyMTYwNTRiYWRmOTA1NDhhYmYKHgjI-YDN2PQHEMWvqKMGGO8xIAwwybbi-gU4BkD0BxoCbHEiIDU5NTJhOGRjNTRhNDFhOWI4NWI2YmRhYTlkMzVmYWM5; odin_tt=ff9ca68f1437504cbd9519ce7c9c9727919184399ac97fe37bda7d71a1174b2064b5abde52fbed46fbd00669e7d6c51f509ed3b66d8bcf1b6932b289afa219fa; passport_auth_status=0ba058bcf412c1d4fab7609632bdaa03%2C147596b4c6b7be6743d50d61ea23c147; passport_auth_status_ss=0ba058bcf412c1d4fab7609632bdaa03%2C147596b4c6b7be6743d50d61ea23c147; uid_tt=5ddf39f3f539d39b0db0ce1f26afebef; uid_tt_ss=5ddf39f3f539d39b0db0ce1f26afebef; sid_tt=e75cef9bfc2823b330192fa172d97185; sessionid=e75cef9bfc2823b330192fa172d97185; sessionid_ss=e75cef9bfc2823b330192fa172d97185; LOGIN_STATUS=1; sid_guard=e75cef9bfc2823b330192fa172d97185%7C1684674506%7C5183998%7CThu%2C+20-Jul-2023+13%3A08%3A24+GMT; sid_ucp_v1=1.0.0-KDQ3NGUyZTExMWZhOThjMTBjNWRhZWYwMmMwNTUxOTZhYzVjMjAwMzkKGgjI-YDN2PQHEMqvqKMGGO8xIAw4BkD0B0gEGgJobCIgZTc1Y2VmOWJmYzI4MjNiMzMwMTkyZmExNzJkOTcxODU; ssid_ucp_v1=1.0.0-KDQ3NGUyZTExMWZhOThjMTBjNWRhZWYwMmMwNTUxOTZhYzVjMjAwMzkKGgjI-YDN2PQHEMqvqKMGGO8xIAw4BkD0B0gEGgJobCIgZTc1Y2VmOWJmYzI4MjNiMzMwMTkyZmExNzJkOTcxODU; SEARCH_RESULT_LIST_TYPE=%22single%22; download_guide=%223%2F20230521%22; pwa2=%223%7C1%22; __live_version__=%221.1.0.9449%22; douyin.com; csrf_session_id=9e3c856f2b36b32dc782af8877b50d03; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtY2xpZW50LWNlcnQiOiItLS0tLUJFR0lOIENFUlRJRklDQVRFLS0tLS1cbk1JSUNGRENDQWJ1Z0F3SUJBZ0lWQUxCb1g4V3pjalpOSm5lQ3N4ZGNaZ3pRcC94L01Bb0dDQ3FHU000OUJBTUNcbk1ERXhDekFKQmdOVkJBWVRBa05PTVNJd0lBWURWUVFEREJsMGFXTnJaWFJmWjNWaGNtUmZZMkZmWldOa2MyRmZcbk1qVTJNQjRYRFRJek1EVXdOakF3TWpJME5Wb1hEVE16TURVd05qQTRNakkwTlZvd0p6RUxNQWtHQTFVRUJoTUNcblEwNHhHREFXQmdOVkJBTU1EMkprWDNScFkydGxkRjluZFdGeVpEQlpNQk1HQnlxR1NNNDlBZ0VHQ0NxR1NNNDlcbkF3RUhBMElBQkNSMEovRHlSMUVLTWw2VnErZzhzS3FoZ1Q2ZVZURDhaalpWZkNPMUhDcFArb0o2bWd6Nng4TmFcbkh2ZGhlMTk5WlJ1VGp1M1h4bWVRK21iN203cFVQZitqZ2Jrd2diWXdEZ1lEVlIwUEFRSC9CQVFEQWdXZ01ERUdcbkExVWRKUVFxTUNnR0NDc0dBUVVGQndNQkJnZ3JCZ0VGQlFjREFnWUlLd1lCQlFVSEF3TUdDQ3NHQVFVRkJ3TUVcbk1Da0dBMVVkRGdRaUJDQnlXUEoxNHdHNzErajBIeXQwUllUUzV3eUVXS0I5N0pIQWFLRHRYM05adERBckJnTlZcbkhTTUVKREFpZ0NBeXBXZnFqbVJJRW8zTVRrMUFlM01VbTBkdFUzcWswWURYZVpTWGV5SkhnekFaQmdOVkhSRUVcbkVqQVFnZzUzZDNjdVpHOTFlV2x1TG1OdmJUQUtCZ2dxaGtqT1BRUURBZ05IQURCRUFpQmo4YTVFZ09ya0hyeURcbmhoakJ4cVpoTUtFTEFhUmhMZUloUVVuSnFjQVNZUUlnV1lqUUlpM1hNalFNVms3U09XQ3RiWE50TnY2Y2VqTmhcbnFKK050RU1xaUdnPVxuLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLVxuIn0=; live_can_add_dy_2_desktop=%221%22; strategyABtestKey=%221684776669.903%22; __ac_nonce=0646c896c001612922522; __ac_signature=_02B4Z6wo00f01DApo9AAAIDAsCtZk5DvTQQwCadAAGhtG9lFfQfuhaUkvrn2QLpv0IPeiaZbEDv7CxVaJo4oWAjd3qPfJerrLe.j2rMvtvzKuzrrav5AEAgYIFMlj8RBrUlO.L3WNd6SEYL.4b; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1685439482531%2C%22type%22%3A1%7D; msToken=cPI5btbunMdAaVzoezr9bQ1CNV-QIXE34Z_ku49y6KjxBZ6WOKyTDu4SW9teSFQgF_oAtrucHikIXqNdTp5IrxlFOrwg6sihaY_8Ftk00rKw0tic1ak5zA==; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAABOhvAjIm3vns-R1X1jh5dt-kQ5s_ihMeO9UG_JpkDRw%2F1684857600000%2F0%2F0%2F1684835970085%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAABOhvAjIm3vns-R1X1jh5dt-kQ5s_ihMeO9UG_JpkDRw%2F1684857600000%2F0%2F0%2F1684836570086%22; home_can_add_dy_2_desktop=%221%22; tt_scid=drS1L8DyH9Frh3.zerRHG5JcWLTIQJJMdl9fGSMYbrHDvx8YlSNhFj9sRqCVJbAW1736; msToken=qOEMGeCNoVPJ7natP4w_PBLnHHKE6N4W4cQZomvwnb2EIVzjHT4d7LVjWpowWaicDb_sP3tHV_6cdJCK5UEQ3rrOMsMwl1FuSbq9V8M6WSAla9fPxVAsDg==; passport_fe_beating_status=false',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}
'https://www.douyin.com/user/MS4wLjABAAAARVIx_ngWRccZKHFW89XnP0VUDA2zwQFSPxEGGtuAmWN6m7KP0ZuqmjQxoNgCYw9D?vid=7250795219963137340'
url='https://www.douyin.com/user/MS4wLjABAAAARxsY9fhtEgejUcMjtq-hQqbzAHhYSK0ShZCpGmhTg1s?vid=7235642801369713979'
response = requests.get(url=url,headers=headers,
).text
div_s=parsel.Selector(response)
div_a=div_s.xpath('.//div[@class="UFuuTZ1P"]/ul/li')
for div_a in div_a:
    sa=div_a.xpath('.//div/a/@href').get()
    saf=sa.split('/')[2]
    url_1 = f'https://www.douyin.com/video/{saf}'
    # 请求头headers
    headers = {
        # 用户信息, 常用于检测是否登陆
        'cookie': 'douyin.com; ttwid=1%7C6TyurTiOZ9ArhVMdRPp72_00DvwDxo8IiI-w8mhaCXQ%7C1659840618%7C1332b7a941a3e4323f0ee6d2d2ed4021db2cea0a7d0e8c5aab9f905fc552d1ca; s_v_web_id=verify_l6iq90r6_xg0L92HI_tCHn_4npy_B0bC_Ot9GMntECkCI; passport_csrf_token=ac2e8b324ab69605caacc8af697bf24c; passport_csrf_token_default=ac2e8b324ab69605caacc8af697bf24c; n_mh=MPHRKGEs6Mdv8j9-lYQ_xItbJLeVCy02zT61y_-m6jI; sso_uid_tt=f51c3a425d052238e550a828e9c0f537; sso_uid_tt_ss=f51c3a425d052238e550a828e9c0f537; toutiao_sso_user=aa6309907d9f46a14b77eafe40c24b67; toutiao_sso_user_ss=aa6309907d9f46a14b77eafe40c24b67; sid_ucp_sso_v1=1.0.0-KDA5NzA1MTFhMDAwYTVjNTE4MmY0NDI1MmQ5NzZhNjMzZjNmMmUxMGYKHgjI-YDN2PQHELu_nJgGGO8xIAwwybbi-gU4BkD0BxoCaGwiIGFhNjMwOTkwN2Q5ZjQ2YTE0Yjc3ZWFmZTQwYzI0YjY3; ssid_ucp_sso_v1=1.0.0-KDA5NzA1MTFhMDAwYTVjNTE4MmY0NDI1MmQ5NzZhNjMzZjNmMmUxMGYKHgjI-YDN2PQHELu_nJgGGO8xIAwwybbi-gU4BkD0BxoCaGwiIGFhNjMwOTkwN2Q5ZjQ2YTE0Yjc3ZWFmZTQwYzI0YjY3; odin_tt=d8ecbe34606e268af2bb58b0f343bb9fc753d8f25a3d6f1829834eca531b21b75c9d03ca23a7d5825bf74e35ac2fd7527f684aea1bfe081c7cc0aee078517c24; sid_guard=aa6309907d9f46a14b77eafe40c24b67%7C1661411261%7C5184000%7CMon%2C+24-Oct-2022+07%3A07%3A41+GMT; uid_tt=f51c3a425d052238e550a828e9c0f537; uid_tt_ss=f51c3a425d052238e550a828e9c0f537; sid_tt=aa6309907d9f46a14b77eafe40c24b67; sessionid=aa6309907d9f46a14b77eafe40c24b67; sessionid_ss=aa6309907d9f46a14b77eafe40c24b67; sid_ucp_v1=1.0.0-KGFlZTRlOGRkOWM0MjUxZGY3NWMyNDY3Mjk3N2QxNTM0ZjlmM2MwZmIKHgjI-YDN2PQHEL2_nJgGGO8xIAwwybbi-gU4BkD0BxoCaGwiIGFhNjMwOTkwN2Q5ZjQ2YTE0Yjc3ZWFmZTQwYzI0YjY3; ssid_ucp_v1=1.0.0-KGFlZTRlOGRkOWM0MjUxZGY3NWMyNDY3Mjk3N2QxNTM0ZjlmM2MwZmIKHgjI-YDN2PQHEL2_nJgGGO8xIAwwybbi-gU4BkD0BxoCaGwiIGFhNjMwOTkwN2Q5ZjQ2YTE0Yjc3ZWFmZTQwYzI0YjY3; download_guide=%223%2F20220914%22; live_can_add_dy_2_desktop=%220%22; strategyABtestKey=1663655909.538; SEARCH_RESULT_LIST_TYPE=%22single%22; douyin.com; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAABOhvAjIm3vns-R1X1jh5dt-kQ5s_ihMeO9UG_JpkDRw%2F1663689600000%2F0%2F0%2F1663657444543%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAABOhvAjIm3vns-R1X1jh5dt-kQ5s_ihMeO9UG_JpkDRw%2F1663689600000%2F0%2F1663656844544%2F0%22; FRIEND_NUMBER_RED_POINT_INFO=%22MS4wLjABAAAABOhvAjIm3vns-R1X1jh5dt-kQ5s_ihMeO9UG_JpkDRw%2F1663689600000%2F1663656953443%2F0%2F0%22; csrf_session_id=46bfbd21ede7be15abfa08d4032eddf2; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1664261931745%2C%22type%22%3A0%7D; tt_scid=5YmVqzyQCq9kBa89xQ6CUXS0jUTftTFYy8l7unxRuS0.jYg7LH62vP4JHM0Wj3rdbee0; __ac_nonce=0632969b80016ee221534; __ac_signature=_02B4Z6wo00f01Wg3PHwAAIDB6DXGPBkI1iloFzjAADkobC4WDViooOamLMlazYqsnVm2lEDD38rlD63AWI8CGuJkPR38ZFb9kcY.l-wBv86Epa62K.IbylonCQBwzRlrAwC9bqaH5rrA8UTZ76; home_can_add_dy_2_desktop=%221%22; msToken=rnNfaCW0IavMRcg28spsyXhAz763PL-cgs-V-JgkATv1tWPdWal0AjTg1Rz7nhYzxu3V2aZQBXcOCoouyMZFp32spDYY8Hn4su0Hu6Vc_-Eng8Lh3WqmCHOwbGlF-wY=; msToken=FWcj23pq3NEEhkZjlW4WyOJe0vP6qpvKsbLr5_nylKinsLBUFSaqatc5DSHDtXWgu7W69z_XTyM0VrBiv6CJ009AX6usYjAoH-w86KmhhiF4r1pt0bol_5T67u8hEc4=',
        'User-Agent': 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    # 发送请求
    response = requests.get(url=url_1, headers=headers)

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
    title = re.findall('<title data-rh="true">(.*?)</title>', response.text, re.S)[0]
    # print(title)
    # # 替换特殊字符
    title = re.sub(r'[\/.*":?<>|\n]', '', title)
    # print(title)
    # 视频
    html_data = re.findall('<script id="RENDER_DATA" type="application/json">(.*?)</script>', response.text)[0]
    # 解码 requests.utils.unquote  编码 requests.utils.quote
    html_data = requests.utils.unquote(html_data)
    # 把完整json字符数据格式转换字典数据类型
    json_data = json.loads(html_data)
    # print(json_data)
    # 字典取值 键值对取值 ---> 根据冒号左边的内容[键], 提取冒号右边的内容[值]
    video_url = 'https:' + json_data['74931a6b75e09238f154ab1577c994c9']['aweme']['detail']['video']['bitRateList'][0]['playAddr'][0]['src']
    # print(video_url)
    # # 保存数据
    video_content = requests.get(url=video_url, headers=headers).content  # 对于视频播放链接发送请求获取二进制数据内容
    # video\\ 文件夹 title 文件名 .mp4文件后缀 wb二进制保存 as 重命名为 f
    with open('video\\' + title + '.mp4', mode='wb') as f:
        # 写入数据
        f.write(video_content)
    print(title,saf)
