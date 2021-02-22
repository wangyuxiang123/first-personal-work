import json
import requests

headers = {'authoration': 'apicode', 'apicode': 'a92c30ec488341bda81968a590c606e4',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68'}
url = 'http://api.yonyoucloud.com/apis/dst/ncov/wholeworld'
response = requests.get(headers=headers, url=url)
response_dict = response.json()
print(type(response_dict))
print(response_dict)

with open("demo.json","w",encoding="UTF8") as f:
    json.dump(response_dict,f,ensure_ascii=False)
