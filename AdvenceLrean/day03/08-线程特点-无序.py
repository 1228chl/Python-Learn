"""
特点1: 线程之间是无序的, 由CPU调度决定执行顺序, 谁先调度谁就先执行
"""
import time
import threading


# todo:1-任务1 定义工作函数，查看线性信息
def work():
    # 添加等待时间
    time.sleep(1)
    thread_info = threading.current_thread()
    print('线程信息',thread_info)

# todo:2-创建10个线程对象，执行任务1
if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=work)
        #启动线程
        t.start()
