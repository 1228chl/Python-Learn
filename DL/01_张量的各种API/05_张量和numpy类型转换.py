# 导包
import numpy as np
import torch

# TODO numpy转换为张量
numpy_demo = np.array([1, 2, 3])
print(type(numpy_demo), numpy_demo)
# todo 1.from_numpy()  共享内存
t1 = torch.from_numpy(numpy_demo)
print(type(t1), t1)
numpy_demo[0] = 100
print(numpy_demo, t1)  # 两个都变化了
print('------------------------------------')
# todo 2.tensor()  不共享内存
t2 = torch.tensor(numpy_demo)
print(type(t2), t2)
numpy_demo[1] = 200
print(numpy_demo, t2)  # t2没有变化,说明没有共享内存

print('=========================================')

# TODO 张量转换为numpy
tensor_demo = torch.tensor([10, 20, 30])
print(type(tensor_demo), tensor_demo)
# todo 1.numpy()  共享内存
n1 = tensor_demo.numpy()
print(type(n1), n1)
tensor_demo[0] = 100
print(tensor_demo, n1)  # 两个都变化了
print('------------------------------------')
# todo 2.numpy().copy() 不共享内存
n2 = tensor_demo.numpy().copy()
print(type(n2), n2)
tensor_demo[1] = 200
print(tensor_demo, n2)
