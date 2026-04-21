"""
所有的生成器都是迭代器, 但是不是所有的迭代器都是生成器
生成器: 根据一定的规则来循环生成数据, 不需要手动管理条件以及状态
好处: 节省内存占用, 适用于大量数据的处理
其他操作和迭代器一样

创建生成器:
1. 生成器推导式  -> 生成器对象 = (i for i in range(num))
2. 借助yield关键字 -> yield i  创建生成器, 并且将数据保存到生成器中, 遍历时执行完yield后会等待
"""
import sys

# 列表推导式
list1 = [i for i in range(1000000)]
# print('list1--->', list1)
print('list1--->', sys.getsizeof(list1))

# 创建生成器对象
# 方式一: 生成器推导式
generator1 = (i for i in range(5))
print('generator1--->', type(generator1), '\n', generator1)
# 保存的是生成数据的规则, 不是数据本身
print('generator1--->', sys.getsizeof(generator1))
# 获取下一个值
print(next(generator1))
print(next(generator1))
for i in generator1:
    print(i)


# print(next(generator1))  # 会发生报错 StopIteration


# 方式二：借助yield关键字
def generator2(num):
    for i in range(num):
        print('开始生成数据...')
        yield i
        print('数据生成完毕...')

# 创建生成器对象2
g = generator2(5)
print('g--->', type(g), '\n', g)
print('g--->', sys.getsizeof(g))
print(next(g))
print(next(g))
for i in g:
    print(i)

# 创建生成器对象3
g3 = generator2(10)
for i in g3:
    print(i)
