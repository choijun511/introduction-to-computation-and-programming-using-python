# 实现一个数据区域之间，所有的偶数和与奇数和
def sum_odd(start, end):
    start = int(start)
    end = int(end)
    sum_list = []
    for i in range(start, end+1, 1):
        if i%2 == 0:
            sum_list.append(i)
        sum_odd = sum(sum_list)
    return sum_odd

def sum_evan(start, end):
    start = int(start)
    end = int(end)
    sum_list = []
    for i in range(start, end+1, 1):
        if i%2 != 0:
            sum_list.append(i)
        sum_odd = sum(sum_list)
    return sum_odd

start = 1
end = 500
print(sum_odd(start, end))
print(sum_evan(start, end))
