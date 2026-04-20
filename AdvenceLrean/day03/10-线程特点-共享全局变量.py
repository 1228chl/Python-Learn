"""
特点1: 线程之间是无序的, 由CPU调度决定执行顺序, 谁先调度谁就先执行
特点2: 主线程默认等待子线程执行结束后再结束
如何实现主线程结束 子线程跟着结束?
主线程守护: daemon=True
特点3: 主线程和所有子线程共用一份数据, 引用赋值
进程不共享: 多个车间中设备资源互相独立
线程共享: 一个车间中多个员工, 多个员工可以使用车间中的设备资源
"""

import threading
import time

# todo:0- 初始化全局变量 空列表
list_data = []


# todo:1- 任务1 定义写函数
def write_data():
    for i in range(5):
        list_data.append(i)
        time.sleep(1)

    print('write_data--->', list_data)


# todo:2- 任务2 定义读函数
def read_data():
    print('read_data--->', list_data)


# todo:3- 创建线程对象
if __name__ == '__main__':
    t1 = threading.Thread(target=write_data)
    t2 = threading.Thread(target=read_data)

    t1.start()
    t2.start()

    time.sleep(10)
    print('主线程读取全局变量列表数据--->', list_data)
