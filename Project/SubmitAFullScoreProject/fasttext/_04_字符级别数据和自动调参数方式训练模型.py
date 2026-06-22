# 导包
import fasttext
from _01_config import Config

# 提前创建配置对象
config = Config()
# 1.模型训练
model = fasttext.train_supervised(
    input=config.process_train_path_chars,
    autotuneValidationFile=config.process_dev_path_chars,  # 自动调参文件
    autotuneDuration=300,  # 自动调参时间
    verbose=3)
# 2.模型保存
model.save_model(config.ft_char_auto_model_path)
print('模型保存成功!')
print('===============================================================================')
# 3.模型加载 此处不需要加载,因为在同一个文件中,一起运行的,直接可以评估
# fasttext.load_model(config.ft_char_auto_model_path)
# 4.模型评估
result = model.test(config.process_test_path_chars)
# 打印结果                          (数据个数,精确率,召回率)
print(f"模型评估结果是:{result}")  # (10000, 0.9202, 0.9202)
print('===============================================================================')
# 5.模型预测
label = model.predict(['词 汇 阅 读 是 关 键   0 8 年 考 研 暑 期 英 语 复 习 全 指 南'])
print(f'模型预测结果是:{label}')  # (('__label__education',), array([1.00001001]))
