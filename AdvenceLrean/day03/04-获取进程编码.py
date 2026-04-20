"""
当前进程id: os.getpid() ->  process id 或者  multiprocessing.current_process().pid
父进程id: os.getppid() ->  parent process id  或者  multiprocessing.parent_process().pid

作用: 管理进程  查看父子进程的关系
"""
import multiprocessing
import time
import os

# 需求: 一边写代码, 一边听歌

# todo:1- 任务1 写代码函数
def coding():
    for i in range(10):
        print(i)
        time.sleep(0.2)
    # 获取子进程1的进程id和父进程id
    print(f'music进程的进程id是:{os.getpid(), multiprocessing.current_process().pid}, '
          f'\n父进程id是:{os.getppid(), multiprocessing.parent_process().pid}')

# todo:2- 任务2 听歌函数
def music():
    for i in range(10):
        print(i)
        time.sleep(0.2)
    # 获取子进程2的进程id和父进程id
    print(f'coding进程的进程id是:{os.getpid(), multiprocessing.current_process().pid}, '
          f'\n父进程id是:{os.getppid(), multiprocessing.parent_process().pid}')

# todo:3- 创建进程对象需要在 函数或方法或程序入口中 实现  主进程
if __name__ == '__main__':
    # target: 任务名称 接收的方法名或函数名
    # name: 进程名称, 可以不进行设置, 默认是从 Process-1开始, Process-2 ...
    p1 = multiprocessing.Process(target=coding, name='进程1')
    print('p1.name--->', p1.name)
    p2 = multiprocessing.Process(target=music)
    print('p2.name--->', p2.name)

    # todo:4- 启动进程对象
    p1.start()
    p2.start()

    # 获取主进程的进程di 和 父进程id
    # 父进程id 就是 运行的pycharm的进程id
    print(f'主进程的进程id是:{os.getpid()}, 父进程id是:{os.getppid()}')

    # 杀死主进程
    # os.kill(os.getpid(), 9)


