# # topic-1:
# # 现有字典dict1 = {'name':'chuanzhi','age':18}
# # 要求：
# # 1.使用循环将字典中所有的键输出到屏幕上
# # 2.使用循环将字典中所有的键输出到屏幕上
# # 3.使用循环将字典中所有的键值对输出到屏幕上
# # 输出方式：  name：chuanzhi
# # age :   18
# dict1 = {'name':'chuanzhi','age':18}
# print(dict1.keys())
# print(dict1.values())
# for i in dict1:
#     print(i,end=" : ")
#     print(dict1[i])

# # topic-2:
# # 有这样的一个列表
# # product=[
# # {"name":"电脑","price":7000},
# # {"name":"鼠标","price":30},
# # {"name":"usb电动小风扇","price":20},
# # {"name":"遮阳伞","price":50}
# # ]，然后小明一共有8000块钱，那么他能不能买下这所有商品？
# # 如果能，请输出“能”，否则输出“不能”
#
# product=[
# {"name":"电脑","price":7000},
# {"name":"鼠标","price":30},
# {"name":"usb电动小风扇","price":20},
# {"name":"遮阳伞","price":50}
# ]
# s = 8000
# for i in product:
#     for j in i.keys():
#         if j == "price":
#             s -= i.get(j)
# if s >= 0:
#     print("能")
# else:
#     print("不能")

# # topic-3:
# # 使用给定的整数n，编写程序以生成包含（i，ixi）的字典，该字典为1到n之间的整数（都包括在
# # 内）。然后程序应打印字典。假设向程序提供了以下输入：8
# # 然后，输出应为：{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#
# n = int(input("请输入一个数字"))
# d = {}
# for i in range(1,n+1):
#     d[i] = i*i
#
# print(d)