"""
不共享全局变量: 各进程会 对原数据 进行深拷贝, 各进程的数据独立存在
"""
import multiprocessing as mp
# todo：0-初始化全局变量空列表
list_data = []

# todo：1-任务1 给全局变量列表添加数据
def write_data():
    for i in range(5):
        list_data.append(i)
    print('write_data',list_data)

# todo：2-任务2 读取全局变量列表数据
def read_data():
    for i in ['tlp','bd','abm','xbs']:
        list_data.append(i)
    print('read_data',list_data)

# todo：3-创建进程
def main():
    # 创建进程对象
    p1 = mp.Process(target=write_data)
    p2 = mp.Process(target=read_data)
    # 启动进程
    p1.start()
    p2.start()

    list_data.append('lbs')
    print('主进程读取全局变量列表数据',list_data)

if __name__ == '__main__':
    main()