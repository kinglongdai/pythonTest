
import numpy as np
# numpy数据类型要比python内置的要多
print(np.__version__)  # 版本


#创建数组
np.array([3.14, 4, 2, 3])  # 数据类型以第一个为准
np.array([3.14, 4, 2, 3], dtype='int')  # 指定数据类型
np.array([3.14, 4, 2, 3], dtype=int)  # 指定数据类型
np.array([3.14, 4, 2, 3], dtype=np.int32)  # 指定数据类型
np.array((2, 2), dtype=[('x', 'i4'), ('y', 'f2')])#分别指定类型

# [行、列]
np.empty([3, 2], dtype=int)  # 空数组，是内存空间中的任意值
np.zeros(10, dtype=int)  # 默认值0
np.ones(10, dtype=int)  # 默认值1
np.full((3, 5), 3.14)  # 指定默认值，这里是3.14
np.arange(0, 20, 2)  # 从0开始，到20结束，步长为2的数组
np.linspace(0, 1, 5)  # 在0~1之间，平均分为分布5个数值
np.random.normal(0, 1, (3, 3))  # 创建一个3×3的、均值为0、方差为1的正态分布的随机数数组
np.random.randint(0, 10, (3, 3))  # 创建一个3×3的、[0, 10)区间的随机整型数组
np.eye(3)# 创建一个3×3的单位矩阵





