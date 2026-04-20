"""
主进程默认等待子进程执行结束后再结束

如果实现主进程结束 子进程跟着结束?
① 守护主进程   daemon=True  推荐此方式
② 杀死子进程  子进程对象.terminate()
"""
import multiprocessing as mp
import time

# todo:1-任务1 给全局变量列表添加数据
def worker():
    for i in range(10):
        print(f'子进程{i}')
        time.sleep(0.2)

# todo:2-创建进程
if __name__ == '__main__':
    # 创建进程对象
    # 方式一：守护主进程 daemon = True
    # p = mp.Process(target=worker, daemon=True)
    p = mp.Process(target=worker)
    # p.daemon = True
    p.start()

    # 方式二：杀死子进程
    p.terminate()

    time.sleep(1)
    print('主进程运行结束')