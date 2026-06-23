# 导包
import torch
from tqdm import tqdm

from _01_d_config import Config
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
# todo 训练核心流程：斌子法则 1211
# todo 1个配置文件
config = Config()

def model_eval(dev_dataloader,student_bilstm):
    # 准备模型
    student_bilstm.eval()
    with torch.no_grad():
        # 提前创建两个列表，用于存储所有的样本的预测标签和真实标签
        all_pred_labels, all_true_labels = [], []
        # todo 1个遍历
        for index, (batch_texts_tensor, batch_labels_tensor) in enumerate(tqdm(dev_dataloader), start=1):
            # TODO 把数据放到指定设备上
            batch_labels_tensor = batch_labels_tensor.to(config.device)
            batch_texts_tensor = {k: v.to(config.device) for k, v in batch_texts_tensor.items()}
            # todo 2个核心
            # 前向传播
            logits = student_bilstm(batch_texts_tensor)
            # 累加每批的预测标签和真实标签
            all_true_labels.extend(batch_labels_tensor.tolist())  # 累加真实的标签
            batch_pred_labels = torch.argmax(logits, dim=-1)  # 最大分数对应的索引就是预测的标签
            all_pred_labels.extend(batch_pred_labels.tolist())  # 累加预测的标签
            # 计算准确率，精确率，召回率，f1分数
            acc = accuracy_score(all_true_labels, all_pred_labels)
            pre = precision_score(all_true_labels, all_pred_labels, average='macro')
            rec = recall_score(all_true_labels, all_pred_labels, average='macro')
            f1 = f1_score(all_true_labels, all_pred_labels, average='macro')

    # todo 打印日志
    # print(f"准确率:{acc},精确率:{pre},召回率:{rec},f1:{f1}")
    return acc,pre,rec,f1