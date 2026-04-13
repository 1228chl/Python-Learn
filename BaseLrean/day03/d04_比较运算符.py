"""
比较运算符: ==, !=, >, <, >=, <=
    比较运算符的结果都是 bool 布尔值
逻辑运算符: and(与) or(或) not(非)
优先级: () > 算术运算符 > 比较运算符 > 逻辑运算符 > 赋值运算符
    (): 优先级最高, 赋值: 优先级最底
"""
num1 = 10
num2 = 20

print(num1 == num2)  # False
print(num1 != num2)  # True
print(num1 > num2)  # False
print(num1 < num2)  #  True
print(num1 >= num2)  #  False
print(num1 <= num2)  #  True


# 逻辑运算符
a = 1
b = 2
c = 3

# 运算计算效率
# and运算, 前面条件不满足, 后面条件不再计算
# or运算, 前面条件满足, 满足条件不再计算

# 需要两个条件都满足
print(a > b and b < c)  # False
# 需要两个条件有一个满足
print(a > b or b < c)  # True
print(not a > b)  # True