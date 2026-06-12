#模型下载
from modelscope import snapshot_download
model_dir = snapshot_download('google-bert/bert-base-chinese',local_dir=r'G:\code\python\Python-Learn\NLP\05-Transformer和Bert应用\model')
