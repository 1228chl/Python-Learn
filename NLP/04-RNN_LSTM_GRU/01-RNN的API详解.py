# 导包
import torch

# 1个样本，每个样本1个词，每个词6维-> 默认1层处理
def demo1_rnn_api():
    # input(seq_len,batch_size,input_size)
    input = torch.randn(1,1,6)
    # hidden(number_lagers,batch_size,hidden_size)
    h0 = torch.zeros(1,1,6)
    # 创建rnn层
    my_rnn = torch.nn.RNN(input_size=6,hidden_size=6,num_layers=1)
    # 前向传播
    output,hn = my_rnn(input,h0)
    print(f"hn形状：{hn.shape},内容：{hn}")
    print(f"output形状：{output.shape},内容：{output}")


# 1个样本，每个样本2个词，每个词6维-> 默认1层处理
def demo2_rnn_api():
    # input(seq_len,batch_size,input_size)
    input = torch.randn(2, 1, 6)
    # hidden(number_lagers,batch_size,hidden_size)
    h0 = torch.zeros(1, 1, 6)
    # 创建rnn层
    my_rnn = torch.nn.RNN(input_size=6, hidden_size=6, num_layers=1)
    # 前向传播
    output, hn = my_rnn(input, h0)
    print(f"hn形状：{hn.shape},内容：{hn}")
    print(f"output形状：{output.shape},内容：{output}")



# 2个样本，每个样本3个词，每个词6维-> 默认1层处理
def demo3_rnn_api():
    # input(seq_len,batch_size,input_size)
    input = torch.randn(3, 2, 6)
    # hidden(number_lagers,batch_size,hidden_size)
    h0 = torch.zeros(1, 2, 6)
    # 创建rnn层
    my_rnn = torch.nn.RNN(input_size=6, hidden_size=6, num_layers=1)
    # 前向传播
    output, hn = my_rnn(input, h0)
    print(f"hn形状：{hn.shape},内容：{hn}")
    print(f"output形状：{output.shape},内容：{output}")



# 3个样本，每个样本4个词，每个词6维-> 默认2层处理
def demo4_rnn_api():
    # input(seq_len,batch_size,input_size)
    input = torch.randn(4, 3, 6)
    # hidden(number_lagers,batch_size,hidden_size)
    h0 = torch.zeros(2, 3, 6)
    # 创建rnn层
    my_rnn = torch.nn.RNN(input_size=6, hidden_size=6, num_layers=2)
    # 前向传播
    output, hn = my_rnn(input, h0)
    print(f"hn形状：{hn.shape},内容：{hn}")
    print(f"output形状：{output.shape},内容：{output}")



if __name__ == '__main__':
    # 1个样本，每个样本1个词，每个词6维-> 默认1层处理
    demo1_rnn_api()
    print("*"*100)
    # 2个样本，每个样本3个词，每个词6维-> 默认1层处理
    demo2_rnn_api()
    print("*"*100)
    # 3个样本，每个样本3个词，每个词6维-> 默认1层处理
    demo3_rnn_api()
    print("*"*100)
    # 3个样本，每个样本4个词，每个词6维-> 默认2层处理
    demo4_rnn_api()
    print("*"*100)
