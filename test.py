# while 寫法
n= 9
r = 1
while n > 0:
    r = r * n
    n = n - 1

# 99乘法
for i in range(1,10):
    for j in range(1,10):
        print(f'{j}x{i}={j*i:2d}', end=' ') #第一回圈
    print() #第二回圈

# python 不需要宣告
x = "Hello"
print(x)
x = 5
print(x)
5
del x
print(x)