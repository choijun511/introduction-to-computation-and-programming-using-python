# 用迭代的方式实现一个斐波那契数列

#def fib(x):
#    if x == 0 or x == 1:
#        return 1
#    else:
#        return fib(x-1) + fib(x-2)

#x = input('请输出一个自然数')
#print(fib(int(x)))

# 用字典实现一个斐波那契数列
def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans

d = {1:1, 2:2}
print(fib_efficient(6,d))
