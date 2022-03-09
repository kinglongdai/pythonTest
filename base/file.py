# 文件


import imp  #导入完整的模块
import re
from tkinter import W  #从tkinter中导入W
from math import * #导入math中的所有，不推荐

'''
output=open(r"C:\1.txt", W)
input=open('C:\\1.txt')
input.read()
input.readline()
input.readlines()
output.write()
output.writelines()
output.close()
'''

# with 关键字
# == 判断相等
# is 判断是否是同一个


# 剩余的给*,没有给[]
L = [1, 2, 3, 4]
*a, b, c = L
print(a, b, c)
a, *b, c = L
print(a, b, c)
a, b, *c = L
print(a, b, c)


while L:
    front, *L = L
    print(front, L)
else:
    print("结束")

