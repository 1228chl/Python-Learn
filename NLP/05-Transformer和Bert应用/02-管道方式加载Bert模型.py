# 导包
import transformers
import numpy as np

# 加载本地bert模型
model = transformers.pipeline(task='feature-extraction',model='bert-base-chinese')

# 准备测试数据
text = '黑马程序员'
#  使用bert模型
result = model(text)
# print(result)
print(np.array(result).shape)# (1, 7, 768)

# 黑马程序员 -> [CLS] 黑马程序员 [SEP] -> 每个词对应768维向量



