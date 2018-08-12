# 在牛顿-拉夫森法的视线中添加一些代码，跟踪求平方根所用的迭代次数。在这段代码的基础上编写一个程序，比较牛顿-拉夫森法和二分法查找的效率。

def Guess(x):
    epsilon = 0.001
    guess = 0
    guessNum = 0
    while abs(guess * guess - int(x)) >= epsilon and guess <= int(x):
        guess += epsilon
        guessNum += 1
    if abs(guess * guess - int(x)) >= epsilon:
        print('没有找到',x,'的平方根')
    else:
        print(guess,' 是接近于x平方根的一个数')
        print('这是穷举法猜测的第', guessNum, '次')

def Bisection(x):
    epsilon = 0.001
    guessNum = 0
    low = 0
    high = int(x)
    half = (high + low)/ 2.0
    while abs(half * half - int(x)) >= epsilon: # 这里的abs()函数一定要注意，因为可能出现大，也可能出现小
        guessNum += 1
        if half * half < int(x)+ epsilon:
            low = half
        else:
            high = half
        half = (high + low)/2.0
        print(half)
    print(half, ' 是接近于x平方根的一个数')
    print('这是二分法猜测的第', guessNum, '次')

def Newtonsmethod(x):
    epsilon = 0.001
    guess = int(x)/2.0
    guessNum = 0
    while abs(guess * guess - int(x)) >= epsilon:
        guess = guess -(((guess * guess) - int(x))/(2*guess))
        guessNum += 1
    print(guess, ' 是接近于x平方根的一个数')
    print('这是牛顿逼近法猜测的第', guessNum, '次')


x = input('请输入一个正整数')
Guess(x)
Bisection(x)
Newtonsmethod(x)
