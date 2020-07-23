# author:JinMing time:2020-05-09

# print(ord('这'))  字符的unicode
# # print(hex(34567)) 十进制转化为十六进制
# # var = '年后'.encode('utf8')
# # print(var)
list=[]
with open('./gbk1/gbk编码.txt','r',encoding='gbk') as file1:
    data1=file1.readline()
    list.append(data1)

with open('./utf8/utf8编码.txt','r',encoding='utf8') as file1:
    data2=file1.readline()
    list.append(data2)

newdata=','.join(list)

print(newdata)

file3=input('请输入新文件名称:')

with open(f'./new/{file3}.txt','w',encoding='utf8') as file3:
    for one in list:
        file3.write(one+'\n')





