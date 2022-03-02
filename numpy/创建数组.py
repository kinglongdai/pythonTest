import numpy as np

# 创建数组

#numpy.empty(shape, dtype = float, order = 'C')

# shape	数组形状
# dtype	数据类型，可选
# order	有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。
x = np.empty([3, 2], dtype=int)
print(x)

# zeros
# 默认为浮点数
x = np.zeros(5)
print(x)

# 设置类型为整数
y = np.zeros((5,), dtype=np.int)
print(y)

# 自定义类型
z = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
print(z)

# ones
# 默认为浮点数
x = np.ones(5)
print(x)

# 自定义类型
x = np.ones([2, 2], dtype=int)
print(x)

# numpy.asarray(a, dtype = None, order = None)

# a	任意形式的输入参数，可以是，列表, 列表的元组, 元组, 元组的元组, 元组的列表，多维数组
# dtype	数据类型，可选
# order	可选，有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。

print(np.asarray([1, 2, 3]))  # list
print(np.asarray((1, 2, 3)))  # tuple
print(np.asarray([(1, 2, 3), (4, 5)]))  # tuple list

# numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)
# 注意：buffer 是字符串的时候，Python3 默认 str 是 Unicode 类型，所以要转成 bytestring 在原 str 前加上 b。

# buffer	可以是任意对象，会以流的形式读入。
# dtype	    返回数组的数据类型，可选
# count	    读取的数据数量，默认为-1，读取所有数据。
# offset	读取的起始位置，默认为0。

#rint(np.frombuffer('Hello World', dtype='S1'))
print(np.frombuffer(b'Hello World', dtype='S1'))

# numpy.fromiter 方法从可迭代对象中建立 ndarray 对象，返回一维数组
print(np.fromiter(iter(range(5)), dtype=float))

# numpy.arange(start, stop, step, dtype)
# start	起始值，默认为0
# stop	终止值（不包含）
# step	步长，默认为1
# dtype	返回ndarray的数据类型，如果没有提供，则会使用输入数据的类型。

print(np.arange(5))
print(np.arange(10, 20, 2))

# numpy.linspace 函数用于创建一个一维数组，数组是一个等差数列构成的，格式如下：
# np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
# start	序列的起始值
# stop	序列的终止值，如果endpoint为true，该值包含于数列中
# num	要生成的等步长的样本数量，默认为50
# endpoint	该值为 true 时，数列中包含stop值，反之不包含，默认是True。
# retstep	如果为 True 时，生成的数组中会显示间距，反之不显示。
# dtype	ndarray 的数据类型

print(np.linspace(1, 10, 10))
print(np.linspace(1, 10, 10, retstep=True))
print(np.linspace(1, 10, 10).reshape([10, 1]))


# numpy.logspace 函数用于创建一个于等比数列。格式如下：
# np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)

# start	序列的起始值为：base ** start
# stop	序列的终止值为：base ** stop。如果endpoint为true，该值包含于数列中
# num	要生成的等步长的样本数量，默认为50
# endpoint	该值为 true 时，数列中中包含stop值，反之不包含，默认是True。
# base	对数 log 的底数。
# dtype	ndarray 的数据类型

print(np.logspace(1.0,  2.0, num=10))
print(np.logspace(0,9,10,base=2))

