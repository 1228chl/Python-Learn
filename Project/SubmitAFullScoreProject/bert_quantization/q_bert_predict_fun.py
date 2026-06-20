# 导包
from q_config import Config
from bert_classifier_model import MyBertClassifier
import torch

# todo 1.提前创建配置对象
config = Config()
# todo 2.加载模型
bert_model = MyBertClassifier()
# TODO 注意： 由于一会加载的是量化后的模型参数，所以当前新建的模型也要做量化
q_bert_model = torch.quantization.quantize_dynamic(model=bert_model,qconfig_spec={torch.nn.Linear},dtype=torch.qint8)
# TODO 保持新模型和量化后模型参数数据一致，再加载
q_bert_model.load_state_dict(torch.load(config.quantization_bert_model_save_path,map_location=config.device))

# todo 3.定义api接口
def predict_fun(data):
    # 获取文本
    text = data['text']
    # tokenizer特征处理
    text_tensor = config.bert_tokenizer(text,max_length=config.max_len,padding='max_length',truncation=True,return_tensors='pt')
    # 模型预测拿到样本对应10个分数
    logits = q_bert_model(text_tensor)
    # argmax()拿到最大分数对应的索引，就是预测标签索引
    y_pred_idx = torch.argmax(logits,dim=-1).item()
    # 根据索引获取类别名
    y_pred_class = config.id2class[y_pred_idx]
    # 拼接到data中返回
    data['predict_class'] = y_pred_class
    # 返回
    return data

if __name__ == '__main__':
    # 模拟准备json格式数据
    # text = '词汇阅读是关键 08年考研暑期英语复习全指南'
    text = input('请您输入一个新闻:')
    data = {"text": text}
    # TODO 模拟调用API
    result = predict_fun(data)
    print(result)  # {'text': '词汇阅读是关键 08年考研暑期英语复习全指南', 'predict_class': 'education'}
