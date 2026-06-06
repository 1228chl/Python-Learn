import numpy as np
import matplotlib.pyplot as plt
import matplotlib

img_data = np.zeros([10,10,3])
print(img_data)
plt.imshow(img_data)
plt.show()

print("*"*60)
img_data = np.full([10,10,3],fill_value=255)
print(img_data)
plt.imshow(img_data)
plt.show()
