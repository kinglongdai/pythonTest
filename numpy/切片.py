import numpy as np


# 切片

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

