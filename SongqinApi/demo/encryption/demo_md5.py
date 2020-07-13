# author:JinMing time:2020-04-30
import hashlib


pwd='sdfsdfsdf'

md5=hashlib.md5()
md5.update(pwd.encode(encoding='UTF-8'))
print('MD5加密后结果为：'+md5.hexdigest())