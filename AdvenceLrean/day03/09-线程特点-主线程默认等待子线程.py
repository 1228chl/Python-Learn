"""
特点1: 线程之间是无序的, 由CPU调度决定执行顺序, 谁先调度谁就先执行
特点2: 主线程默认等待子线程执行结束后再结束
如何实现主线程结束 子线程跟着结束?
主线程守护: daemon=True
"""

import threading
import time


# todo:1- 任务1 定义工作函数
def work():
    for i in range(10):
        print(f'正在工作中...{i}')
        time.sleep(0.2)


if __name__ == '__main__':
    # todo:2- 创建线程对象, 执行任务1
    # t = threading.Thread(target=work, daemon=True)
    t = threading.Thread(target=work)
    t.daemon=True
    # t.setDaemon(True)

    # 启动线程
    t.start()

    time.sleep(1)
    print('主线程执行结束...')