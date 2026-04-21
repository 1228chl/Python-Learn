import multiprocessing as mp
import time


def coding():
    time.sleep(1)
    print('coding')


def music():
    time.sleep(3)
    print('music')


def talk():
    time.sleep(2)
    print('talk')

if __name__ == '__main__':
    p = mp.Process(target=coding)
    p.start()
    p1 = mp.Process(target=music)
    p1.start()
    p2 = mp.Process(target=talk)
    p2.start()