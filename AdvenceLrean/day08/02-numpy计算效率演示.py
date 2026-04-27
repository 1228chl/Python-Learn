import random
import time
import numpy as np

a = []
for i in range(100000000):
    a.append(random.random())

print('列表运算...')
start_time = time.time()
sum1 = sum(a)
print("python sum: %s" % (time.time() - start_time))

print('=' * 80)

print('numpy数组运算...')
b = np.array(a)
start_time = time.time()
sum2 = np.sum(b)
print("numpy sum: %s" % (time.time() - start_time))
