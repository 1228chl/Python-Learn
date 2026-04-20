"""
创建线程对象:
线程对象名 = threading.Thread(target=, args=(), kwargs={}, name=)
target: 任务名/函数名/方法名
args: 处理带参的任务, 接收元组
kwargs: 处理带参的任务, 接收字典   字典的key值要和任务的形参名相同

启动线程:
对象名.start()
"""
import threading
import time


# todo:1- 任务1 写代码函数
def coding():
    for i in range(10):
        print(f'正在写代码...{i}')
        time.sleep(0.2)


# todo:2- 任务2 听音乐函数  谁在听哪位歌手的第几首音乐
def music(name, singer, num):
    for i in range(num):
        print(f'{name}正在听{singer}的第{i}首音乐...')
        time.sleep(0.2)


# 主进程程序入口
if __name__ == '__main__':
    # todo:3- 创建线程对象
    # 3.1 创建线程对象
    # target: 函数名/方法名/任务名
    # name: 线程的名称, 可以不用写, 默认是从 Thread-1开始
    t1 = threading.Thread(target=coding, name='线程1')
    print('t1.name--->', t1.name)
    t2 = threading.Thread(target=music, args=('小明', '周杰伦'), kwargs={'num': 10})
    print('t2.name--->', t2.name)

    # 3.2 启动线程对象
    t1.start()
    t2.start()