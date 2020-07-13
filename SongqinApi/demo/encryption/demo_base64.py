# author:JinMing time:2020-04-30
import base64

str="sfdsfdsfasewrewtrevcxvcxdfds"
pwd=base64.b64encode(str.encode("UTF-8"))
print('编码后的结果为：',pwd)
bstr=base64.b64decode(pwd)
print('解码后的字节码为：',bstr)
print('解码后：',bstr.decode('UTF-8'))
