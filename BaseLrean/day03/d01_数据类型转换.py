"""
其他类型-->转字符串: str(变量)
       -->转int整型: int(变量)
       -->转浮点数: float(变量)
       -->字符串转为内部原生类型: eval(字符串)
"""

# name = input("请输入姓名: ")
# age = int(input("请输入年龄: "))
# height = float(input("请输入身高: "))
# num = int(input("请输入学号: "))
#
# # 打印用户输入的变量值类型
# # input接收的任何类型都会被转为字符串 赋值给变量
# print(type(name), type(age), type(height))
# # num = int(num)
# # print(type(num))
# # height = float(height)
# # print(type(height))
#
# print(f"姓名: {name}, 年龄: {age}, 身高: {height}")
# print(f"姓名: {name}, 学号: {num:06d}, 身高: {height:.2f}")  # %05d, %.2f
# # print(f"姓名: {name}, 学号: {int(num):06d}, 身高: {float(height):.2f}")  # %05d, %.2f

# 不是所有str都可以转int和 float
# a = "张三"
# float和int对str进行转换时, 字符串中必须包裹的就是int和 float类型才能正常转换
# float(a)
# int(a)

# int和float相互转换
a = 1.9
b = 10
print(int(a))  # int直接取整舍弃小数位
print(float(b))  # float是在int后面加 .0

# eval把str类型转为它包裹的内部类型(相当于对str脱皮, 暴露内部源数据)
c = "1.9"
d = "10"
print(eval(c))
print(eval(d))

