# 导包
from q_config import Config
from dataloader_utils import build_all_dataloader
from bert_classifier_model import MyBertClassifier
from bert_model_eval_utils import model_eval
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
print('============================================开始量化======================================================')
# todo 4.动态量化核心思想：将线性层的权重从FP32实时转换为INT8进行计算，偏置依然保持FP32，激活值是后续在推理过程中仍是动态计算的
dq_bert_model = torch.quantization.quantize_dynamic(model=my_bert_model,qconfig_spec={torch.nn.Linear},dtype=torch.qint8)
print('============================================量化评估和保存======================================================')
# todo 5.量化后评估下模型
acc,pre,rec,f1 = model_eval(dev_dataloader,dq_bert_model)
print(f"准确率:{acc},精确率:{pre},召回率:{rec},f1:{f1}")
# todo 6.保存量化后的模型
torch.save(dq_bert_model.state_dict(),config.quantization_bert_model_save_path)
print('量化后模型保存成功')
