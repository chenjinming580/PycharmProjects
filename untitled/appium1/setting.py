# author:JinMing time:2020-04-15
import hashlib
md5_object = hashlib.md5()
md5_object.update(b'boss123')
md5_result = md5_object.hexdigest()
password ='boss124'

print(md5_result)