"""
创建进程对象:
对象名 = multiprocessing.Process(target=, name=, args=(), kwargs={})

启动进程:
对象名.start()
"""
import multiprocessing
import time


# 需求: 一边写代码, 一边听歌

# todo:1- 任务1 写代码函数
def coding():
    for i in range(10):
        print(f'正在写代码...{i}')
        time.sleep(0.2)


# todo:2- 任务2 听歌函数
def music():
    for i in range(10):
        print(f'正在听歌...{i}')
        time.sleep(0.2)


# def main():
#     p1 = multiprocessing.Process(target=coding, name='进程1')
#     print('p1.name--->', p1.name)
#     p2 = multiprocessing.Process(target=music)
#     print('p2.name--->', p2.name)
#
#     # todo:4- 启动进程对象
#     p1.start()
#     p2.start()

# todo:3- 创建进程对象需要在 函数或方法或程序入口中 实现
if __name__ == '__main__':
    # main()

    # target: 任务名称 接收的方法名或函数名
    # name: 进程名称, 可以不进行设置, 默认是从 Process-1开始, Process-2 ...
    p1 = multiprocessing.Process(target=coding, name='进程1')
    print('p1.name--->', p1.name)
    p2 = multiprocessing.Process(target=music)
    print('p2.name--->', p2.name)

    # todo:4- 启动进程对象
    p1.start()
    p2.start()
