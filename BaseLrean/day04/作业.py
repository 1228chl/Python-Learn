
# for i in range(3):
#     users = input("请输入用户名")
#     passwords = input("请输入密码")
#     if 0<= i < 3:
#         if users == 'admin' and passwords == 'admin888':
#             print("登录成功")
#             break
#         elif users != 'admin':
#             print("用户名错误")
#         elif passwords != 'admin888':
#             print("密码错误")
#     else:
#         print("尝试登录超过3次，请稍等再登！")
#         break

# # topic-1：使用while循环打印'hello python'50次
# i = 0
# while i < 50:
#     print("hello python")
#     i += 1

# # topic-：使用while循环打印1-100
# i = 1
# while i<=100:
#     print(i)
#     i = i+1

# # topic-3:使用while循环计算1 - 100 之间的累加和
# i=1
# sums = 0
# while i<=100:
#     sums += i
#     i+= 1
# print(sums)

# # topic-4:使用for循环计算1 - 100 之间的累加和
# sums= 0
# for i in range(1,101):
#     sums += i
# print(sums)

# # topic-5:要求用户输入一个字符串，遍历当前字符串并打印，如果遇见“q”,则终止循环
# s = input("please input a string:")
# for i in s:
#     if i == "q":
#         break
#     else:
#         print(i,end="")

# # topic-6:使用for循环计算100 - 999 之间的偶数的个数
# sums = 0
# for i in range(100,1000,2):
#     if i % 2 == 0:
#         sums += 1
# print(sums)

# # topic-7:要求用户输入一个字符串，遍历当前字符串并打印，如果遇见“e”,则终止循环。如果遇见` ' '`（空格）则跳过当前输出。
# s = input("please enter a string:")
# for i in s:
#     if i == "e":
#         break
#     elif i == " ":
#         continue
#     print(i,end="")

# # topic-8:编写代码模拟用户登陆。要求：用户名为 binzi，密码 123456，
# # 如果输入正确，打印“欢迎光临”，程序结束，如果输入错误，提示用户输入错误并重新输入
# username = "binzi"
# password = "123456"
#
# while True:
#     u = input("please input username:")
#     p = input("please input password:")
#     if u == username and p == password:
#         print("欢迎登录")
#         break
#     else:
#         print("输入错误，请重新输入：")

# '''
# topic-9:
# 编写程序,分别统计字母和数字的个数,具体效果如下:
# 请输入字符串:abc123def
# 结果如下:
# LETTERS:6
# DIGITS:3
# '''
#
# s = "abc123def"
# n = len(s)
# alpha_s = 0
# digit_s = 0
# other_s = 0
# for i in range(n):
#     if s[i].isalpha():
#         alpha_s += 1
#     elif s[i].isdigit():
#         digit_s += 1
#     else:
#         other_s += 1
# print(alpha_s, digit_s, other_s)


# '''
# topic-10:
# 编写一个接受句子的程序，并计算大写字母和小写字母的数量。 假设将以下输入提供给程序：
# 请输入字符串:ABC123DEF
# 结果如下:
# UPPER CASE:  6
# LOWER CASE:  0'''
#
# s = "ABC123DEF"
# n = len(s)
# upper_s = 0
# lower_s = 0
# other_s = 0
# for i in range(n):
#     if s[i].isupper():
#         upper_s += 1
#     elif s[i].islower():
#         lower_s += 1
#     else:
#         other_s += 1
# print(upper_s, lower_s, other_s)

# # topic-11:设计("过7游戏”程序,即在1- 99之间的数字中,如果数字包含7或者是7的倍数,则输出")过...",否则输出具体的数字.
# for i in range(1,100):
#     if i % 7 == 0 or i % 10 == 7 or i // 10 == 7:
#         print(i,"过。。。")
#     else:
#         print(i)

