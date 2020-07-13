alist = [3,1,7,0]
def mySort(list):
    alist5=[]
    for one in range(0,len(list)):
        alist2=min(list) #找出最小值
        alist3=list.index(alist2) #记录最小值的下标
        alist4=list.pop(alist3) #记录删除最小值下标的值
        alist5.append(int(alist4))#新增最小值
    return alist5

print(mySort([0,1,9,8]))




