
'''
数组的属性:确定数组的大小、形状、存储大小、数据类型。
数组的索引:获取和设置数组各个元素的值。
数组的切分:在大的数组中获取或设置更小的子数组。
数组的变形:改变给定数组的形状。
数组的拼接和分裂:将多个数组合并为一个，以及将一个数组分裂成多个。
'''

import numpy as np

np.random.seed(0)  # 设置随机数种子
x3 = np.random.randint(10, size=(3, 4, 5))  # 三维数组
print(x3.ndim)  # 维度
print(x3.shape)  # 维度的大小
print(x3.size)  # 数组的个数
print(x3.dtype)  # 类型


x1 = np.array([[12, 5, 2, 4],
               [7, 6, 8, 8],
               [1, 6, 7, 7]])
x1[:2, :3]  # 两行，三列
x1[0] = x1[0, :]  # 第一行
x1[:, 0]  # 第一列

x1.copy()  # 创建副本


# 变形
x = np.arange(1, 10).reshape((3, 3))  # 3行3列
x[np.newaxis, :]  # 通过newaxis获得的行向量

x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
np.concatenate([x, y])  # 拼接


grid = np.array([[1, 2, 3],
                 [4, 5, 6]])
np.concatenate([grid, grid])  # 拼接自己
