import numpy as np

# 数据类型
'''
# bool_:true/false
# int_(int8、int16、int32、int64=i1、i2、i3、i4)
# float_
# complex_
#b	布尔型、i	(有符号) 整型、u	无符号整型 integer、f	浮点型、c	复数浮点型、m	timedelta（时间间隔）、M	datetime（日期时间）、O	(Python) 对象、S, a	(byte-)字符串、U	Unicode、V	原始数据 (void)
# >大端、<小端
'''
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

