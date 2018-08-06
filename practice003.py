# 编写一个程序，要求用户输入一个整数，然后输出两个整数root和pwr，满足0 < pwr < 6，并且root**pwr等于用户输入的整数。如果不存在这样一对整数，则输出一条消息进行说明。

intger = int(input('请输入一个整数'))

root = 0
pwr = 1

while pwr < 6:
    while root <= intger:
        root = root + 1
        if root**pwr == intger:
            print('root的值是:' + str(root) + 'pwr的值是:' + str(pwr))
    pwr = pwr + 1
    else:
        print('there is no number ')
