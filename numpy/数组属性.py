import numpy as np

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
'''

print(np.arange(24).ndim)
print(np.shape(np.array([[1, 2, 3], [4, 5, 6]])))

a = np.array([[1,2,3],[4,5,6]]) 
a.shape =  (3,2)  
print (a)

x = np.array([1,2,3,4,5], dtype = np.int8)  
print (x.itemsize)

