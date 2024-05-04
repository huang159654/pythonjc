import json
import re

import pandas as pd
df = pd.read_csv('转发500(1).csv')
df['近期文章'] = df['近期文章'].str.replace('[','')
df['近期文章'] = df['近期文章'].str.replace(']','')
df.to_csv('new_file.csv', index=False)
print(df)
        # sa=re.findall("'(.*?)'",i,re.S)
        # json_str = json.dumps(sa)
        # json_obj = json.loads(json_str)
        # for g in json_obj:
        #         l=g
        #         print(l)
        #         break
                # print(l)
        #         df1 = df['文章ID','博主id','用户ID','拼接用户ID','评论时间','文本内容','点赞','用户名','用户认证情况','用户所在地区','性别','用户关注数','用户简介','用户粉丝数','生日','加入微博时间','用户标签','近期发表微博的','用户发布微博数量','用户会员']
        #         # print(df1)
        #         # # 最后，你可以将结果写回到一个新的CSV文件中：
        #         # # python复制代码
        #         l.to_csv('new_file.csv', index=False)
        # #这样就可以把选定的列导出成新的CSV文件了。
