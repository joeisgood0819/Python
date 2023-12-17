x = [1, 2 ,3]
x = [2 , "two", [1, 2, 3], 1, 3, 3]
print (len(x))

x[-1] #後面數來第一個 [1 ,2 ,3]

#slice功能
print(x[0:4])
print(x[-2:-1])
print(x[-1:2]) #空list
print(x[:4])
print(x[2:])

y = x[:] #copy x list into y
y [0] = 'one'
print(x)
y = x
y [0] = 'one' #同步修改
print(x)

x = [1:3] = ["one", "two", "three"] #可以更多也可以更少=直接取代替換


