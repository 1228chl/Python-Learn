"""
需求: 根据歌词文件, 一行就是一条样本, 生成指定批次的样本, 每批次的样本数可以自己定义
模拟后续深度学习中的dataloader生成器对象
"""
import math


# todo:1- 创建生成器函数
def data_loader(batch_size):
    # todo:2- 读取歌词文件数据, readlines
    with open('data/jaychou_lyrics.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()
        print('data--->', len(data), data[:10])

    # todo:3- 统计歌词文件中的行数 -> 样本数
    total_samples_num = len(data)
    print('total_samples_num--->', total_samples_num)

    # todo:4- 根据数据集样本数 和 批次样本数据 统计 批次数 -> 整份数据集可以生成多少批样本
    total_batchs_num = math.ceil(total_samples_num / batch_size)
    print('total_batchs_num--->', total_batchs_num)

    # todo:5- 循环遍历批次数生成当前批次的样本
    for batch_idx in range(total_batchs_num):
        print('当前批次:', batch_idx)

        # 列表切片操作
        # 第1批次: data[0: 3]
        # 第2批次: data[3: 6]
        # 第3批次: data[6: 9]
        # 以此类推: data[batch_idx * batch_size: (batch_idx + 1) * batch_size]
        yield data[batch_idx * batch_size: (batch_idx + 1) * batch_size]


if __name__ == '__main__':
    dataloader = data_loader(4)
    print(next(dataloader))
    print(next(dataloader))

    for i in dataloader:
        print(i)
