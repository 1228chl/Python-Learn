"""
创建进程对象：
对象名 = multiprocessing.Process(target = ,name = ,args = () ,kwargs = {})
target:函数名/方法名
name：进程对象的名称，，可以不用写，默认是Process-1开始
args: 处理带参的任务, 接收元组类型
kwargs: 处理带参的任务, 接收字典类型  字典的key要和任务的形参名相同
"""
import time
from multiprocessing import Process


# 需求：一般写代码一边听歌，谁在写第几行代码，听第几首歌
# todo：1-任务1 写代码函数
def coding(name,num):
    for i in range(num):
        print(name,i)
        time.sleep(0.2)

# todo：2- 任务2 听音乐
def music(name,num):
    for i in range(num):
        print(name,i)
        time.sleep(0.2)

# todo：3- 程序入口 主进程
if __name__ == '__main__':
    # 3.1 创建子进程兑现
    #args：接收元组类型，（实参1，实参2）
    p1 = Process(target=coding,args=('老王',10))
    # kwwarge：接收字典类型，{”任务刑事案靠：实参值}
    p2 = Process(target=music,kwargs={'name':'特朗普','num':5})

    # 启动进程
    p1.start()
    p2.start()