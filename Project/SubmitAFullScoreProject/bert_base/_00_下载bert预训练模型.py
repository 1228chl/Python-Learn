# Model Download
from modelscope import snapshot_download
from _01_config import Config
config = Config()
model_dir = snapshot_download('google-bert/bert-base-chinese',local_dir=config.bert_base_chinese_path)
print(model_dir)