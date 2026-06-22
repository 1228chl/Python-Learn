# 导包
import torch
from _01_q_config import Config

# todo 提前创建配置对象
config = Config()


# todo 加载原始数据
def load_data_list(base_path):
    """
    :param base_path: train.txt或者dev.txt或者test.txt的路径
    原始数据:  新闻\t标签\n新闻\t标签\n...
    :return: [(新闻,标签),(新闻,标签)...]
    """
    # 提前创建一个列表,用于存储(新闻,标签)元组
    data_list = []
    for line in open(base_path, 'r', encoding='utf8'):
        text, label_str = line.strip().split('\t')
        label = int(label_str)
        # 先封装成元组,再append到列表中
        data_list.append((text, label))
    # 返回结果
    return data_list


# todo 自定义dataset类: 1个继承3个重写
class MyDataSet(torch.utils.data.Dataset):
    def __init__(self, data_list):
        self.data_list = data_list

    def __len__(self):
        return len(self.data_list)

    def __getitem__(self, index):
        return self.data_list[index]


# todo 自定义collate_fn函数
def my_collate_fn(batch):
    """
    :param batch: 一批的[(新闻,标签),(新闻,标签)...]
    :return: 这一批的tokenizer处理后的特征数据和标签
    """
    # todo 单独获取这一批数据中的所有texts和labels
    # 方法1: 推导式
    # texts = [t[0] for t in batch]
    # labels = [t[1] for t in batch]
    # 方法2: zip
    texts, labels = zip(*batch)
    # todo 先把labels转换为张量
    batch_labels_tensor = torch.tensor(labels)
    # todo 再用tokenizer处理texts,最后转换为张量
    batch_texts_tensor = config.bert_tokenizer(texts, max_length=config.max_len, padding='max_length', truncation=True,
                                               return_tensors='pt')
    # todo 返回结果
    return batch_texts_tensor, batch_labels_tensor


def test_dataloader():
    data_list = load_data_list(config.test_path)  # 数据转换
    data_set = MyDataSet(data_list)  # __init__
    print(f"数据集条数:{len(data_set)}")  # 10000 底层调用了__len__
    # 封装dataloader
    dataloader = torch.utils.data.DataLoader(data_set, config.batch_size, shuffle=True, collate_fn=my_collate_fn)
    print(f"按照每批{config.batch_size}条,共分{len(dataloader)}批")  # len(data_set)/batch_size
    # TODO collate_fn调用时机: 是遍历dataloader的时候自动调用
    for batch_texts_tensor, batch_labels_tensor in dataloader:  # 底层调用了my_collate_fn,此处batch拿到my_collate_fn返回的数据
        print(f'tokenizer处理后特征:{batch_texts_tensor}')
        print(f"这一批特征对应的标签:{batch_labels_tensor}")
        # 拿着batch前向传播
        break


# TODO 提前构建训练/验证/测试3个dataloader
def build_all_dataloader():
    # 1.构建train_dataloader
    data_list = load_data_list(config.train_path)
    data_set = MyDataSet(data_list)
    train_dataloader = torch.utils.data.DataLoader(data_set, config.batch_size, shuffle=True, collate_fn=my_collate_fn)
    # 2.构建dev_dataloader
    data_list = load_data_list(config.dev_path)
    data_set = MyDataSet(data_list)
    dev_dataloader = torch.utils.data.DataLoader(data_set, config.batch_size, shuffle=False, collate_fn=my_collate_fn)
    # 3.构建test_dataloader
    data_list = load_data_list(config.test_path)
    data_set = MyDataSet(data_list)
    test_dataloader = torch.utils.data.DataLoader(data_set, config.batch_size, shuffle=False, collate_fn=my_collate_fn)
    # 4.返回
    return train_dataloader, dev_dataloader, test_dataloader


if __name__ == '__main__':
    train_dataloader, dev_dataloader, test_dataloader = build_all_dataloader()
    print(f"训练集按照每批{config.batch_size}条,一共{len(train_dataloader)}批")  # 64 2813
    print(f"验证集按照每批{config.batch_size}条,一共{len(dev_dataloader)}批")  # 64 157
    print(f"测试集按照每批{config.batch_size}条,一共{len(test_dataloader)}批")  # 64 157
