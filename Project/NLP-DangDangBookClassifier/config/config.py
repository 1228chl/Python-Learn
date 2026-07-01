import json
import os
import transformers
import torch

class Config:
    def __init__(self):
        print('正在初始化配置文件...')
        # 根目录
        self.root_path = r'G:\code\python\Python-Learn\Project\NLP-DangDangBookClassifier'

        # 原始数据路径
        self.title_csv = self.root_path + r'data/origin_csv/cat_title.csv'
        self.title_fixed = self.root_path + r'data/origin_csv/cat_title_fixed.csv'
        self.category_index = self.root_path + r'data/origin_txt/category_index.txt'
        self.stop_words = self.root_path + r'data/origin_txt/stopwords.txt'

        self.train_path = self.root_path + r'data/origin_csv/train.csv'
        self.dev_path = self.root_path + r'data/origin_csv/dev.csv'
        self.test_path = self.root_path + r'data/origin_csv/test.csv'

        #分词处理后数据存放路径
        self.process_train_path = self.root_path + r'data/processed/process_train.txt'
        self.process_test_path = self.root_path + r'data/processed/process_test.txt'
        self.process_dev_path = self.root_path + r'data/processed/process_dev.txt'

        # tfidf和模型保存位置
        self.tfidf_save_path = self.root_path + r'model/baselines/random_forests/tfidf.pkl'
        self.random_forests_save_model_path = self.root_path + r'model/baselines/random_forests/random_forests.pkl'

        # fasttext相关路径
        # fasttext处理后数据存放路径
        self.process_train_path_chars = self.root_path + r'data/processed/train_process_chars.txt'
        self.process_test_path_chars = self.root_path + r'data/processed/test_process_chars.txt'
        self.process_dev_path_chars = self.root_path + r'data/processed/dev_process_chars.txt'

        self.process_train_path_words = self.root_path + r'data/processed/train_process_words.txt'
        self.process_test_path_words = self.root_path + r'data/processed/test_process_words.txt'
        self.process_dev_path_words = self.root_path + r'data/processed/dev_process_words.txt'
        # fasttext模型保存路径
        self.ft_char_default_model_path = self.root_path + r'model/baselines/fasttext/ft_char_default.bin'
        self.ft_char_auto_model_path = self.root_path + r'model/baselines/fasttext/ft_char_auto.bin'
        self.ft_word_default_model_path = self.root_path + r'model/baselines/fasttext/ft_word_default.bin'
        self.ft_word_auto_model_path = self.root_path + r'model/baselines/fasttext/ft_word_auto.bin'
        # 分类词表
        # 缓存文件路径（和原始txt放在同目录，方便管理）
        self.mapping_cache_path = self.root_path + r'data/origin_txt/id2class_cache.json'

        # 1. 加载 id2class（优先从缓存读，没有则生成并保存）
        if os.path.exists(self.mapping_cache_path):
            with open(self.mapping_cache_path, 'r', encoding='utf-8') as f:
                raw_dict = json.load(f)
                # JSON键默认是字符串，转回int
                self.id2class = {int(k): v for k, v in raw_dict.items()}
            print(f'  √ 从缓存加载类别映射，共 {len(self.id2class)} 类')
        else:
            # 首次运行：读取原始txt，生成字典
            self.id2class = {index: line.strip() for index, line in
                             enumerate(open(self.category_index, 'r', encoding='utf-8'))}
            # 保存为json缓存，下次直接用
            with open(self.mapping_cache_path, 'w', encoding='utf-8') as f:
                json.dump(self.id2class, f, ensure_ascii=False, indent=2)
            print(f'  √ 首次生成类别映射并保存缓存，共 {len(self.id2class)} 类')

        # 2. 生成反向映射 class2id（顺带实现）
        self.class2id = {v: k for k, v in self.id2class.items()}

        # bert预训练模型路径
        self.bert_base_chinese_path = self.root_path + r'model/bert/base/bert-base-chinese'
        # 提前加载tokenizer和bert模型
        self.bert_tokenizer = transformers.BertTokenizer.from_pretrained(self.bert_base_chinese_path)
        self.bert_model = transformers.BertModel.from_pretrained(self.bert_base_chinese_path)
        # 提前加载config文件对象
        self.bert_config = transformers.BertConfig.from_pretrained(self.bert_base_chinese_path)
        # BERT 模型保存路径
        self.bert_model_path = self.root_path + r'model/bert/base/bert_model'

        # ========== 新增：压缩模型保存路径（量化、剪枝、蒸馏） ==========
        # 三个文件夹都位于 model/bert/base/ 下
        self.quantization_dir = self.root_path + r'model/bert/quantization/'
        self.pruning_dir = self.root_path + r'model/bert/pruning/'
        self.distill_dir = self.root_path + r'model/bert/distill/'

        # 为了方便，也可以单独定义各压缩产物的具体文件名
        self.onnx_raw_path = self.quantization_dir + r'model.onnx'  # 原始 ONNX
        self.onnx_quantized_path = self.quantization_dir + r'model_quantized.onnx'  # 量化后的 ONNX
        # 剪枝和蒸馏保存的是完整的 PyTorch 模型目录（包含 config.json, pytorch_model.bin 等）
        # 无需额外定义文件名，直接使用 save_pretrained(dir) 即可

        #参数
        self.epochs = 5
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.batch_size = 64
        self.lr = 3e-5
        self.max_len = 96
        self.class_num = len(self.id2class)

        self.hidden_dropout_prob = 0.2
        self.attention_probs_dropout_prob = 0.2
        self.gradient_accumulation_steps = 2  # 梯度累积步数

        self.patience = 3
        self.eval_interval = 1000
        self.best_metric = 'f1'

        print('配置文件初始化动作完成！')



