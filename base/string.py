# 字符串
from itertools import count

a = "hello"
print(len(a))
print(a+str(123))
print(a[1])
print(a[-1])

print(a.title())
print(a.isupper())
print(a.upper())
print(a.lower())
print(a.startswith("h"))
print(a.endswith("@"))

print(a[1:3])
print(a[1:])
print(a[1:4:2])
print(a[:])

print(a.find('l'))
print(a.replace('h', 'k'))
print(a.split("e"))
print(a.lstrip())
print(a.isalpha())