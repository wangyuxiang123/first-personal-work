import json
import requests

headers = {'authoration': 'apicode', 'apicode': 'a92c30ec488341bda81968a590c606e4',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68'}
url = 'http://api.yonyoucloud.com/apis/dst/ncov/wholeworld'
response = requests.get(headers=headers, url=url)
response_dict = response.json()

print(type(response_dict))

data = response_dict["data"]["continent"]  # 初步处理州数据获取

Asia = data[0]["country"]
Europe = data[1]["country"]
NorthAmerica = data[2]["country"]
SouthAmerica = data[3]["country"]
Africa = data[4]["country"]
Oceania = data[5]["country"]

country = Asia + Europe + NorthAmerica + SouthAmerica + Africa + Oceania

print(len(country))
print(type(country))
with open('../Data/translate.json', 'r', encoding='utf-8') as f:
    c2e = json.load(f)
countryList = []
otherList = []

for i in country:
    try:
        countryDict = {}
        countryDict['name'] = c2e[i["provinceName"]]
        countryDict['value'] = i["confirmedCount"]
        countryList.append(countryDict)
    except:
        otherList.append(i["provinceName"])


with open("../Data/global_epidemic_statistics.json", 'w',encoding='UTF8') as f:
    json.dump(countryList,f,ensure_ascii=False)
    print("写入global_epidemic_statistics.json成功")
