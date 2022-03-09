# 类

from json.tool import main
from socket import if_nameindex

from scipy import ifft


class kinglong:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printHello(self):
        print("hello "+self.name)

    def printHello2(name='kk'):
        print("hello "+name)

    def square(x):         # 计算平方数
        print(x ** 2) 


kinglong.printHello2("dai")
dai = kinglong(kinglong, 12)
print(dai.name)

map(kinglong.square, [1, 2, 3, 4, 5])    # 计算列表各个元素的平方

if __name__=='__main__':
    pass;
