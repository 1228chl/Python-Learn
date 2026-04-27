import numpy as np
from skimage.util import dtype

# todo:1-创建全0，或全1数组，或全指定指数组
# 创建全0数组
arr1 = np.zeros(shape=(2,3),dtype=int)
print('arr--->',arr1.shape,arr1.dtype)
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print('arr--->',arr.shape,arr1,arr.dtype)
# 模仿数组的形状和类型创建一个全0数组
arr2 = np.zeros_like(arr)
print('arr2--->',arr2.shape,arr2,arr2.dtype)

# 创建全1数组
arr3 = np.ones(shape=(3,5,6))
print('arr3--->',arr3.shape,arr3,arr3.dtype)

arr4 = np.ones_like(arr)
print('arr4--->',arr4.shape,arr4,arr4.dtype)

# 创建全是指定值的数组
arr5 = np.full(shape=(2,3),fill_value=10.)
print('arr5--->',arr5.shape,arr5,arr5.dtype)

arr6 = np.full_like(arr,fill_value=5)
print('arr6--->',arr6.shape,arr6,arr6.dtype)

# todo:2-从现有数组中创建新数组
arr = np.array([1,2,3,4])

# 创建副本数据，和原数组的内存地址不同
arr7 = np.array(arr)
print('arr7--->',arr7.shape,arr7,arr7.dtype)

# asarray：和原数组共享内存地址
arr8 = np.asarray(arr)
print('arr8--->',arr8.shape,arr8,arr8.dtype)

# 修改arr中的某个值
arr[0] = 100
print('arr--->',arr)
print('arr7--->',arr7)
print('arr8--->',arr8)


# todo：-3创建范围数组
# start:起始值
# stop：结束值
# num：数组中的元素个数
# endpoint：是否包含结束值
arr1 = np.linspace(0,10,11,True)
print('arr1--->',arr1,arr1.dtype)

# 等同于range
# 左闭右开
# step：步长，默认为1
arr2 = np.arange(0,10,1)
print('arr2--->',arr2,arr2.dtype)

# 生成等比数组
arr3 = np.logspace(0,2,3,base=10,endpoint=True,dtype=int)
# 10^0 10^1 10^2
print('arr3--->',arr3,arr3.dtype)


# todo:4-创建随机数组
# 随机小数
# 在[0,1)范围内生成随机小数
# 3，2指的是对应的维度
arr1 = np.random.rand(3,2)
print('arr1-->',arr1,arr1.dtype)

# 生成满足正太分布的随机数组，均值为0标准为1范围内生成
arr2 = np.random.randn(3,2)
print('arr2-->',arr2,arr2.dtype)

# 随机整数
# 在[low,high)范围内生成的整数
# size：数组的形状
arr3 = np.random.randint(0,10,size=(3,2,2))
print('arr3',arr3,arr3.dtype)