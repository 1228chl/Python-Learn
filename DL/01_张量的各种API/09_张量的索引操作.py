"""索引"""
# 导包
import torch

"""
二维张量格式：[行,列]
三维张量格式：[0轴索引,1轴索引,2轴索引]
索引的表现形式：单独索引,列表,切片,布尔索引
"""
# todo 1.二维张量索引
#提前设置种子
torch.manual_seed(666)
# 创建二维张量
t1 = torch.randint(1, 10, (4, 5))
print(t1)
print(t1[:,:])
#需求：获取第2行数据
print(t1[1,:])
#需求：获取第一行第三行数据
print(t1[[0,2],:])
#需求：获取前3行数据
print(t1[[0,1,2]])
#需求；获取小于5的数据
print(t1<5)
print(t1[t1<5])


# todo 2.三维张量索引
# 提前设置种子
torch.manual_seed(1)
# 创建二维张量
t2 = torch.randint(1, 10, size=(3, 4, 5))
print(t2)
print(t2[:, :, :])
# 获取0轴的第1个
print(t2[0, :, :])
# 获取1轴的第1个
print(t2[:, 0, :])
# 获取2轴的第1个
print(t2[:, :, 0])