from pprint import pprint
from urllib import parse

import requests
keyword=input('请输入你要搜索的视频名字:')
da=parse.quote(keyword)

url = f'https://www.douyin.com/aweme/v1/web/general/search/single/?device_platform=webapp&aid=6383&channel=channel_pc_web&search_channel=aweme_general&sort_type=0&publish_time=0&keyword={da}&search_source=normal_search&query_correct_type=1&is_filter_search=0&from_group_id=&offset=0&count=15&pc_client_type=1&version_code=190600&version_name=19.6.0&cookie_enabled=true&screen_width=1280&screen_height=720&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=113.0.0.0&browser_online=true&engine_name=Blink&engine_version=113.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=0&webid=7229858075049084420&msToken=QhI9QdepP85qmsZi0T56NL9GslDT7wzaxvwVEwkdJ7Wg9EEEopaCIcDbBsQ-QbaAD4R2XfJHYycwh4dvhOyWxhcn3_fvTI9ua88Em6ZJ2WVUw7a-HpoH_A==&X-Bogus=DFSzswVusl0ANeZztSAXNe9WX7rj',
sa=url[0]
print(sa)
referer=f'https://www.douyin.com/search/{da}?aid=9d657a95-f03a-40dc-9b9b-6ce292ee1965&publish_time=0&sort_type=0&source=normal_search&type=general'
headers = {
    'authority': 'www.douyin.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    #'cookie': 'passport_csrf_token=fb76764f2ca0bd15388b18696beb79db; passport_csrf_token_default=fb76764f2ca0bd15388b18696beb79db; s_v_web_id=verify_lhb8qed6_XPV4UjRe_e4y2_4Xn4_9ZTi_VZ2h5zzWGObv; store-region-src=uid; store-region=cn-fj; my_rd=1; ttwid=1%7CD5j1F0r9DNCs-j9bF3WTfyyMo6p_uQAX1M0dfSzCtyk%7C1684674109%7C89814cf60c3c0073fc4aca373f0f569d05b50d8c1e55145a32b8fecaa106e19a; passport_assist_user=Cj-6jrlFxNZL5D9iv4d9dpxNU3FG7k_7lHW2jis7dBT4HoxpWFwjhef1MZr2Vxv1ZjYIwTT2rKZo_8H62YOchdAaSAo8e8765ORxOQZ-Fo0qTtmQVFGKaxqsEFAlIeU6ikO4O1BwAL9OCdxDoufp4Q-a9ALKPkPUmBCRm8q8yQ32EJXcsQ0Yia_WVCIBA2LDvps%3D; n_mh=MPHRKGEs6Mdv8j9-lYQ_xItbJLeVCy02zT61y_-m6jI; sso_uid_tt=938efb297bac1a4dc7592bf409709cf5; sso_uid_tt_ss=938efb297bac1a4dc7592bf409709cf5; toutiao_sso_user=5952a8dc54a41a9b85b6bdaa9d35fac9; toutiao_sso_user_ss=5952a8dc54a41a9b85b6bdaa9d35fac9; sid_ucp_sso_v1=1.0.0-KDA4NDgxNzJiYWFjZTgzNWJjOWM2M2EyMTYwNTRiYWRmOTA1NDhhYmYKHgjI-YDN2PQHEMWvqKMGGO8xIAwwybbi-gU4BkD0BxoCbHEiIDU5NTJhOGRjNTRhNDFhOWI4NWI2YmRhYTlkMzVmYWM5; ssid_ucp_sso_v1=1.0.0-KDA4NDgxNzJiYWFjZTgzNWJjOWM2M2EyMTYwNTRiYWRmOTA1NDhhYmYKHgjI-YDN2PQHEMWvqKMGGO8xIAwwybbi-gU4BkD0BxoCbHEiIDU5NTJhOGRjNTRhNDFhOWI4NWI2YmRhYTlkMzVmYWM5; odin_tt=ff9ca68f1437504cbd9519ce7c9c9727919184399ac97fe37bda7d71a1174b2064b5abde52fbed46fbd00669e7d6c51f509ed3b66d8bcf1b6932b289afa219fa; passport_auth_status=0ba058bcf412c1d4fab7609632bdaa03%2C147596b4c6b7be6743d50d61ea23c147; passport_auth_status_ss=0ba058bcf412c1d4fab7609632bdaa03%2C147596b4c6b7be6743d50d61ea23c147; uid_tt=5ddf39f3f539d39b0db0ce1f26afebef; uid_tt_ss=5ddf39f3f539d39b0db0ce1f26afebef; sid_tt=e75cef9bfc2823b330192fa172d97185; sessionid=e75cef9bfc2823b330192fa172d97185; sessionid_ss=e75cef9bfc2823b330192fa172d97185; LOGIN_STATUS=1; sid_guard=e75cef9bfc2823b330192fa172d97185%7C1684674506%7C5183998%7CThu%2C+20-Jul-2023+13%3A08%3A24+GMT; sid_ucp_v1=1.0.0-KDQ3NGUyZTExMWZhOThjMTBjNWRhZWYwMmMwNTUxOTZhYzVjMjAwMzkKGgjI-YDN2PQHEMqvqKMGGO8xIAw4BkD0B0gEGgJobCIgZTc1Y2VmOWJmYzI4MjNiMzMwMTkyZmExNzJkOTcxODU; ssid_ucp_v1=1.0.0-KDQ3NGUyZTExMWZhOThjMTBjNWRhZWYwMmMwNTUxOTZhYzVjMjAwMzkKGgjI-YDN2PQHEMqvqKMGGO8xIAw4BkD0B0gEGgJobCIgZTc1Y2VmOWJmYzI4MjNiMzMwMTkyZmExNzJkOTcxODU; SEARCH_RESULT_LIST_TYPE=%22single%22; download_guide=%223%2F20230521%22; pwa2=%223%7C1%22; FRIEND_NUMBER_RED_POINT_INFO=%22MS4wLjABAAAABOhvAjIm3vns-R1X1jh5dt-kQ5s_ihMeO9UG_JpkDRw%2F1685030400000%2F1684953696633%2F0%2F0%22; __live_version__=%221.1.0.9614%22; live_can_add_dy_2_desktop=%220%22; douyin.com; csrf_session_id=9e3c856f2b36b32dc782af8877b50d03; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtY2xpZW50LWNlcnQiOiItLS0tLUJFR0lOIENFUlRJRklDQVRFLS0tLS1cbk1JSUNGRENDQWJ1Z0F3SUJBZ0lWQUxCb1g4V3pjalpOSm5lQ3N4ZGNaZ3pRcC94L01Bb0dDQ3FHU000OUJBTUNcbk1ERXhDekFKQmdOVkJBWVRBa05PTVNJd0lBWURWUVFEREJsMGFXTnJaWFJmWjNWaGNtUmZZMkZmWldOa2MyRmZcbk1qVTJNQjRYRFRJek1EVXdOakF3TWpJME5Wb1hEVE16TURVd05qQTRNakkwTlZvd0p6RUxNQWtHQTFVRUJoTUNcblEwNHhHREFXQmdOVkJBTU1EMkprWDNScFkydGxkRjluZFdGeVpEQlpNQk1HQnlxR1NNNDlBZ0VHQ0NxR1NNNDlcbkF3RUhBMElBQkNSMEovRHlSMUVLTWw2VnErZzhzS3FoZ1Q2ZVZURDhaalpWZkNPMUhDcFArb0o2bWd6Nng4TmFcbkh2ZGhlMTk5WlJ1VGp1M1h4bWVRK21iN203cFVQZitqZ2Jrd2diWXdEZ1lEVlIwUEFRSC9CQVFEQWdXZ01ERUdcbkExVWRKUVFxTUNnR0NDc0dBUVVGQndNQkJnZ3JCZ0VGQlFjREFnWUlLd1lCQlFVSEF3TUdDQ3NHQVFVRkJ3TUVcbk1Da0dBMVVkRGdRaUJDQnlXUEoxNHdHNzErajBIeXQwUllUUzV3eUVXS0I5N0pIQWFLRHRYM05adERBckJnTlZcbkhTTUVKREFpZ0NBeXBXZnFqbVJJRW8zTVRrMUFlM01VbTBkdFUzcWswWURYZVpTWGV5SkhnekFaQmdOVkhSRUVcbkVqQVFnZzUzZDNjdVpHOTFlV2x1TG1OdmJUQUtCZ2dxaGtqT1BRUURBZ05IQURCRUFpQmo4YTVFZ09ya0hyeURcbmhoakJ4cVpoTUtFTEFhUmhMZUloUVVuSnFjQVNZUUlnV1lqUUlpM1hNalFNVms3U09XQ3RiWE50TnY2Y2VqTmhcbnFKK050RU1xaUdnPVxuLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLVxuIn0=; strategyABtestKey=%221685273761.937%22; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1685878561952%2C%22type%22%3A1%7D; _tea_utm_cache_2018=undefined; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAABOhvAjIm3vns-R1X1jh5dt-kQ5s_ihMeO9UG_JpkDRw%2F1685289600000%2F0%2F0%2F1685280055210%22; __ac_nonce=0647351d50095e8db5d74; __ac_signature=_02B4Z6wo00f01xZvTBwAAIDDlm22Xc70b7cWT0iAAKHyRRoS14cfz277dPGxg6kpSiQQ4mji-0KaaQ6-DL5PuGZllT8Z4dEl9MAYcMNg92hg3usofUz1IpSmEyoHQ-g8mtzIMM42Ftzp4uykcb; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAABOhvAjIm3vns-R1X1jh5dt-kQ5s_ihMeO9UG_JpkDRw%2F1685289600000%2F0%2F1685279190857%2F0%22; home_can_add_dy_2_desktop=%221%22; passport_fe_beating_status=true; tt_scid=0tCVx4ndwGyO0N7Eq.xIhaS-v5rhqkRHtZJ.pbFveaoO3Sd.Lmc-S1h4wa1vyecJd8b0; msToken=TNsM5SvKqnc5UcAwpKgxJxDbrx1UYYdm4rpu-j-oYqfpc8cmbPgDpGIaBJ9Dyxk66FWw9J_VUyaUCLCEfmrD_V9n_MC_fljzlqPA1U4Uz9ipr5zSPNTcoQ==; msToken=jgPZ8MNt779AznkNaGrq8h7QZM8ajF8whRgtzBSHvyUs6DPyXeu5Ep_1Xq23XD7E98s7Tuwz6RPq8X3eXZuH7vvSOaXEwOxFHWyrV2_sAymfi1N9H0_BEg==',
    'pragma': 'no-cache',
    'referer':referer ,
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
}

response = requests.get(url=sa,headers=headers,).json()
print(response)
data_json=response['data']
digg_count_json =response['aweme_info']['statistics']['comment_count']
# print(digg_count_json)
data_json =response['data'][0]['aweme_info']['aweme_id']
# print(data_json)
for i in data_json:
    digg_count_json=i['aweme_info']['statistics']['comment_count']#评论
    url_id = i['aweme_info']['aweme_id']
    id_url='https://www.douyin.com/video/'+url_id
    print(id_url,digg_count_json)
