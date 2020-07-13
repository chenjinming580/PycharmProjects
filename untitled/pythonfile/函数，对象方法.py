# def func():#函数定义不会执行里面代码
#     print('step1')
#     print('step2')
#     f2()
#
# def f2():#函数定义不会执行里面代码
#     print('xxxxx')
#
# func()#执行代码


# str1 = ' gahaskk'
#
# print(str1.count('a'))  # 计算字符串中包含的多少个指定的子字符串
# print(str1.endswith('k'))  # 检查字符串是否以指定的字符串结尾  --返回值 bool
# print(str1.startswith('b'))  # 检查字符串是否以指定的字符串开头  --返回值 bool
#
# print(str1.find('a'))  # 返回指定的子字符串在字符串中出现的位置,只返回查找第一个出现的位置
# print(str1.find('a', 1)) #指定开始查找第二个a（0代表一个a）下标位置
# print(str1.find('x')) #如果要查找的内容，不在该对象里面，那么该方法返回  -1
#
# print(str1.isalpha()) #检查字符串中是否都是字母  ---返回值  bool
#
# str2=['a','b''c','d']
#
# print('*'.join(str2)) #将 sequence类型的参数的元素字符串合并(连接)到一个字符串，'*' 作为分隔符
# print(str1.split('a'))#切割---返回是list
#
# print(str1.replace('a','X')) #替换字符串里面指定的子字符串
# print(str1.strip()) # 将字符串前置空格和后置空格删除
# print(str1.lstrip()) #将字符串前置空格删除
# print(str1.rstrip()) #将字符串后置空格删除
#
# str3 = '   a b c    ' #将所有空格去掉
# #第一种方案
# str4=(str3.strip())
# str5=(str4.split(' '))
# print(str5)
# print(''.join(str5))
# #第二种方案
# print(str3.replace(' ',''))
# print(max([12,13,14,15]))
# print(max((12,13,14)))


# def getName(srcStr):
    # return srcStr.split(',')[1].replace(' ','')[9:]
    # return srcStr.split('the name is ')[1].split(',')[0]
    #return srcStr.split(',')[1].split(' is ')[-1]




# print(getName('A old lady come in, the name is Jack, level 94454'))
# ['A old lady come in',' the name is Mary',' level 94454']
# [' the name','marry']
#
# str1 = 'abcaa'
# print(str1.replace('a','x',1))

# alist = [10,20,30,40,20,50,20,]
# del alist[0]
# print(alist)
print('my name is {}{}'.format('Mike'))