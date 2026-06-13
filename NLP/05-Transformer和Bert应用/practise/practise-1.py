import transformers

tokenizer = transformers.BertTokenizer.from_pretrained('../bert-base-chinese')
model = transformers.BertModel.from_pretrained('../bert-base-chinese')

text = '环境问题后的离开了哈到付哈'

data = tokenizer(
    text,
    max_length=20,
    padding='max_length',
    truncation=True,
    return_tensors='pt'
)
result = model(**data)
print(result.last_hidden_state.shape)
print(result.last_hidden_state)
print("*"*80)
print(result.last_hidden_state[:,0,:].shape)
print(result.last_hidden_state[:,0,:])
print("*"*80)
print(result.pooler_output.shape)
print(result.pooler_output)