"""
特点1: 线程之间是无序的, 由CPU调度决定执行顺序, 谁先调度谁就先执行
特点2: 主线程默认等待子线程执行结束后再结束
如何实现主线程结束 子线程跟着结束?
主线程守护: daemon=True
特点3: 主线程和所有子线程共用一份数据, 引用赋值
进程不共享: 多个车间中设备资源互相独立
线程共享: 一个车间中多个员工, 多个员工可以使用车间中的设备资源
特点4: 线性共享全局变量 会导致 计算出错  CPU密集计算任务(算数任务, 机器学习(wx+b))
有一份题, 需要A学生进行解题操作 -> 计算任务
有一份体, 需要B学生复制N份出来 -> 不属于计算任务
"""

import threading

# todo:0- 初始化变量 值为0
result = 0


# todo:1- 任务1 累加1000000次
def func1():
    global result
    for i in range(1000000):
        result += 1
    print('func1--->', result)


# todo:2- 任务2 累加1000000次
def func2():
    global result
    for i in range(1000000):
        result += 1
    print('func2--->', result)


# todo:3- 创建线程对象
if __name__ == '__main__':
    t1 = threading.Thread(target=func1)
    t2 = threading.Thread(target=func2)

    t1.start()
    t2.start()

    print('主线程读取全局变量数据--->', result)
