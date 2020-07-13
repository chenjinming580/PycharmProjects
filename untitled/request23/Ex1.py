# author:JinMing time:2020-04-21
import requests

r=requests.get('https://www.baidu.com',verify=True)
r.encoding='utf-8'

print(r.text)


