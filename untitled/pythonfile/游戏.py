class Tiger:
    nickName = '老虎'  #静态属性
    def __init__(self,inWeight):#实例属性
        self.weight = inWeight

    #实例方法--
    def roar(self):
        print('我是老虎---wow！，体重减5斤')
        self.weight -= 5

    def feed(self,food):
        if food == 'meat':
            self.weight += 10
            print('恭喜，喂食正确，体重增加10斤')
        else:
            self.weight -= 10
            print('抱歉，喂食错误，体重减少10斤')

class Sheep:
    nickName = '羊'  #静态属性
    def __init__(self,inWeight): #实例属性
        self.weight = inWeight

    #实例方法--
    def roar(self):
        print('我是羊---mie~~，体重减5斤')
        self.weight -= 5

    def feed(self,food):
        if food == 'grass':
            self.weight += 10
            print('恭喜，喂食正确，体重增加10斤')
        else:
            self.weight -= 10
            print('抱歉，喂食错误，体重减少10斤')


class Room:
    def __init__(self,inNum,inAnimal):
        self.num = inNum
        self.animal = inAnimal

from random import randint

#---------游戏初始化---------------
roomList = []#元素---房间实例
for one in range(1,11):
    if randint(0,1) == 1:
        ani = Tiger(200)
    else:
        ani = Sheep(100)
    room = Room(one,ani)
    roomList.append(room)
    print()





