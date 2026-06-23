from _03_bert_classifier_model import MyBertClassifier
from _01_d_config import Config
from _02_dataloader_utils import build_all_dataloader
import torch
from tqdm import tqdm
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
from _04_bert_model_eval_utils import model_eval
# TODO 1.相比bert多了lstm模型和F函数
from _03_d_bilstm_classifier_model import MyBiLSTM
import torch.nn.functional as f

# 训练核心流程：斌子法则 14251
# 1个配置文件
config = Config()

# print present working device
print(f'当前运行的设备是:{config.device}')

# if is cuda ,demand model and data by to(device) put gpu device.
# 模型训练API
def model_train():
    # 4个准备
    # 准备数据
    train_dataloader, dev_dataloader, test_dataloader = build_all_dataloader()

    # 模型准备
    my_bert_model = MyBertClassifier()

    # TODO 2.bert模型作为教师模型：加载训练好参数并修改为评估模式
    my_bert_model.load_state_dict(torch.load(config.bert_classifier_model_save_path))

    my_bert_model.to(config.device)
    my_bert_model.eval()

    # TODO 3.新增bilstm学生模型，并设置为训练模式
    student_bilstm = MyBiLSTM()
    student_bilstm.to(config.device)
    student_bilstm.train()

    # 准备损失函数
    loss_fn = torch.nn.CrossEntropyLoss(reduction='mean')

    # TODO 4.优化器中修改为学生模型，学习率也要修改为学生模型的学习率
    optimizer = torch.optim.AdamW(student_bilstm.parameters(),lr=config.lstm_lr,betas=(0.9,0.999))

    # 提前定义best_score，初始为0
    best_f1_score = 0

    # 2个遍历
    # 外层循环控制轮次
    for epoch in range(1,config.epochs +1):
        # 额外添加日志变量 每10批打印损失，准确率，精确率，召回率，f1分数
        total_loss,batch_cnt = 0,0
        all_pred_labels,all_true_labels = [],[]

        # 内层循环控制批次
        for index,(batch_texts_tensor, batch_labels_tensor) in enumerate(tqdm(train_dataloader),start=1):
            # 把数据放到指定设备上
            batch_labels_tensor = batch_labels_tensor.to(config.device)
            batch_texts_tensor = {k: v.to(config.device) for k, v in batch_texts_tensor.items()}

            # 5个核心
            # TODO 4.修改前向传播为学生模型，老师模型不需要更新梯度
            student_logits = student_bilstm(batch_texts_tensor)
            with torch.no_grad():
                teacher_logits = my_bert_model(batch_texts_tensor)
                # teacher_labels = torch.argmax(teacher_logits,dim=-1)

            # TODO 5.修改损失计算方式
            # todo 5.1修改计算交叉熵损失
            hard_loss = loss_fn(student_logits,batch_labels_tensor)
            # hard_loss = loss_fn(student_logits, teacher_labels)

            # todo 5.2新增计算KL损失
            teacher_probs = f.log_softmax(teacher_logits / config.T, dim=-1)
            student_probs = f.log_softmax(student_logits / config.T, dim=-1)
            kl_loss = f.kl_div(student_probs, teacher_probs, reduction='batchmean', log_target=True)

            # todo 5.3合并kl损失和交叉熵损失
            loss = config.alpha * hard_loss + (1-config.alpha) * (kl_loss * (config.T * config.T))

            # 梯度清零
            optimizer.zero_grad()

            # 反向传播
            loss.backward()

            # 梯度裁剪
            torch.nn.utils.clip_grad_norm_(student_bilstm.parameters(), max_norm=1.0)

            # 参数更新
            optimizer.step()



            # todo 额外计算日志变量
            total_loss += loss.item()

            # todo 6.TODO 标签都通过.cpu().tolist()转换,同时argmax()一定改为学生预测分数
            batch_cnt += 1
            all_true_labels.extend(batch_labels_tensor.cpu().tolist())
            batch_pred_labels = torch.argmax(student_logits,dim=-1)
            all_pred_labels.extend(batch_pred_labels.cpu().tolist())

            # 额外打印日志 每10批打印损失，准确率，精确率，召回率，f1分数
            if index %10 == 0 or index == len(train_dataloader):
                # 计算准确率，精确率，召回率，f1分数
                acc = accuracy_score(all_true_labels,all_pred_labels)
                pre = precision_score(all_true_labels, all_pred_labels, average='macro')
                rec = recall_score(all_true_labels, all_pred_labels, average='macro')
                f1 = f1_score(all_true_labels, all_pred_labels, average='macro')

                # 计算损失
                loss = total_loss/batch_cnt

                # 打印日志
                print(f"当前轮次:{epoch},当前批次:{index},损失:{loss},准确率:{acc},精确率:{pre},召回率:{rec},f1:{f1}")

                # 清空日志变量
                total_loss,batch_cnt = 0,0
                all_true_labels,all_pred_labels = [],[]

            # 边训练边评估 每100批,评估一次,如果当前分数高于历史最高分,记录并保存
            if index %100 == 0 or index == len(train_dataloader):
                # 调用model_eval()进行评估
                # TODO 7.后续所有评估和保存都修改为学生模型
                acc,pre,rec,f1 = model_eval(dev_dataloader,student_bilstm)
                print(
                    f"评估日志: 轮次:{epoch},当前批次:{index},损失:{loss},准确率:{acc},精确率:{pre},召回率:{rec},f1:{f1}")

                # 一定记得把模型切换到训练模式
                student_bilstm.train()

                # 判断当前评估分数是否是最优分数,如果是就记录并保存
                if f1 > best_f1_score:
                    # 记录当前最优分数
                    best_f1_score = f1

                    # 1个保存
                    torch.save(student_bilstm.state_dict(),config.distill_bilstm_save_path)
                    print(f"保存当前最优分数:{f1}的模型")

if __name__ == '__main__':
    model_train()