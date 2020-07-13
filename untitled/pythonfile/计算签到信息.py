#取到每一个学生的签到信息
retdict={}
def putInfoToDict(fileName):
    saleInfo= fileName
    fo = open(saleInfo, 'r')

    for one in fo.readlines():
        temp=one.replace('(','').replace(')','').replace(';','').strip().split(',')
        # print(temp)
        stuid=int(temp[1])
        time=temp[0].replace("'",'')
        lessid=int(temp[2])
        retdict2={'lessid':lessid,'checkintime':time}
        if stuid not in retdict:
            retdict[stuid]=[]
        retdict[stuid].append(retdict2)
            # print(retdict)
    return retdict




ret = putInfoToDict('F:/file3.txt')

import pprint

pprint.pprint(ret)








