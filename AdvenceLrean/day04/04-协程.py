"""
协程三要素:
1. 定义异步函数: async def 函数名():
2. 执行处等待: await 任务
3. 启动程序: asyncio.run(函数名())

常见场景: 同时执行多个任务
await asyncio.gather(taskA(), taskB(), ...)
"""
import asyncio
import time


# todo:1- 定义异步函数
async def worker(name, delay):
    print(f'{name}开始执行..., 将耗时{delay}秒')
    # 模拟程序执行的过程, 执行时间
    await asyncio.sleep(delay)
    print(f'{name}执行完毕...')
    return f'{name}的结果'


# todo:2- 定义主函数, 并发执行多个任务
async def main():
    # 2.1 记录开始时间
    start = time.time()

    # 2.2 收集任务列表
    tasks = [worker('任务A', 2),
             worker('任务B', 1),
             worker('任务C', 3)]

    # 此操作是单个任务执行, 不是并发
    await worker('任务D', 4)
    await worker('任务E', 5)

    # 2.3 异步等待执行 -> 并发执行多个任务
    # *tasks -> 列表拆包操作
    # result = await asyncio.gather(*tasks)
    result = await asyncio.gather(worker('任务A', 2),
                                  worker('任务B', 1),
                                  worker('任务C', 3))
    print('结果:', result)
    print('耗时:', time.time() - start)


# todo:3- 启动主函数
if __name__ == '__main__':
    asyncio.run(main())
