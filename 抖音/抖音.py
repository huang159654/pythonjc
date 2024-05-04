import parsel
import requests
import csv
from requests import session
f = open('抖音.csv', mode='a', encoding='utf_8_sig', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    '账号名称',
    '点赞',
    '评论',
    '视频链接',
    '发布时间'
])
csv_writer.writeheader()
# offset=input('请输入翻页数字:')#0,16,26,36
for offset in range(0,240,10):
    headers = {
        'authority': 'www.douyin.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'ttwid=1%7CoUtUgD7EvPpj6Qu64gb758lvWI_SmQLFtcu0mjIFO1M%7C1688678932%7C7f5f10e398cbb0340b1e9834f0aef4ba0f63ac03ee039aec34484e0d651ac8dd; passport_csrf_token=cff25ffbec0ff203079ceadea84da40c; passport_csrf_token_default=cff25ffbec0ff203079ceadea84da40c; __bd_ticket_guard_local_probe=1688678929890; s_v_web_id=verify_ljrnu53k_dwqhfzw3_fhmi_4A5q_BjRV_Usw08f5Z22iy; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtY2xpZW50LWNzciI6Ii0tLS0tQkVHSU4gQ0VSVElGSUNBVEUgUkVRVUVTVC0tLS0tXHJcbk1JSUJEekNCdFFJQkFEQW5NUXN3Q1FZRFZRUUdFd0pEVGpFWU1CWUdBMVVFQXd3UFltUmZkR2xqYTJWMFgyZDFcclxuWVhKa01Ga3dFd1lIS29aSXpqMENBUVlJS29aSXpqMERBUWNEUWdBRS9WN3luSFdpL3d3S0VEdFFWUVBvYXdFTVxyXG5DZkR2YUpITmdpaTcxblhsVG9CUGMzRnB0RXczVlZ4U1hOVHJFTHFHTDFGOXVrcHBPeEJwTWl3MFU4L1lCNkFzXHJcbk1Db0dDU3FHU0liM0RRRUpEakVkTUJzd0dRWURWUjBSQkJJd0VJSU9kM2QzTG1SdmRYbHBiaTVqYjIwd0NnWUlcclxuS29aSXpqMEVBd0lEU1FBd1JnSWhBTmZDT0NzQlF1YmRvU1pLWDdibmFoMHBualkrdkp3MFdCcUo1S0VJSy83ZVxyXG5BaUVBOEM2L0RLOXFlVW1Fd045VU9pcFY4U08rMUt6TFFaSUtEZm42VThGV0RlND1cclxuLS0tLS1FTkQgQ0VSVElGSUNBVEUgUkVRVUVTVC0tLS0tXHJcbiJ9; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; ttcid=efdedc6380d94d7b9e70f28cc4adabb423; download_guide=%223%2F20230707%2F0%22; pwa2=%222%7C0%7C0%7C0%22; douyin.com; device_web_cpu_core=8; device_web_memory_size=8; webcast_local_quality=null; strategyABtestKey=%221688955548.411%22; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1689560349121%2C%22type%22%3Anull%7D; xgplayer_user_id=315442593126; csrf_session_id=265c6db6b7a091e57a87c96606c5bcab; __ac_nonce=064ab6ac80056373a883c; __ac_signature=_02B4Z6wo00f01VQ999QAAIDB1D8NlMl9kMFUHfNAADGnzZoRJBQtJ32q801hJVV4XNZBIGqVOOv8ioCW4wT.KUBxvipuI9Q8rvNpQEml.IYyLkLmG9cpchALAKri96NO92-kCwazej0Gr.zg8a; SEARCH_RESULT_LIST_TYPE=%22single%22; msToken=LaMoix-eUyl73IhM_5PnucmfvUTqDnU9eussPC_vSVqcfcpj1f1Z_NYqLXv-GaoPSO6HjfelNX4AvHB2UvMaoPaBixEiwx-aEdsHL75HFQATTLPyHkyQqAv8DD57B3U=; msToken=HMnhHN-vPvi4jOkK7sDDYcZosheO8j7R2WW5FiKiPmL95RjsyPUVYqohGWtn5YpKtC-M5yVHTTSyG7KIy6ddZ7STT8l72BxiDZTT6gMhCM6cLxQmUsylRW4bkt1A6w4=; home_can_add_dy_2_desktop=%221%22; tt_scid=GdzPi6fctD6KoWBXYXljEQltcnjfW-gp.hneTxVHPTmXyYOCqrDgrXdrPlguNpK7961c',
        'referer': 'https://www.douyin.com/search/%E7%B1%B3%E8%AF%BA%E5%9C%B0%E5%B0%94%E9%85%8A?publish_time=182&sort_type=0&source=tab_search&type=video',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }
    # url=f'https://www.douyin.com/aweme/v1/web/search/item/?device_platform=webapp&aid=6383&channel=channel_pc_web&search_channel=aweme_video_web&sort_type=0&publish_time=182&keyword=%E7%B1%B3%E8%AF%BA%E5%9C%B0%E5%B0%94%E9%85%8D&search_source=tab_search&query_correct_type=1&is_filter_search=1&from_group_id=&offset={offset}&count=10&search_id=20230621213855CB9BD9307EE4BE25F3C5&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1280&screen_height=720&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=114.0.0.0&browser_online=true&engine_name=Blink&engine_version=114.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=8.35&effective_type=4g&round_trip_time=0&webid=7241982921493186086&msToken=4CgssKQQ9Ta6pP7wvr6mLf2wptIVgxr08StrSu_PntomSIb7hVEoVErBH8P5IG08yyP7v_JqS3awZKM7yWqtkeh7yfyO_ifzwsnSN2qTmu3nZCxeR7xBmIFS-ELpdWw=&X-Bogus=DFSzswVuAPkANH1btnRcMF9WX7nl',

    response = requests.get(f'https://www.douyin.com/aweme/v1/web/search/item/?device_platform=webapp&aid=6383&channel=channel_pc_web&search_channel=aweme_video_web&sort_type=0&publish_time=182&keyword=%E7%B1%B3%E8%AF%BA%E5%9C%B0%E5%B0%94%E9%85%8D&search_source=tab_search&query_correct_type=1&is_filter_search=1&from_group_id=&offset={offset}&count=10&search_id=20230621213855CB9BD9307EE4BE25F3C5&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1280&screen_height=720&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=114.0.0.0&browser_online=true&engine_name=Blink&engine_version=114.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=8.35&effective_type=4g&round_trip_time=0&webid=7241982921493186086&msToken=4CgssKQQ9Ta6pP7wvr6mLf2wptIVgxr08StrSu_PntomSIb7hVEoVErBH8P5IG08yyP7v_JqS3awZKM7yWqtkeh7yfyO_ifzwsnSN2qTmu3nZCxeR7xBmIFS-ELpdWw=&X-Bogus=DFSzswVuAPkANH1btnRcMF9WX7nl',
    headers=headers,
    ).json()
    data_json=response['data']
    for da in data_json:
        try:
            url_id=da['aweme_info']['aweme_id']
            # print(url_id)
            nickname = da['aweme_info']['author']['nickname']#账号名称
            # print(nickname)
            video_url = 'https://www.douyin.com/video/' + url_id#视频链接
            # print(video_url)
            iur_data=requests.get(url=video_url,headers=headers).text
            # print(iur_data)
            html_data_1=parsel.Selector(iur_data)
            Like=html_data_1.xpath('.//*[@id="douyin-right-container"]/div[3]/div/div[1]/div[3]/div/div[2]/div[1]/div[1]/span/text()').get()#点赞
            comments=html_data_1.xpath('.//*[@id="douyin-right-container"]/div[3]/div/div[1]/div[3]/div/div[2]/div[1]/div[2]/span/text()').get()#评论
            time_da = html_data_1.xpath(
                './/*[@id="douyin-right-container"]/div[3]/div/div[1]/div[3]/div/div[2]/div[2]/span/text()[2]').get()  # 发布时间
            print(Like,comments,time_da,video_url)
            # html_data = re.findall('<title data-rh="true">(.*?)</title>',iur_data)[0]
            # html_data = requests.utils.unquote(html_data)
            # json_data = json.loads(html_data)
            dit = {
                '账号名称':nickname,
                '点赞':Like,
                '评论':comments,
                '视频链接':video_url,
                '发布时间':time_da,
            }
            csv_writer.writerow(dit)
            print('下载完毕！',nickname,Like,comments,time_da,video_url)
        except Exception as e:
            e





