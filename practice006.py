# 用迭代的方式实现一个斐波那契数列

def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

x = input('请输出一个自然数')
print(fib(int(x)))
