
import numpy as np


# 数组迭代

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


# numpy.transpose 函数用于对换数组的维度，格式如下：
# numpy.transpose(arr, axes)
# 参数说明:
# arr：要操作的数组
# axes：整数列表，对应维度，通常所有维度都会对换。


a = np.arange(12).reshape(3,4)
 
print ('原数组：')
print (a )
print ('\n')
 
print ('对换数组：')
print (np.transpose(a))

#等价
print ('转置数组：')
print (a.T)


