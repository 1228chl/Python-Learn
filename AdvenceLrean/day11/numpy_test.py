import numpy as np

#创建一个 5×5 的二维数组，边界值为 1，内部值为 0。
# # 方式一
# arr = np.ones((5,5),dtype=int)
# arr[1:-1,1:-1] = 0
# print(arr)
#
# # 方式二
# core = np.zeros((3,3),dtype=int)
# arr = np.pad(core,pad_width=1,constant_values=1)
# print(arr)

# 从 5×5 的 1~25 数组中提取中心 3×3 子数组。
# arr = np.arange(1,26).reshape(5,5)
# center = arr[1:4,1:4]
# print(center)

# 筛选分数 ≥90 并计算平均值。
# scores = np.array([85,92,78,90,88,76,95,89])
# high_scores = scores[scores >= 90]
# mean_high = high_scores.mean()
# print(high_scores)
# print(mean_high)

# 将 (6,) 数组变换为 (2,3) → (3,2) → 恢复 (6,)。
# a = np.arange(6)
# print(a)
# b = a.reshape(2,3)
# print(b)
# c = b.reshape(3,2)
# print(c)
# d = c.ravel()
# print(d)


# 计算形状 (2,3) 和 (3,) 的数组相加。
# a = np.array([[1,2,3],[4,5,6]])
# b = np.array([10,20,30])
# result = a + b
# print(result)


# 生成 4×4 随机整数 [0,100]，求每行最大值、每列最小值、整体标准差。
np.random.seed(0)
mat = np.random.randint(0,101,size=(4,4))
print('矩阵：\n',mat)

row_max = mat.max(axis=1)
col_min = mat.min(axis=0)
std_all = mat.std()

print('每行最大值：',row_max)
print('每行最小值',col_min)
print('整体标准差',std_all)


data = [1,2,3]
a = np.array(data)
b = a[:]
c = a.view()
d = np.asarray(a)
e = a.copy()
f = np.array(a)

a[0] = 100

print(a[0])
print(b[0])
print(c[0])
print(d[0])
print(e[0])
print(f[0])