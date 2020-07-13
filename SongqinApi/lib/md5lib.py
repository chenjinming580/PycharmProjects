# author:JinMing time:2020-04-30
import hashlib
def md5(pwd):
    md5=hashlib.md5()
    md5.update(pwd.encode(encoding='UTF-8'))
    md5.hexdigest()
    return md5.hexdigest()

