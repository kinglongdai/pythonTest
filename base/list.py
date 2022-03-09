#列表/数组


a=[1,2,3,4]
a[0]="k"
print(a)
print(len(a))
print(a[:2])

a.append('p')
print(a)
a.insert(1,'M')
print(a)
a.remove('P')
a.pop(1)
del a[2]

b=[[1,2,3],[4,5,6]]
print(b[0])

a=[x*2 for x in range(101) if x%2==0]
print(a)


c=list(map(sum,b)) #之和作为入参
print(c)

