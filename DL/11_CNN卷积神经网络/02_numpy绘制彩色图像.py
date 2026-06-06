import numpy as np
import matplotlib.pyplot as plt
# 由于我们自己无法想象彩色图像像素点，读取已经存在的

img_data = plt.imread('data/img.jpg')
print(img_data.shape)
plt.imshow(img_data)
plt.show()
img_data = np.random.randint(0,255,(64,64,3))
# 用读取出来的数据点重新绘制图像
plt.imshow(img_data)
plt.show()

