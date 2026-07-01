# 导包
import transformers

# 加载bert预训练模型
bert_tokenizer = transformers.BertTokenizer.from_pretrained('bert-base-chinese')
bert_model = transformers.BertModel.from_pretrained('bert-base-chinese')

# 准备数据
texts = ['传智教育','黑马程序员','人工智能专业']
# texts = ('传智教育','黑马程序员')

# bert_tokenizer处理数据
# data = bert_tokenizer(test='传智教育',text_pair='黑马程序员')
data = bert_tokenizer(
    texts,
    max_length=8,
    padding='max_length',
    truncation=True,
    return_tensors='pt'
)

# 底层填充：['[CLS]传智教育[SEP][PAD][PAD]','[CLS]黑马程序员[SEP][PAD]','[CLS]人工智能专业[SEP]']
print(data['input_ids'])
print(data['token_type_ids'])
print(data['attention_mask'])

# bert_model前向传播
result = bert_model(**data)
print(result.last_hidden_state.shape)
print(result.last_hidden_state[:,0,:].shape)
print(result.pooler_output.shape)

