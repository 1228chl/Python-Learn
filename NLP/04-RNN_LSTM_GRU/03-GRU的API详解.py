# 导包
import torch


# 1个样本,每个样本1个词,每个词6维->默认1层处理
def demo1_gru_api():
    # input(seq_len,batch_size,input_size)
    input = torch.randn(1, 1, 6)
    # hideen(number_layers,batch_size,hidden_size)
    h0 = torch.zeros(1, 1, 6)
    # 创建gru层
    my_gru = torch.nn.GRU(input_size=6, hidden_size=6, num_layers=1)
    # 前向传播
    output, hn = my_gru(input, h0)
    print(f"hn形状:{hn.shape},hn内容:\n{hn}")
    print(f"output形状:{output.shape},output内容:\n{output}")


# 1个样本,每个样本2个词,每个词6维->默认1层处理
def demo2_gru_api():
    # input(seq_len,batch_size,input_size)
    input = torch.randn(2, 1, 6)
    # hideen(number_layers,batch_size,hidden_size)
    h0 = torch.zeros(1, 1, 6)
    # 创建gru层
    my_gru = torch.nn.GRU(input_size=6, hidden_size=6, num_layers=1)
    # 前向传播
    output, hn = my_gru(input, h0)
    print(f"hn形状:{hn.shape},hn内容:\n{hn}")
    print(f"output形状:{output.shape},output内容:\n{output}")


# 2个样本,每个样本3个词,每个词6维->默认1层处理
def demo3_gru_api():
    # input(seq_len,batch_size,input_size)
    input = torch.randn(3, 2, 6)
    # hideen(number_layers,batch_size,hidden_size)
    h0 = torch.zeros(1, 2, 6)
    # 创建gru层
    my_gru = torch.nn.GRU(input_size=6, hidden_size=6, num_layers=1)
    # 前向传播
    output, hn = my_gru(input, h0)
    print(f"hn形状:{hn.shape},hn内容:\n{hn}")
    print(f"output形状:{output.shape},output内容:\n{output}")


# 3个样本,每个样本3个词,每个词6维->默认1层处理
def demo4_gru_api():
    # input(seq_len,batch_size,input_size)
    input = torch.randn(3, 3, 6)
    # hideen(number_layers,batch_size,hidden_size)
    h0 = torch.zeros(1, 3, 6)
    # 创建gru层
    my_gru = torch.nn.GRU(input_size=6, hidden_size=6, num_layers=1)
    # 前向传播
    output, hn = my_gru(input, h0)
    print(f"hn形状:{hn.shape},hn内容:\n{hn}")
    print(f"output形状:{output.shape},output内容:\n{output}")


# 3个样本,每个样本4个词,每个词6维->2层处理
def demo5_gru_api():
    # 提前设置随机种子
    torch.manual_seed(666)
    # input(seq_len,batch_size,input_size)
    input = torch.randn(4, 3, 6)
    # hideen(number_layers,batch_size,hidden_size)
    h0 = torch.zeros(2, 3, 6)
    # 创建gru层
    my_gru = torch.nn.GRU(input_size=6, hidden_size=6, num_layers=2)
    # 前向传播
    output, hn = my_gru(input, h0)
    print(f"hn形状:{hn.shape},hn内容:\n{hn}")
    print(f"output形状:{output.shape},output内容:\n{output}")


# 隐藏状态内容如果是全0,可以省略不写,底层自动生成
# 3个样本,每个样本4个词,每个词6维->2层处理
def demo6_gru_api():
    # 提前设置随机种子
    torch.manual_seed(666)
    # input(seq_len,batch_size,input_size)
    input = torch.randn(4, 3, 6)
    # hideen(number_layers,batch_size,hidden_size)
    # 创建gru层
    my_gru = torch.nn.GRU(input_size=6, hidden_size=6, num_layers=2)
    # 前向传播
    output, hn = my_gru(input)
    print(f"hn形状:{hn.shape},hn内容:\n{hn}")
    print(f"output形状:{output.shape},output内容:\n{output}")


# 可以手动设置batch_first=True,观察结果
# 3个样本,每个样本4个词,每个词6维->2层处理
def demo7_gru_api():
    # 提前设置随机种子
    torch.manual_seed(666)
    # input(batch_size,seq_len,input_size)
    input = torch.randn(3, 4, 6)
    # 创建gru层
    my_gru = torch.nn.GRU(input_size=6, hidden_size=6, num_layers=2, batch_first=True)
    # 前向传播
    output, hn = my_gru(input)
    print(f"hn形状:{hn.shape},hn内容:\n{hn}")
    print(f"output形状:{output.shape},output内容:\n{output}")


if __name__ == '__main__':
    # 1个样本,每个样本1个词,每个词6维->默认1层处理
    demo1_gru_api()
    # 1个样本,每个样本2个词,每个词6维->默认1层处理
    # demo2_gru_api()
    # 2个样本,每个样本3个词,每个词6维->默认1层处理
    # demo3_gru_api()
    # 3个样本,每个样本3个词,每个词6维->默认1层处理
    # demo4_gru_api()
    # 3个样本,每个样本4个词,每个词6维->2层处理
    # demo5_gru_api()
    print('==================================================')
    # 隐藏状态内容如果是全0,可以省略不写,底层自动生成
    # demo6_gru_api()
    print('==================================================')
    # 可以手动设置batch_first=True,观察结果
    # demo7_gru_api()
    print('==================================================')


