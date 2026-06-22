from _03_bert_classifier_model import MyBertClassifier
from _01_d_config import Config
from _02_dataloader_utils import build_all_dataloader
import torch
from tqdm import tqdm
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
from _04_bert_model_eval_utils import model_eval
# todo 相比bert多了lstm模型

# TODO 训练核心流程：斌子法则
# todo 1个配置文件
config = Config()
# 模型训练API
def model_train():
    # todo 4个准备
    # 准备数据
    train_dataloader, dev_dataloader, test_dataloader = build_all_dataloader()
    # 模型准备
    my_bert_model = MyBertClassifier()
    # 准备损失函数
    loss_fn = torch.nn.CrossEntropyLoss(reduction='mean')
    # 准备优化器
    optimizer = torch.optim.AdamW(my_bert_model.parameters(),lr=config.lr,betas=(0.9,0.999))
    # TODO 提前定义best_score = 0
    best_f1_score = 0
    # todo 2个遍历
    # 外层循环控制轮次
    for epoch in range(1,config.epochs +1):
        # todo 额外添加日志变量 每10批打印损失，准确率，精确率，召回率，f1分数
        total_loss,batch_cnt = 0,0
        all_pred_labels,all_true_labels = [],[]
        # 内层循环控制批次
        for index,(batch_texts_tensor, batch_labels_tensor) in enumerate(tqdm(train_dataloader),start=1):
            # todo 5个核心
            # 前向传播
            logits = my_bert_model(batch_texts_tensor)
            # 计算损失
            loss = loss_fn(logits,batch_labels_tensor)
            # 梯度清零
            optimizer.zero_grad()
            # 反向传播
            loss.backward()
            # 参数更新
            optimizer.step()
            # todo 额外计算日志变量
            total_loss += loss.item()
            batch_cnt += 1
            all_true_labels.extend(batch_labels_tensor.tolist())
            batch_pred_labels = torch.argmax(logits,dim=1)
            all_pred_labels.extend(batch_pred_labels.tolist())
            # todo 额外打印日志 每10批打印损失，准确率，精确率，召回率，f1分数
            if index %10 == 0 or index == len(train_dataloader):
                # 计算准确率，精确率，召回率，f1分数
                acc = accuracy_score(all_true_labels,all_pred_labels)
                pre = precision_score(all_true_labels, all_pred_labels, average='macro')
                rec = recall_score(all_true_labels, all_pred_labels, average='macro')
                f1 = f1_score(all_true_labels, all_pred_labels, average='macro')
                # 计算损失
                loss = total_loss/batch_cnt
                # todo 打印日志
                print(f"当前轮次:{epoch},当前批次:{index},损失:{loss},准确率:{acc},精确率:{pre},召回率:{rec},f1:{f1}")
                # 清空日志变量
                total_loss,batch_cnt = 0,0
                all_true_labels,all_pred_labels = [],[]
            # todo 边训练边评估
            if index %100 == 0 or index == len(train_dataloader):
                # 调用model_eval()进行评估
                acc,pre,rec,f1 = model_eval(dev_dataloader,my_bert_model)
                # 一定记得把模型切换到训练模式
                my_bert_model.train()
                if f1 > best_f1_score:
                    # 记录当前最优分数
                    best_f1_score = f1
                    torch.save(my_bert_model.state_dict(),config.bert_classifier_model_save_path)
                    print(f"当前轮次:{epoch},当前批次:{index},损失:{loss},准确率:{acc},精确率:{pre},召回率:{rec},f1:{f1}")

    # todo 1个保存
    torch.save(my_bert_model.state_dict(),config.bert_classifier_model_save_path)

if __name__ == '__main__':
    model_train()