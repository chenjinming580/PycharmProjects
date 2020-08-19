# author:JinMing time:2020-04-21
import requests

rs=requests.get('https://www.baidu.com',verify=True)
rs.encoding='utf-8'

print(rs.text)


