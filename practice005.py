# 编写一个函数IsIn，接受两个字符串作为参数，如果一个字符串是另一个字符串的一部分，返回True，否则返回False

def IsIn(x,y):
    if (x in y) or (y in x):
        print(True)
    else:
        print(False)

IsIn('abscsa','bc')
IsIn('abscsa','ab')
IsIn('ab','abscsa')
