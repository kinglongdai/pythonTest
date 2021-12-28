
import numpy as np

# 数据类型
'''
# bool_:true/false
# int_(int8、int16、int32、int64=i1、i2、i3、i4)
# float_
# complex_
#b	布尔型、i	(有符号) 整型、u	无符号整型 integer、f	浮点型、c	复数浮点型、m	timedelta（时间间隔）、M	datetime（日期时间）、O	(Python) 对象、S, a	(byte-)字符串、U	Unicode、V	原始数据 (void)
# >大端、<小端

print(np.dtype(np.bool_))
print(np.dtype(np.int64))
print(np.dtype('i4'))
print(np.dtype('<i4'))  # print(np.dtype('>i4'))不支持
print(np.dtype(np.float_))
print(np.dtype('f4'))
print(np.dtype('<f4'))


print(np.dtype([('age',np.int8)]))

#自定义结构
dt = np.dtype([('age',np.int8)]) 
a = np.array([(10,),(20,),(30,)], dtype = dt) 
print(a)
print(a['age'])


student = np.dtype([('name','S100'), ('age', 'i1'), ('marks', 'f4')]) 
b = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 
print(b)

'''

# 数组属性
'''
# ndarray.ndim	秩，即轴的数量或维度的数量
# ndarray.shape	数组的维度，对于矩阵，n 行 m 列
# ndarray.size	数组元素的总个数，相当于 .shape 中 n*m 的值
# ndarray.dtype	ndarray 对象的元素类型
# ndarray.itemsize	ndarray 对象中每个元素的大小，以字节为单位
# ndarray.flags	ndarray 对象的内存信息
# ndarray.real	ndarray元素的实部
# ndarray.imag	ndarray 元素的虚部
# ndarray.data	包含实际数组元素的缓冲区，由于一般通过数组的索引获取元素，所以通常不需要使用这个属性。


print(np.arange(24).ndim)
print(np.shape(np.array([[1, 2, 3], [4, 5, 6]])))

a = np.array([[1,2,3],[4,5,6]]) 
a.shape =  (3,2)  
print (a)

x = np.array([1,2,3,4,5], dtype = np.int8)  
print (x.itemsize)

'''

# 创建数组
'''
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

'''

# 切片
'''
a = np.arange(10)
s = slice(2, 7, 2)
print(a[s])

a = np.arange(10)
b = a[2:7:2]   # 从索引 2 开始到索引 7 停止，间隔为 2
print(b)

#切片还可以包括省略号 …，来使选择元组的长度与数组的维度相同
a = np.array([[1,2,3],[3,4,5],[4,5,6]])  
print (a[...,1])   # 第2列元素
print (a[1,...])   # 第2行元素
print (a[...,1:])  # 第2列及剩下的所有元素

'''

# 高级索引
'''

x = np.array([[0,  1,  2], [3,  4,  5], [6,  7,  8], [9,  10,  11]])
print('我们的数组是：')
print(x)
print('\n')
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
print('这个数组的四个角元素是：')
print(y)

# 布尔索引
x = np.array([[0,  1,  2], [3,  4,  5], [6,  7,  8], [9,  10,  11]])
print(x[x > 5])

# 使用了 ~（取补运算符）来过滤 NaN。
a = np.array([np.nan,  1, 2, np.nan, 3, 4, 5])
print(a[~np.isnan(a)]) #iscomplex

#花式索引
x = np.arange(32).reshape((8, 4))
print(x)
print("~~~~~~~~~~~")
print(x[[4, 2, 1, 7]])

#传入多个索引数组（要使用np.ix_） 
x=np.arange(32).reshape((8,4))
print (x[np.ix_([1,5,7,2],[0,3,1,2])])



# 广播
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
print(a * b)


a = np.array([[0, 0, 0],
              [10, 10, 10],
              [20, 20, 20],
              [30, 30, 30]])
b = np.array([1, 2, 3])
print(a + b)

'''

# 数组迭代
'''
a = np.arange(6).reshape(2, 3)
print(a)
print('~~~~~~~~~~~~~~~~')
for x in np.nditer(a):
    print(x, end=", ")

print('\n~~~~~~~~~~~~~~~~')
for x in np.nditer(a, order='C'):
    print(x, end=", ")

print('\n~~~~~~~~~~~~~~~~')
for x in np.nditer(a, order='F'):
    print(x, end=", ")

print('\n~~~~~~~~~~~~~~~~')

'''

#flat	数组元素迭代器
a = np.arange(9).reshape(3,3) 
print ('原始数组：')
for row in a:
    print (row)
 
#对数组中每个元素都进行处理，可以使用flat属性，该属性是一个数组元素迭代器：
print ('迭代后的数组：')
for element in a.flat:
    print (element)


# numpy.ndarray.flatten 返回一份数组拷贝，对拷贝所做的修改不会影响原始数组，格式如下：
# ndarray.flatten(order='C')
# 参数说明：
#order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'K' -- 元素在内存中的出现顺序
a = np.arange(8).reshape(2,4)
 
print ('原数组：')
print (a)
print ('\n')
# 默认按行
 
print ('展开的数组：')
print (a.flatten())
print ('\n')
 
print ('以 F 风格顺序展开的数组：')
print (a.flatten(order = 'F'))

#numpy.ravel
#numpy.ravel() 展平的数组元素，顺序通常是"C风格"
a = np.arange(8).reshape(2,4)
 
print ('原数组：')
print (a)
print ('\n')
 
print ('调用 ravel 函数之后：')
print (a.ravel())
print ('\n')
 
print ('以 F 风格顺序调用 ravel 函数之后：')
print (a.ravel(order = 'F'))

'''
numpy.transpose 函数用于对换数组的维度，格式如下：
numpy.transpose(arr, axes)
参数说明:
arr：要操作的数组
axes：整数列表，对应维度，通常所有维度都会对换。
'''

a = np.arange(12).reshape(3,4)
 
print ('原数组：')
print (a )
print ('\n')
 
print ('对换数组：')
print (np.transpose(a))

#等价
print ('转置数组：')
print (a.T)

'''

'''
