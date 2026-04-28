"""
将原数组的形状修改为满足要求的形状
eg: 模型预测/推理时要求 数据集是二维数据, 一条数据[1,2,3,4]是一维数据,  此时需要将 [1,2,3,4] 变形为 [[1,2,3,4]] 二维数据集
"""
import numpy as np

# 创建数组
# 形状 (6,)
arr1 = np.array([1, 2, 3, 4, 5, 6])
print('arr1--->', arr1.shape)

# reshape(): 修改后数组的元素个数要和原数组一致  ※※※
# 将arr1的形状修改为(1, 6)
# new_arr1 = np.reshape(arr1, shape=(1, 6))
new_arr1 = np.reshape(arr1, shape=(1, -1))
print('new_arr1--->', new_arr1.shape, new_arr1)
# 将arr2的形状修改为(2, 3)
new_arr2 = arr1.reshape((2, 3))
print('new_arr2--->', new_arr2.shape, new_arr2)
# -1: 未知数x, 会自动计算-1的维度值  3*x=6  x=2
new_arr3 = arr1.reshape((3, -1))
print('new_arr3--->', new_arr3.shape, new_arr3)

print('=' * 80)

# resize(): 不要求修改后的数组元素个数和原数组一致
new_arr4 = np.resize(arr1, new_shape=(1, 6))
print('new_arr4--->', new_arr4.shape, new_arr4)
new_arr5 = np.resize(arr1, new_shape=(2, 4))
# new_arr5 = np.resize(arr1, new_shape=(2, 2))
print('new_arr5--->', new_arr5.shape, new_arr5)

print('=' * 80)

# arr.T -> 转置, 一般针对二维数组, 行变列, 列变行
# 形状 (2, 3)
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print('arr--->', arr.shape, arr)
# 形状 (3,2)
new_arr4 = arr.T
print('new_arr4--->', new_arr4.shape, new_arr4)
