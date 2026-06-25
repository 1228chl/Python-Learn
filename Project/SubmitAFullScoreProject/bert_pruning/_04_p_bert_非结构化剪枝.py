# 导包
from _01_p_config import Config
from _02_dataloader_utils import build_all_dataloader
from _03_bert_classifier_model import MyBertClassifier
from _04_bert_model_eval_utils import model_eval
import torch
import torch.nn.utils.prune as prune

# 提前加载配置对象
config = Config()


# 提前定义两个api工具,一个查看参数稀疏度(0占比),一个打印部分参数
def show_model_sparse(model):
    """
    :param model: 参数是bert模型
    :return: 返回bert模型中参数的稀疏度
    """
    # 获取当前模型的层数
    layer_num = len(model.bert.encoder.layer)
    print(layer_num)
    # 提前定义两个参数,记录0的总数量和总参数量
    zero_params_num = 0
    all_params_num = 0
    for i in range(layer_num):
        weight = model.bert.encoder.layer[i].attention.self.query.weight
        zero_params_num += torch.sum(weight == 0).item()
        all_params_num += weight.numel()  # 其中numel()自动计算每层的参数总量
    # 所有层的权重都统计完后计算稀疏度  可以使用三元运算符解决除0错误
    sparse = zero_params_num / all_params_num if all_params_num != 0 else 0
    return sparse


def print_sub_weight(model):
    sub_weight = model.bert.encoder.layer[0].attention.self.query.weight
    print(f"部分参数如下:\n{sub_weight[:5, :5]}")


if __name__ == '__main__':
    # todo 准备数据
    train_dataloader, dev_dataloader, test_dataloader = build_all_dataloader()
    # todo 准备模型  一定记得加载训练好的参数,并且放到指定设备上
    mybert = MyBertClassifier()
    mybert.load_state_dict(torch.load(config.bert_classifier_model_save_path))
    mybert.to(config.device)
    # todo 剪枝前查看模型稀疏度和部分参数以及评估操作
    # 查看模型稀疏度
    sparse = show_model_sparse(mybert)
    print(f"剪枝前模型稀疏度: {sparse}")
    # 查看部分参数
    print_sub_weight(mybert)
    # 剪枝前评估
    acc, pre, rec, f1 = model_eval(dev_dataloader, mybert)
    print(f"剪枝前模型准确率:{acc},精确率:{pre},召回率:{rec},f1:{f1}")
    print('====================================开始剪枝操作==========================================')
    # todo 开始对模型进行剪枝
    # 获取所有权重参数列表: 每层参数形状(网络层,参数名)
    all_prun_params = [(mybert.bert.encoder.layer[i].attention.self.query, 'weight') for i in
                       range(len(mybert.bert.encoder.layer))]
    # 剪枝: 根据用户指定的比例0.3和剪枝方法非结构化的L1对所有权重参数剪枝
    prune.global_unstructured(
        parameters=all_prun_params,
        pruning_method=prune.L1Unstructured,
        amount=0.3
    )
    # 固化剪枝
    for module,params_name in all_prun_params:
        prune.remove(module,params_name)
    print('====================================剪枝后评估操作=========================================')
    # todo 剪枝后查看模型稀疏度和部分参数以及评估操作
    # 查看模型稀疏度
    sparse = show_model_sparse(mybert)
    print(f"剪枝前模型稀疏度: {sparse}")
    # 查看部分参数
    print_sub_weight(mybert)
    # 剪枝前评估
    acc, pre, rec, f1 = model_eval(dev_dataloader, mybert)
    print(f"剪枝前模型准确率:{acc},精确率:{pre},召回率:{rec},f1:{f1}")
    print('====================================保存剪枝后模型=========================================')
    # todo 保存模型
    torch.save(mybert.state_dict(),config.pruning_bert_model_save_path)

