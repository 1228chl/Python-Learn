# 导包
import torch
from _01_d_config import Config

# 创建配置对象
config = Config()

# 自定义双向LSTM模型
# 一个继承
class MyBiLSTM(torch.nn.Module):
    # 两个重写
    def __init__(self):
        super().__init__()
        # 词嵌入层
        self.embedding = torch.nn.Embedding(num_embeddings=config.bert_config.vocab_size,
                                            embedding_dim=config.embed_size)
        # 定义双向LSTM循环层
        self.bilstm = torch.nn.LSTM(input_size=config.embed_size, hidden_size=config.hidden_size_lstm,
                                    num_layers=config.num_layers, batch_first=True, bidirectional=True)
        # 定义随机失活层
        self.dropout = torch.nn.Dropout(p=config.dropout_p)
        # bilstm输出双倍的hidden_size_lstm维度，不符合当前10分类,添加线性层转换,最终输出10维向量
        self.linear = torch.nn.Linear(config.hidden_size_lstm * 2, config.class_num)

    def forward(self, x):
        # 此处x包含；input_ids,token_type_ids,attention_mask三部分
        # todo 1.单独获取input_ids和attention_mask
        input_ids = x['input_ids']
        attention_mask = x['attention_mask']
        # todo 2.词嵌入层生成词向量
        # input_ids形状: [batch_size,seq_len]
        # all_embed:[batch_size,seq_len,embed_size]
        all_embed = embed = self.embedding(input_ids)
        # todo 3.因为lstm不需要bert的特殊字符,过滤：[CLS],[SEP],[PAD]词向量（本质都是置为0）
        cls_token_id = 101
        sep_token_id = 102
        # 拿到删除cls和sep的布尔张量
        drop_cls_sep_mask = (input_ids != cls_token_id) & (input_ids != sep_token_id)
        # 获取去除cls和sep以及pad后的注意力：删除cls和sep的布尔张量和attention_mask相乘获取新的掩码注意力
        valid_mask = drop_cls_sep_mask * attention_mask
        # 拿着整体词向量 和valid_mask,有效位置的保留原始词向量，无效位置改为0（cls和sep以及pad）
        valid_mask = valid_mask.unsqueeze(-1)
        valid_embed = all_embed * valid_mask

        # todo 4.双向LSTM开始前向传播
        # lstm_out形状：[batch_size,seq_len,hidden_size*2]
        lstm_out, _ = self.bilstm(valid_embed)

        # todo 5.平均池化，对整个句子有效字符进行平均池化
        # 先获取所有有效位的输出
        # valid_lstm_out形状：[batch_size,seq_len,hidden_size*2]
        valid_lstm_out = lstm_out * valid_mask

        # sum_hidden形状：[batch_size,hidden_size*2]
        # 求和
        sum_hidden = valid_lstm_out.sum(dim=1)
        # 求个数
        valid_token_cnt = valid_mask.sum(dim=1)
        # 平均池化
        avg_hidden = sum_hidden / valid_token_cnt

        # todo 6.随机失活层
        avg_hidden = self.dropout(avg_hidden)

        # todo 7.线性层
        logits = self.linear(avg_hidden)

        # 返回结果
        return logits

if __name__ == '__main__':
    mylstm = MyBiLSTM()
    print(mylstm)