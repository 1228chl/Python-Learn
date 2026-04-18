"""
带参数的装饰器 也可以叫做 装饰器函数工厂(生成装饰器)
在装饰器函数基础上包裹一层函数(可以接收任意参数), 用于生成装饰器函数
"""

import time
import random


def reset_on_failure(max_retries=3, delay=1):
    """
    装饰器：函数执行失败时重置状态并重试

    Args:
        max_retries (int): 最大重试次数，默认为3
        delay (int/float): 每次重试之间的等待时间（秒），默认为1

    Returns:
        function: 装饰器函数
    """

    def decorator(func):
        """
        内部装饰器函数，用于接收被装饰的函数

        Args:
            func: 被装饰的目标函数

        Returns:
            function: 包装后的函数
        """

        def wrapper(*args, **kwargs):
            """
            包装函数，实现重试逻辑

            Args:
                *args: 位置参数
                **kwargs: 关键字参数

            Returns:
                目标函数的返回值

            Raises:
                Exception: 当达到最大重试次数仍失败时，抛出最后一次异常
            """
            # 遍历重试次数，从1到max_retries
            for attempt in range(1, max_retries + 1):
                try:
                    # 打印当前尝试次数
                    print(f"[尝试 {attempt}/{max_retries}] ", end='')
                    # 执行目标函数并返回结果
                    return func(*args, **kwargs)
                except Exception as e:
                    # 捕获异常并打印错误信息
                    print(f"失败: {e}")

                    # 如果还有重试机会
                    if attempt < max_retries:
                        # 打印等待信息并暂停指定时间
                        print(f"{delay}秒后重试...")
                        time.sleep(delay)
                    else:
                        # 已达到最大重试次数，打印最终失败信息并重新抛出异常
                        print(f"已达最大重试次数({max_retries})，操作失败")
                        raise

        # 返回包装函数
        return wrapper

    # 返回装饰器函数
    return decorator


@reset_on_failure(max_retries=3, delay=1)
def unstable_api_call():
    """
    模拟不稳定的 API 调用

    该函数有60%的概率抛出连接超时异常，用于测试重试机制

    Returns:
        dict: 包含状态和数据的字典，例如 {"status": "success", "data": "订单信息"}

    Raises:
        ConnectionError: 当模拟网络超时时抛出
    """

    # 生成0-1之间的随机数，如果小于0.6则模拟网络超时
    if random.random() < 0.6:
        raise ConnectionError("网络连接超时")

    # 模拟API调用成功
    print("API 调用成功！")
    return {"status": "success", "data": "订单信息"}


if __name__ == "__main__":
    # 主程序入口，测试不稳定API调用的重试机制
    result = unstable_api_call()
    print(f"结果: {result}\n")