# 导包
from _01_d_config import Config
from _03_d_bilstm_classifier_model import MyBiLSTM
import torch

# todo 1.提前创建配置对象
config = Config()
# TODO 2.加载模型  此处修改为蒸馏后的模型
student_bilstm = MyBiLSTM()
student_bilstm.load_state_dict(torch.load(config.distill_bilstm_save_path))


# todo 3.定义api接口
def predict_fun(data):
    # 获取文本
    text = data['test']
    # tokenizer特征处理
    text_tensor = config.bert_tokenizer(text, max_length=config.max_len, padding='max_length', truncation=True,
                                               return_tensors='pt')
    # 模型预测拿到样本对应10个分数
    logits = student_bilstm(text_tensor)
    # argmax()拿到最大分数对应的索引,就是预测标签索引
    y_pred_idx = torch.argmax(logits,dim=-1).item()
    # 根据索引获取类别名
    y_pred_class = config.id2class[y_pred_idx]
    # 拼接到data中返回
    data['predict_class'] = y_pred_class
    # 返回
    return data


if __name__ == '__main__':
    # 模拟准备json格式数据
    # test = '词汇阅读是关键 08年考研暑期英语复习全指南'
    text = input('请您输入一个新闻:')
    data = {"test": text}
    # TODO 模拟调用API
    result = predict_fun(data)
    print(result) # {'test': '词汇阅读是关键 08年考研暑期英语复习全指南', 'predict_class': 'education'}
