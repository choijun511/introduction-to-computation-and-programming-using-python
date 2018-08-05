# 假设s是包含多个小数的字符串，由逗号隔开，如：‘1.23,2.4,3.123’。编写一个程序，输出s中所有数值的和。

s = '1.23,2.4,3.123'

s = s + ','
temporary = ''
num = []

for x in s:
    if x != ',':
        temporary = temporary + x
    else:
         num.append(temporary)
         temporary = ''

print(max(num))
