# 运算符
import math
from random import random
from pyrsistent import b
from soupsieve import match
from sqlalchemy import true

# 运算符

a = 1
b = 2
print(a, b)
a, b = 3, 4
print(a, b)
a, b = b, a
print(a, b)

a += 1  # 不支持++
print(a)

print(a/2)
print(a//2)  # 取整

# 不支持？：
b = "small" if(a > 1) else "big"
print(b)


if(a > 1):
    b = "small"
else:
    b = "big"
print(b)


print(True or False)
print(True and False)
print(True is False)  # ==
print(True is not False)  # !=

# 在对象类型是可变的情况下是不相等的
a, b = [], []
print(a is b)  # 对象不相等
print(a == b)  # 值相等


print(type("123"))
print(str(123))

print(10/4)
print(10//4)
print(10/4.0)
print(10//4.0)


print(math.floor(2.6))#地板
print(math.trunc(2.4))#截断
print(round(1.22222,2))

