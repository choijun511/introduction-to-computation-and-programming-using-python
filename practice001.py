# 编写一个程序，检查3个变量x,y,z，输出其中最大的奇数。如果其中没有奇数，就输出一个消息进行说明

x = input('请输入x的值')
y = input('请输入y的值')
z = input('请输入z的值')

old = [int(x),int(y),int(z)]
new = []

for i in old:
    if i%2 != 0:
        new.append(i)

if len(new) != 0:
    print(max(new))
else:
    print('there is no odd number in x,y,z')
