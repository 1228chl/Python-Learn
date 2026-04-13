"""
增加元素的操作:
    1. li.append(元素)  在li列表的尾部追加1个元素
    2. li.extend(li2)  在li列表的尾部追加li2中的所有元素
    3. li.insert(索引, 元素)  在li列表的指定索引前插入1个元素
"""

# 定义一个li
li = [1, 2, 3, 4, 5]
print(li)

# 追加1个元素
temp = li.append(6)
print(li)  # list是可变类型, 追加元素都是在原列表上进行操作, 返回None
print(temp)

# 追加多个元素
li.extend([7, 8, 9])
print(li)

# 指定位置插入元素
li.insert(0, 0)
print(li)
li.insert(-1, -1)  # 注意是在指定的索引前面插入元素
print(li)
li.insert(len(li), -2)  # 在列表的末尾插入元素直接用append更方便
print(li)