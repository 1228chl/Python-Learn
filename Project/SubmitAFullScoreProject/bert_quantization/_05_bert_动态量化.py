# 导包
from _01_config import Config
from _02_dataloader_utils import build_all_dataloader
from _03_bert_classifier_model import MyBertClassifier
from _04_bert_model_eval_utils import model_eval
import torch

# 提前加载配置文件
config = Config()
# todo 1.准备数据
train_dataloader, dev_dataloader, test_dataloader = build_all_dataloader()
# todo 2.准备模型 加载训练好的模型参数
my_bert_model = MyBertClassifier()
# todo 注意: 加载模型的时候,选择cpu方式
my_bert_model.load_state_dict(torch.load(config.bert_classifier_model_save_path, map_location=config.device))
# todo 注意: 模型放到指定设备上
my_bert_model.to(config.device)
# todo 3.提前评估下模型
acc, pre, rec, f1 = model_eval(dev_dataloader, my_bert_model)
print(f"准确率:{acc},精确率:{pre},召回率:{rec},f1:{f1}")
print('==============================================================================================================')