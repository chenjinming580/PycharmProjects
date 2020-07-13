#1.取出每行员工的信息并计算税后工资
salInfo='F:/file1.txt'
saleInfo2='F:/file2.txt'
fo=open(salInfo,'r')
fo2=open(saleInfo2,'w')
for one in fo.readlines():
    temp=one.replace('\n','').split(';')
    wmq=temp[0].split(':')[-1].strip()
    salary1=int(temp[-1].split(':')[-1].strip())
    tallage=int(salary1*0.1)
    realsal=int(salary1*0.9)
    info=f'name:{wmq:<8}; salary: {salary1};tax: {tallage};income: {realsal}'#格式化字符串
    # 2.存入新的文件中
    fo2.write(info+'\n')








