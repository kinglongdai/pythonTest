

# python 没有？：
from os import readlink
from typing import AsyncGenerator


a = 2 if 1 > 2 else 1
print(a)

# python 没有++
a = a+1

# for--else 语法
# 没有break的情况下else会执行


print(3 > 4)

# 0123456789012345678901234567890123456789012345678901234567890'
record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])

print(int(record[20:23]))
print(float(record[31:37]))
print(cost)

a = slice(5, 50, 2)
print(a.start)
print(a.stop)
print(a.step)


s = 'HelloWorld'
a.indices(len(s))
for i in range(*a.indices(len(s))):
    print(s[i])


# 不拼接+
name = "kinglong"
age = 32
print(f"{name}:{age}")


def manually_calling_close_on_a_file(filename):
    with open(filename) as f:
        f.write("hello!\n")


def mutable_default_arguments():
    # 判断空
    def append(n, l=None):
        if l is None:
            l = []
        l.append(n)
        return l

    l1 = append(0)  # [0]


# 试用items
def using_dict_items():
    d = {"a": 1, "b": 2, "c": 3}
    for key, val in d.items():
        print(key)
        print(val)

#
