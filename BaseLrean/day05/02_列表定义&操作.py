li = ["张三","李四","王五","张三"]
print(li)
print(type(li))
#创建空列表
temp_li = []
print(temp_li)
print(type(temp_li))
temp_li = list()
print(temp_li)
print(type(temp_li))

# 列表查询
# len(迭代对象) 查看对象的长度（元素的个数）
print(len(li))
# 列表索引
print(li[0])
print(li[-1])
# list split
print(li[0:3])
print(li[::-1])

# 内置查看方法
print(li.index("张三"))
print(li.count("张三"))
print("z" in li)
print("z" not in li)
