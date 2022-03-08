# 输入输出

f = float(input('请输入一个小数: '))
print(f)
print('%f=' % f)
print('%f+1=%f' % (f, f+1))

print('hello, world!')
# print("你好,世界！")
print('你好', '世界')
print('hello', 'world', sep=', ', end='!')  # 以，间隔，以！结束
print('goodbye, world', end='!\n')  # 换行

print(123+456)
print("123"+str(456))

# 换行，不能有空格
a = 1 +\
    2
print(a)

print("{0}".format(a))

#一般来说，以双下划线开头并结尾的变量名是用来表示Python实现细节的命名模式。而这个列表中没有下划线的属性是字符串对象能够调用的方法。
print(dir(str))

#2\8\16进制
print(bin(9))
print(oct(9))
print(hex(9))

print(3>2>1)


