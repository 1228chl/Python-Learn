"""
迭代器: 是python中的对象, 用于遍历数据, 一个一个进行访问  range()本质上就是一个迭代器
好处: 节省内存占用, 惰性计算(不用不生成,用时再生成)
创建迭代器流程:
1. __init__  初始化起始和结束
2. __iter__  返回迭代器对象本身 -> 实现遍历迭代器对象
3. __next__  判断是否当前值是否超过最大值  如果超过抛出停止迭代  否则保存当前值以及更新当前值

迭代器使用:
1. 遍历操作
2. next(迭代器对象)  ->  获取下一个值

注意点:
已生成的数据就会销毁, 不再生成
"""

# for i in range(1, 5):
#     print(i)


# 需求: 创建迭代器, 模拟range(1, 5) 操作

# todo:1- 创建迭代器类
class MyIteration():
    # todo:2- __init__
    def __init__(self, start, end):
        """
        :param start: 起始值, 当前输出的值
        :param end: 结束值
        """
        self.current_value = start
        self.end = end

    # todo:3- __iter__
    # 对象可迭代
    def __iter__(self):
        return self

    # todo:4- __next__
    def __next__(self):
        # 4.1 判断当前值是否超过最大值, 超过抛出异常
        if self.current_value >= self.end:
            raise StopIteration

        # 4.2 不超过, 保存当前值, 更新当前值
        # 方式一:
        # value = self.current_value
        # self.current_value += 1
        # return value

        # 方式二:
        self.current_value += 1
        return self.current_value - 1

class MyIterator():
    def __init__(self, start, end):
        self.current_value = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.current_value >= self.end:
            raise StopIteration
        self.current_value += 1
        return (self.current_value - 1) * 99


if __name__ == '__main__':
    # 创建迭代器对象
    my_iter1 = MyIteration(1, 5)

    # 调用next方法, 生成下一个值
    print(next(my_iter1))
    print(next(my_iter1))

    print('=' * 80)
    for i in my_iter1:
        print(i)

    # print(next(my_iter1))  # 会发生报错 StopIteration

    # 创建迭代器对象2
    my_iter2 = MyIteration(0, 10)
    print(next(my_iter2))
    for i in my_iter2:
        print(i)

    # 查看内存占用空间
    import sys

    # 创建迭代器对象3
    my_iter3 = MyIteration(0, 10000000)
    print('my_iter3--->', sys.getsizeof(my_iter3))
    print('my_iter2--->', sys.getsizeof(my_iter2))

    list1 = [i for i in range(10000000)]
    print('list1--->', sys.getsizeof(list1))

    for item in MyIterator(0,1000):
        print(item)