import fasttext
from _01_config import Config

# 提前创建配置对象
config = Config()
# 1.模型训练
model = fasttext.train_supervised(input=config.process_train_path_words,verbose=2)
# 2.模型保存
model.save_model(config.ft_word_default_model_path)
print('模型保存成功')
print('*'*90)
# 3.模型加载
# model = fasttext.load_model(config.ft_word_default_model_path)
# 4.模型评估
result = model.test(config.process_test_path_words)
# 打印结果
print(f'模型评估结果是：{result}')
print('*'*90)
# 5.模型预测
label = model.predict(['词 汇 阅 读 是 关 键    0 8 年 考 研 暑 期 英 语 复 习 指 南'])
print(f'模型预测结果是：{label}')
