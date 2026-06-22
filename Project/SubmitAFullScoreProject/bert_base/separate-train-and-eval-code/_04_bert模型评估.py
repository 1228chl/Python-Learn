# 导包
import torch

from Project.SubmitAFullScoreProject.bert_base._01_config import Config
from Project.SubmitAFullScoreProject.bert_base._02_dataloader_utils import build_all_dataloader
from Project.SubmitAFullScoreProject.bert_base._03_bert_classifier_model import MyBertClassifier
from tqdm import tqdm
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# TODO 训练核心流程: 斌子法则 1212
# todo 1个配置文件
config = Config()


def model_eval():
    # todo 2个准备
    # 准备数据
    train_dataloader, dev_dataloader, test_dataloader = build_all_dataloader()
    # 准备模型
    my_bert_model = MyBertClassifier()
    my_bert_model.load_state_dict(torch.load(config.bert_classifier_model_save_path))
    my_bert_model.eval()
    with torch.no_grad():
        # 提前创建两个列表,用于存储所有的样本的预测和真实标签
        all_pred_labels, all_true_labels = [], []
        # todo 1个遍历
        # 内层循环控制批次
        for index, (batch_texts_tensor, batch_labels_tensor) in enumerate(tqdm(dev_dataloader), start=1):
            # todo 2个核心
            # 前向传播
            logits = my_bert_model(batch_texts_tensor)
            # 累加每批的预测标签和真实标签
            all_true_labels.extend(batch_labels_tensor.tolist())  # 累加真实的这批标签
            batch_pred_labels = torch.argmax(logits, dim=-1)  # 最大分数对应的索引就是预测的标签
            all_pred_labels.extend(batch_pred_labels.tolist())  # 累加预测的这批标签
        # 计算准确率,精确率,召回率,f1分数
        acc = accuracy_score(all_true_labels, all_pred_labels)
        pre = precision_score(all_true_labels, all_pred_labels, average='macro')
        rec = recall_score(all_true_labels, all_pred_labels, average='macro')
        f1 = f1_score(all_true_labels, all_pred_labels, average='macro')

        # todo 打印日志
        print(f"一次性评估阶段: 准确率:{acc},精确率:{pre},召回率:{rec},f1:{f1}")


if __name__ == '__main__':
    model_eval()
