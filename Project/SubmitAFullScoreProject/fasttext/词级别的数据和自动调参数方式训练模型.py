# 导包
import fasttext
from config import Config

# 提前创建配置对象
config = Config()

# 1.模型训练
model = fasttext.train_supervised(input=config.process_train_path_words,
                                  autotuneValidationFile=config.process_dev_path_words,
                                  autotuneDuration=300,
                                  verbose=3)
# 2.模型保存
model.save_model(config.ft_word_auto_model_path)
print('模型保存成功!')
print('===============================================================================')
# 3.模型加载  此处不需要加载,因为在同一个文件中,一起运行的,直接可以评估
# fasttext.load_model(config.ft_word_auto_model_path)
# 4.模型评估
result = model.test(config.process_test_path_words)
# 打印结果                          (数据个数,精确率,召回率)
print(f"模型评估结果是:{result}")  # (10000, 0.9207, 0.9207)
print('===============================================================================')
# 5.模型预测
label = model.predict(['词汇 阅读 是 关键   08 年 考研 暑期 英语 复习 全 指南'])
print(f'模型预测结果是:{label}')  # (('__label__education',), array([1.0000093]))
