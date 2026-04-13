# 定义一个二维数组
students = [
    ["张三","李四"],
    ["王五","赵六"],
    ["田七","钱八"]
]

# 便利整个列表，获取每个元素
for row in students:
    for item in row:
        print(item)

# 获取嵌套列表的一行
print(students[0])
print(students[1])
print(students[2])

# 获取每一个元素
print(students[0][0],students[0][1])
print(students[1][0],students[1][1])
print(students[2][0],students[2][1])