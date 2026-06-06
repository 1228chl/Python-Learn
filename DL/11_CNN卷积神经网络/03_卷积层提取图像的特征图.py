import numpy as np
import matplotlib.pyplot as plt
import torch

# 1. 加载图片
img_n1 = plt.imread('data/img.jpg')
print(type(img_n1),img_n1.shape)
# 2.把numpy(H,W,C)转换为张量(H,W,C)
img_t1 = torch.tensor(img_n1,dtype=torch.float32)
print(type(img_t1),img_t1.shape)
# 3.把张量转换为(N,C,H,W)转换成张量(N,C,H,W)
img_t2 = img_t1.permute(2,0,1).unsqueeze(0)
print(type(img_t2),img_t2.shape)#[1, 3, 640, 640]

print('*'*50)
# 4.创建卷积层
conv = torch.nn.Conv2d(in_channels=3,out_channels=4,kernel_size=3,stride=1,padding=1)

# 5.使用卷积层提取特征
map_img = conv(img_t2)
print(type(map_img),map_img.shape)
print('*'*50)
# 6.把张量(1,C,H,W)降维为张量(C,H,W),再交换为张量(H,W,C)
img_t3 = map_img.squeeze(0).permute(1,2,0)
print(type(img_t3),img_t3.shape)
# 7.把张量(H,W,C)转换为numpy(H,W,C)
img_n2 = img_t3.detach().numpy()
print(type(img_n2),img_n2.shape)
# 8.生成特征图
# 可以分别绘制0，1，2，3四个特征图
plt.imshow(img_n2[:,:,0])
plt.show()
plt.imshow(img_n2[:,:,1])
plt.show()
plt.imshow(img_n2[:,:,2])
plt.show()
plt.imshow(img_n2[:,:,3])
plt.show()

# # 将特征图转换为 NumPy 数组并移除批次维度
# feature_maps = map_img.squeeze(0).detach().cpu().numpy()  # 形状: (4, H, W)
#
# # 创建子图布局：1 行 4 列
# fig, axes = plt.subplots(1, 4, figsize=(12, 3))
#
# for i in range(4):
#     # 取出第 i 个特征图
#     fm = feature_maps[i]
#
#     # 归一化到 [0, 1] 范围，便于 imshow 显示
#     fm_min, fm_max = fm.min(), fm.max()
#     if fm_max - fm_min > 1e-8:
#         fm_norm = (fm - fm_min) / (fm_max - fm_min)
#     else:
#         fm_norm = fm - fm_min  # 避免除零，此时图像为纯色
#
#     # 显示特征图（使用灰度颜色映射）
#     axes[i].imshow(fm_norm,cmap='viridis')
#     axes[i].set_title(f'Feature Map {i + 1}')
#     axes[i].axis('off')
#
# plt.tight_layout()
# plt.show()