# author:JinMing time:2020-04-21
# from config import *
age=13
bbb=1323242
class ceshiclass:

    name='小陈'
    def __init__(self):
        self.age=age

    def ceshi(self,id,sex=None):
        id=id
        name=self.name
        age=self.age
        sex=sex
        return f'name={name},age={age},sex={sex}'

    @classmethod
    def ceshi2(cls):
        name=cls.name
        return name

    @staticmethod
    def ceshi3():
        name=1213
        return name




str=ceshiclass().ceshi3()

# tt=str.ceshi(1)
print(str)


