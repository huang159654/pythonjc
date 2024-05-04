import json
import random
import re
import time
import pandas
import openpyxl
import redis
import requests
from lxml import etree


class UserID:
    def __init__(self):
        self.dataframe = pandas.read_excel('采集.xlsx', sheet_name='查值', engine='openpyxl')
        self.cookies = {'SINAGLOBAL': '9323548330764.504.1682497166529',
                        'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9W5AechS-POTiZnX9M6lSIBB5JpX5KMhUgL.Fo-4Shef1Kzpeo52dJLoIE-LxK-L1-eL1-qLxKnLBo2L1hq_i--fiKnRi-z7i--fi-88i-zc',
                        'UOR': ',,www.baidu.com',
                        'ULV': '1684769262077:10:8:1:7078796198245.088.1684769262008:1684542416668',
                        'XSRF-TOKEN': 'ovxNWe2-HEwvoUqdnMaJrmxL',
                        'ALF': '1688543517',
                        'SSOLoginState': '1685951517',
                        'SCF': 'AhsKKFN1w2Qt4-IcDNZqB_pwOujOGkEp_3YVfiOkMoeAgQLAihF27GqMCpBLM8Ofl8Rr5vP0ElP5Rp2SZPxCzbA.',
                        'SUB': '_2A25JeeRNDeRhGeNH71EU-SzNyTyIHXVqD1KFrDV8PUNbmtANLUrHkW9NSqZOFTgw2Xy3NklYnIEw4LCmIzARiCwd',
                        'WBPSESS': 'gHzPH5ZTL1_nT5tkC2WP5TyuDUAq1M8luzAUkaSvaTP7Lx-9IbSgHdF1CzWwPbyInCpqDqbfndfNBGqmZNaituvgYZMHRN4BhHw1glVtK0x1rGLDyn3kRRS38LA7PnTR4IbpujVEHO1yHK3OB7bO-w==',

                        }
        self.headers = {
            'authority': 'weibo.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'client-version': 'v2.40.55',
            # 'cookie': 'SINAGLOBAL=9323548330764.504.1682497166529; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5AechS-POTiZnX9M6lSIBB5JpX5KMhUgL.Fo-4Shef1Kzpeo52dJLoIE-LxK-L1-eL1-qLxKnLBo2L1hq_i--fiKnRi-z7i--fi-88i-zc; UOR=,,www.baidu.com; ULV=1684769262077:10:8:1:7078796198245.088.1684769262008:1684542416668; XSRF-TOKEN=toRoU63lq4KuPm2gpaDkh4-R; ALF=1687631229; SSOLoginState=1685039229; SCF=AhsKKFN1w2Qt4-IcDNZqB_pwOujOGkEp_3YVfiOkMoeABOPGJ7At_EJcyKA787lnHmvO9flpHZX-mkqCfDQKopw.; SUB=_2A25Ja9gtDeRhGeNH71EU-SzNyTyIHXVqAU7lrDV8PUNbmtANLRX-kW9NSqZOFTjiHhziGI3OyhknIHEo2v1q8hV8; WBPSESS=gHzPH5ZTL1_nT5tkC2WP5TyuDUAq1M8luzAUkaSvaTP7Lx-9IbSgHdF1CzWwPbyInCpqDqbfndfNBGqmZNaitgUXcCdr-sSDY0Vv1-ofx9_yentEGtB5Q-84bYyfqSBhpyscxIDkt26Km2ixPsB7hQ==',
            'referer': 'https://weibo.com/u/2427203772',
            'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'server-version': 'v2023.05.23.3',
            'traceparent': '00-601d65102f673a11f8de6f3c4304762e-43b9f47f1140402d-00',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58',
            'x-requested-with': 'XMLHttpRequest',
            'x-xsrf-token': 'toRoU63lq4KuPm2gpaDkh4-R', }

    def ID_to_redis(self):
        redis_pool = redis.ConnectionPool(host='127.0.0.1', port=6379, max_connections=20, db=5)
        redis_store = redis.Redis(connection_pool=redis_pool)
        dict_data = self.dataframe.to_dict()
        for name, uid in zip(dict_data['name'].values(), dict_data['uid'].values()):
            redis_store.set(str(uid), str(name))
            print(name, uid)
        print('数据保存至redis......OK')

    def get_UID(self):
        redis_read = redis.Redis(host='127.0.0.1', port=6379, db=5)
        keys = redis_read.keys()
        for key in keys:
            self.get_artcile(UID=key.decode())
            # print(key.decode())

    def get_artcile(self, UID=None):
        info = {'uid': UID}
        print(info)
        detail_list = []
        redis_read = redis.Redis(host='127.0.0.1', port=6379, db=5)
        since_id = ''
        i = 0
        for i in range(3):
            i += 1
            if i == 1:
                params = {
                    'uid': f'{UID}',
                    'page': f'{i}',
                    'feature': '0',
                }
            else:
                params = {
                    'uid': f'{UID}',
                    'page': f'{i}',
                    'feature': '0',
                    'since_id': f'{since_id}'
                }
            print(params)
            response = requests.get('https://weibo.com/ajax/statuses/mymblog', params=params, cookies=self.cookies,
                                    headers=self.headers).json()
            print(response)
            since_id = response['data']['since_id']
            for data in response['data']['list']:
                detail = {}
                try:
                    if data['pic_ids']:
                        detail['pic_ids'] = data['pic_ids']
                    else:
                        detail['pic_ids'] = []
                    detail['comments_count'] = data['comments_count']
                    detail['mid'] = data['mid']
                    detail['article_detail'] = data['text_raw'].strip('\n').strip('\u200b')
                    if len(detail_list) <= 50:
                        detail_list.append(detail)
                except Exception as e:
                    print(e)
        print(UID)
        name = redis_read.get(UID).decode()
        info[f'{name}'] = detail_list
        self.artcile_to_redis(info=info)

    def artcile_to_redis(self, info=None):
        redis_pool_1 = redis.ConnectionPool(host='127.0.0.1', port=6379, max_connections=20, db=11)
        redis_store = redis.Redis(connection_pool=redis_pool_1)
        redis_store.set(str(info['uid']), str(info))

    def get_comment_keys(self):
        try:
            redis_read = redis.Redis(host='127.0.0.1', port=6379, db=11)
            comment_dic = {}
            for key in redis_read.keys():
                uid = key.decode()
                infos = redis_read.get(uid).decode()
                infos_dic = eval(infos)
                name = infos_dic.keys()
                comment_mid = []
                comment_dic[f'{uid}'] = comment_mid
                for user_name in name:
                    if user_name != 'uid':
                        data = infos_dic[user_name]
                        for mids in data:
                            comment_mid.append(mids['mid'])
            self.get_comment_info(key=comment_dic)
        except Exception as e:
            print(e)

    def get_comment_info(self, key=None):
        global child_comment
        for uid in key.keys():
            mid_list = key[uid]
            for mid in mid_list:
                max_id = ''
                comment = {}
                info_list = []
                for i in range(5):
                    i += 1
                    if i == 1:
                        params = {
                            'flow': '0',
                            'is_reload': '1',
                            'id': f'{mid}',
                            'is_show_bulletin': '3',
                            'is_mix': '0',
                            'count': '10',
                            'uid': f'{uid}',
                            'fetch_level': '0',
                        }
                    else:
                        params = {
                            'flow': '0',
                            'is_reload': '1',
                            'id': f'{mid}',
                            'is_show_bulletin': '3',
                            'is_mix': '0',
                            'max_id': f'{max_id}',
                            'count': '20',
                            'uid': f'{uid}',
                            'fetch_level': '0',
                        }
                    response = requests.get('https://weibo.com/ajax/statuses/buildComments', params=params,
                                            cookies=self.cookies, headers=self.headers).json()
                    # time.sleep(random.randint(50, 100) / 100)
                    max_id = response['max_id']
                    info = {}
                    child_comment_list = []
                    for data in response['data']:
                        if data['total_number'] != 0:
                            cid = data['id']
                            cid_number = data['total_number']
                            if cid_number <= 19:
                                child_comment = self.child_comment(cid=cid, uid=uid, num=cid_number)
                            elif cid_number >= 19:
                                child_comment = self.child_comment_more(cid=cid, num=cid_number, uid=uid)
                            info[f"{data['text_raw']}"] = child_comment
                            info_list.append(info)
                        info_list.append(data['text_raw'])
                comment[f'{mid}'] = info_list
                print(f'{uid}评论信息{comment}正在保存中')
                self.comment_to_redis(info=comment)

    def child_comment(self, cid=None, uid=None, num=0):
        max_id = '0'
        params = {
            'is_reload': '1',
            'id': f'{cid}',
            'is_show_bulletin': '2',
            'is_mix': '1',
            'fetch_level': '1',
            'max_id': f'{max_id}',
            'count': '20',
            'uid': f'{uid}',
        }
        response = requests.get('https://weibo.com/ajax/statuses/buildComments', params=params,
                                cookies=self.cookies,
                                headers=self.headers).json()
        child_comment = []
        for data in response['data']:
            child_comment.append(data['text_raw'])
        return child_comment

    def child_comment_more(self, cid=None, uid=None, num=0):
        import math
        try:
            max_id = '0'
            child_comment = []
            print(math.ceil(int(num) / 20))
            for i in range(math.ceil(int(num) / 20)):
                params = {
                    'is_reload': '1',
                    'id': f'{cid}',
                    'is_show_bulletin': '2',
                    'is_mix': '1',
                    'fetch_level': '1',
                    'max_id': f'{max_id}',
                    'count': '20',
                    'uid': f'{uid}',
                }
                response = requests.get('https://weibo.com/ajax/statuses/buildComments', params=params,
                                        cookies=self.cookies,
                                        headers=self.headers).json()
                max_id = response['max_id']
                for data in response['data']:
                    child_comment.append(data['text_raw'])
            print(child_comment)
            return child_comment
        except Exception as e:
            print(e)

    def comment_to_redis(self, info=None):
        redis_pool_2 = redis.ConnectionPool(host='127.0.0.1', port=6379, max_connections=20, db=0)
        redis_store = redis.Redis(connection_pool=redis_pool_2)
        for key, value in info.items():
            redis_store.set(str(key), str(value))
        # print(f'{info}保存完成......')

    def artcile_to_excet(self, file_name=None):
        dataframe = pandas.read_excel('采集.xlsx', sheet_name='品牌', engine='openpyxl')
        name_list = []
        art_list = []
        article_info = redis.Redis(host='127.0.0.1', port=6379, db=11)
        for name, uid in zip(dataframe['brand'], dataframe['uid']):
            article_data = article_info.get(uid)
            data = eval(article_data.decode())
            for article in data[f'{name}']:
                attic = article['article_detail']
                name_list.append(name)
                art_list.append(attic)
        frame = {'品牌': name_list, '文章': art_list}
        art_frame = pandas.DataFrame(frame)
        art_frame.to_excel('品牌文章.xlsx', index=False, engine='openpyxl')

    def comments_to_excel(self, file_name=None):
        global comment
        art_read = redis.Redis(host='127.0.0.1', port=6379, db=5)
        detail_read = redis.Redis(host='127.0.0.1', port=6379, db=11)
        comment_read1 = redis.Redis(host='127.0.0.1', port=6379, db=0)
        comment_read2 = redis.Redis(host='127.0.0.1', port=6379, db=13)
        comment_read3 = redis.Redis(host='127.0.0.1', port=6379, db=14)
        keys = art_read.keys()
        name_a = []
        article = []
        comments = []
        for key in keys:
            name = art_read.get(key.decode()).decode()
            art = detail_read.get(key.decode())
            detail = eval(art.decode())
            for art in detail[f'{name}']:
                art_info = art['article_detail']
                mid = art['mid']
                comment1 = comment_read1.get(mid)
                comment2 = comment_read2.get(mid)
                comment3 = comment_read3.get(mid)
                if comment1:
                    comment = comment1.decode()
                elif comment2:
                    comment = comment2.decode()
                elif comment3:
                    comment = comment3.decode()

                for commen in eval(comment):
                    name_a.append(name)
                    article.append(art_info)
                    comments.append(commen)
                    print(commen)

                # except Exception as e:
                #     # comments.append('/')
                #     # print('/')
                #     print(e)
        dict_info = {'博主': name_a, '文章': article, '评论': comments}
        df = pandas.DataFrame(dict_info)
        df.to_excel(f'{file_name}.xlsx', engine='openpyxl', index=False)
        print(comments)
        print(dict_info)

    def search_brand(self):
        name = pandas.read_excel('采集.xlsx', sheet_name='品牌')
        wenzhang = []
        pinpai = []
        for keyword in name['brand']:
            i = 0
            for i in range(4):
                i += 1
                params = {
                    'q': f'{keyword}',
                    'page': f'{i}',
                }

                response = requests.get('https://s.weibo.com/weibo', params=params, cookies=self.cookies,
                                        headers=self.headers).text
                HTML = etree.HTML(response)
                data = HTML.xpath('//*[@id="pl_feedlist_index"]/div[2]/div/div/div[1]/div[2]/p/text()')
                # data_str = etree.tostring(data, encoding='utf-8').decode('utf-8')
                # data1 = re.findall(r'target="_blank">(.*?)a', data_str)
                for info in data:
                    result = info.strip() + info.strip()
                    pinpai.append(keyword)
                    wenzhang.append(result)
                    print(result)
                if len(wenzhang) >= 50:
                    continue
        jieguo = {}
        jieguo['品牌'] = pinpai
        jieguo['文章'] = wenzhang
        df = pandas.DataFrame(jieguo)
        df.to_excel('品牌搜索文章1.xlsx', index=False, engine='openpyxl')
        print(jieguo)


if __name__ == '__main__':
    weibo = UserID()
    # 将用户列表导入redis数5号据库
    weibo.ID_to_redis()
    # 通过ID号搜索用户文章信息并存入redis11号库
    weibo.get_UID()
    # 通过文章信息爬取评论内容并保存到redis的0号库
    weibo.get_comment_keys()
    # 将评论信息导出为Excel文件
    weibo.comments_to_excel(file_name='123')
    # 将文章导出为excel文件
    weibo.artcile_to_excet(file_name='品牌文章')
