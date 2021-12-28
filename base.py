
import json
import collections
import heapq
'''list/tuple/dict 
可变：列表、字典
不可变：数字、字符串、元组
[1, 2, 'aa']
(1, 2)
{'1': 2, '2': 3}'''



#
a = (1, 2)
b, c = a
print(b)

# 占位符
a = (1, 2, 3)
b, _, _ = a
print(b)

#
a = (1, 2, 3)
b, *c = a
print(c)

# 获取最大的3个
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))  # Prints [42, 37, 23]


portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(2, portfolio, key=lambda s: s["shares"])
print(cheap)

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
a = list(nums)
print(a)
heapq.heapify(a)
print(a)


d = collections.defaultdict(list)
d['a'].append(1)
print(d)


d = collections.OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])

print(json.dumps(d))
