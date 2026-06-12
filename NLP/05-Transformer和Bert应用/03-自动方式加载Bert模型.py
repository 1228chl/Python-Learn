# 导包
import transformers

# 加载bert模型（tokenizer和model）
my_tokenizer = transformers.AutoTokenizer.from_pretrained('bert-base-chinese')
my_model = transformers.AutoModel.from_pretrained('bert-base-chinese')

# 准备数据
text1 = '我爱你'
text2 = ['我爱你','我非常恨你']

# 使用tokenizer处理数据
data = my_tokenizer(
    text2,
    max_length=6,
    padding='max_length',
    truncation=True,
    return_tensors='pt'
)
print(data) # {input_ids,token_type_ids,attention_mask}
# 使用model前向传播
result = my_model(**data)
print(result['last_hidden_state'].shape) # torch.Size([1, 8, 768])
print(result['last_hidden_state'][:,0,:].shape) # cls的最终向量信息包含所有语义信息
print(result['pooler_output'].shape) # 池化后向量包含所有语义信息

