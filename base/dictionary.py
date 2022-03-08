# 字典

from traceback import print_tb


a = {1: 2, 3: 4}
print(a)

print(a.keys())
print(a.values())


b = {}
b['kk'] = 'kingongdai'
print(b)

c = {'kk': [1, 2, 3],
     'pp': {'q': 12, 'w': 'ww'}}
print(c['pp'])
print(c['pp']['q'])
print(c['kk'])
c['kk'].append(4)
c['pp']['q'] = 123
print(c)


print(list(c.keys()))

for i in c.keys():
    print(i.upper())

d = 2
while d > 0:
    d -= 1
    print(d)
    
e=[i*2 for i in range(10)]
print(e)

print(100 in e)
if not 100 in e:
    print("不在")

 
