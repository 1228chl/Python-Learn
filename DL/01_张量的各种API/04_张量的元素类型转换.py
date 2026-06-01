# 导包
import torch

# 1.先创建张量
t = torch.tensor(data=[1, 2, 3])
print(t.dtype)
# 2.1 直接用byte()/short()/int()/long()/half()/float()/double()
print(t.byte())
print(t.short())
print(t.int())
print(t.long().dtype)
print(t.half())
print(t.float().dtype)
print(t.double())

print('=' * 80)

# 2.2 用type(手动指定类型)
print(t.type(torch.uint8))
print(t.type(torch.int16))
print(t.type(torch.int32))
print(t.type(torch.int64).dtype)
print(t.type(torch.float16))
print(t.type(torch.float32).dtype)
print(t.type(torch.float64))

print('=' * 80)

# 2.4 用to(手动指定类型)
print(t.to(torch.uint8))
print(t.to(torch.int16))
print(t.to(torch.int32))
print(t.to(torch.int64).dtype)
print(t.to(torch.float16))
print(t.to(torch.float32).dtype)
print(t.to(torch.float64))
