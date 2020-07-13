# stuinfo=input('请输入学生的姓名和年龄:')
# stuinfo2=stuinfo.replace(' ','').split(';')
# # print(stuinfo2)
# for one in stuinfo2:
#     if ',' not in one:
#         continue
#     name,age=one.split(',')
#     name=name.strip()
#     age=age.strip()
#     print(f'{name:<20}: {age:0>2}')

# inputStr = input('Please input student age info:')
# studentInfo = inputStr.split(';')
# print(studentInfo)
# for one in studentInfo:
#     # check if it is valid input
#     if ',' not in one:
#         continue
#
#     name, age = one.split(',')
#     name = name.strip()
#     age = age.strip()
#
#     #  check is age digit
#     if not age.isdigit():
#         continue
#
#     age = int(age)
#
#     print('%-20s :  %02d' % (name, age))
#     # print('{:20} :  {:02}'.format(name, age))
#     # print(f'{name:20} :  {age:02}')


alist = ['Mike', 'Jack', 'Mary', 'Pat','Will','Lisa']

for one in range(0,2):# 2次  0  1

    for name in alist:

            # print(name)

        if name == 'Jack':

            continue
        print(name)
