# # topic-1:
# # 1.需求:定义空列表:  列表名 = []   或者   列表名 = list()
# # 2.需求: 定义一个列表存储'张三','李四','王五'等多个学生姓名
# # 3.需求: 在所有姓名列表中找到下标索引为1的姓名
# # 4.需求: 在所有姓名列表中找到下标索引为-1的姓名
# # 5.需求: 在所有姓名列表中找到张三
#
# l = ['张三','李四','王五']
# print(l[1])
# print(l[-1])
# for i in l:
#     if i == "张三":
#         print(i)
# print(l.index("张三"))
#
# # topic-2:
# # 1.需求: 做核酸早上刚开始没有人排队(定义空列表)
# # 2.需求: 张三排队到末尾
# # 3.需求: 李四和王五夫妻俩一起排队到末尾
# # 4.需求: 赵六走关系需要插队到第一个位置
# # 5.需求: 删除第一个位置的元素
# # 6.需求: 移除做完核酸的张三
# # 7.需求: 清空列表中所有元素
#
# l = []
# l.append("张三")
# print(l)
# s = ["李四","王五"]
# l.extend(s)
# print(l)
# l.insert(0,"赵六")
# print(l)
# l.pop(0)
# print(l)
# l.remove("张三")
# print(l)
# l.clear()
# print(l)
#
# # topic-3:
# # 1.需求: 定义列表,已知数据['张三','李四','王五','张三']
# # 2.需求: 查询张三在列表中出现次数
# # 3.需求: 查询李四在列表中的下标索引
# # 4.需求: 查询names列表中有多少个元素
# l = ['张三','李四','王五','张三']
# l.count("张三")
# print(l)
# print(l.index("李四"))
# print(len(l))
#
# # topic-4:
# # 1.需求: 定义 空元组格式两种方式
# # 2.需求: 定义一个元组,存储'张三','李四','王五','张三'
# # 3.需求: 查询第一个位置的元素
# # 4.需求: 查询张三元素在元组中出现次数
# # 5.需求: 查询李四元素在元组中的下标索引
# # 6.需求: 查询names元组当前元素的个数
# s = tuple()
# print(s)
# s1 = ()
# print(s1)
# s2 = ('张三','李四','王五','张三')
# print(s2)
# print(s2[0])
# print(s2.count("张三"))
# print(s2.index("李四"))
# print(len(s2))
#
# # topic-5:
# # james有一个关于爬虫的项目，他需要在一个字符串中查找python这个关键字，
# # 当前他通过index()函数进行查找，虽然可以实现查找的需求，但是总会在
# # 没有查找到关键字的时候报错，为什么会报错，如何优化？
# i = "pytthon python"
# if "python" in i:
#     print(i.index("python"))
#
# # topic-6:
# # 1.需求: 定义字符串 存储 '你TMD哦'
# # 2.需求: 利用replace把TMD替换成挺萌的
# s = '你TMD哦'
# print(s.replace("TMD","挺萌的"))
#
# # topic-7:
# # 1.需求: 定义字符串'苹果,香蕉,橘子,橙子,榴莲'
# # 2.需求: 要求把所有水果分开单独放到一个容器中要求结果:['苹果', '香蕉', '橘子', '橙子', '榴莲']
# # 3.需求: 查看切割后容器类型
# # 4.需求: 使用切割后生成的列表
#
# s = '苹果,香蕉,橘子,橙子,榴莲'
# s1 = list(s.split(","))
# print(type(s.split(",")))
# print(s1)
#
# # topic-8
# # 1.请创建一个空集合set1
# # 2.给set1添加一个元素5
#
# set1 = set()
# set1.add(5)
# print(set1)
#
# # topic-9:
# # 编写一个程序，该程序从控制台接受一个逗号分隔的数字序列，并生成一个列表和一个包含每个数字的元组。
# # 假设向该程序提供了以下输入：34,67,55,33,12,98
# # 然后，输出应为：
# # ['34', '67', '55', '33', '12', '98']
# # ('34', '67', '55', '33', '12', '98')
# s = input()
# s1 = list(s.split(","))
# s2 = set(s1)
# print(s)
# print(s1)
# print(s2)
#
# # topic-10:
# # 编写一个程序，该程序接受一系列由'空格'分隔的单词作为输入，并在删除所有重复的单词并将其按 字母数字顺序排序后打印这些单词。
# # 假设将以下输入提供给程序：hello world and practice makes perfect and hello world again
# # 最终输出结果为: again and hello makes perfect practice world
#
# s = input("11:")
# s1 = list(s.split())
# s2 = set(s1)
# s3 = sorted(s2)
# for i in s3:
#     print(i, end=" ")
#
# # topic-11:
# # 给定一个列表，首先删除以s开头的元素，
# # 删除后，修改第一个元素为"joke"，
# # 并且把最后一个元素复制一份，放在joke的后边
# my_list = ["spring", "look", "strange", "curious", "black", "hope"]
#
# for i in my_list:
#     if i.startswith("s"):
#         my_list.remove(i)
# print(my_list)
# my_list[0] = "joke"
# print(my_list)
# my_list.insert(my_list.index("joke")+1,my_list[-1])
# print(my_list)

