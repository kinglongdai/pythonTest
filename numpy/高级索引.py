
import numpy as np


# 高级索引

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

