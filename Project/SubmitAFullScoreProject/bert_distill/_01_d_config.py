import transformers
import torch
class Config:
    def __init__(self):
        # 各种路径
        # 原始数据路径
        self.root_path = r'G:\code\python\Python-Learn\Project\SubmitAFullScoreProject/'
        self.train_path = self.root_path + r'data/train.txt'
        self.dev_path = self.root_path + r'data/dev.txt'
        self.test_path = self.root_path + r'data/test.txt'

        self.class_path = self.root_path + r'data/class.txt'
        self.stop_words_path = self.root_path + r'data/stopwords.txt'

        # 随机森林处理后数据存放路径
        self.process_train_path = self.root_path + r'rf/processed_data/process_train.txt'
        self.process_test_path = self.root_path + r'rf/processed_data/process_test.txt'
        self.process_dev_path = self.root_path + r'rf/processed_data/process_dev.txt'

        # 随机森林模型保存路径
        self.rf_save_model_path = self.root_path + r'rf/model/rf.pkl'
        self.tfidf_save_path = self.root_path + r'rf/model/tfidf.pkl'
        # fasttext相关路径
        # fasttext处理后数据存放路径
        self.process_train_path_chars = self.root_path + r'fasttext/processed_data/train_process_chars.txt'
        self.process_test_path_chars = self.root_path + r'fasttext/processed_data/test_process_chars.txt'
        self.process_dev_path_chars = self.root_path + r'fasttext/processed_data/dev_process_chars.txt'

        self.process_train_path_words = self.root_path + r'fasttext/processed_data/train_process_words.txt'
        self.process_test_path_words = self.root_path + r'fasttext/processed_data/test_process_words.txt'
        self.process_dev_path_words = self.root_path + r'fasttext/processed_data/dev_process_words.txt'
        # fasttext模型保存路径
        self.ft_char_default_model_path = self.root_path + r'fasttext/model/ft_char_default.bin'
        self.ft_char_auto_model_path = self.root_path + r'fasttext/model/ft_char_auto.bin'
        self.ft_word_default_model_path = self.root_path + r'fasttext/model/ft_word_default.bin'
        self.ft_word_auto_model_path = self.root_path + r'fasttext/model/ft_word_auto.bin'
        # 分类词表
        self.id2class = {index: line.strip() for index, line in enumerate(open(self.class_path, 'r', encoding='utf-8'))}

        # 4.bert相关路径和参数

        # bert预训练模型路径
        self.bert_base_chinese_path = self.root_path + r'bert_base/bert-base-chinese'
        # 提前加载tokenizer和bert模型
        self.bert_tokenizer = transformers.BertTokenizer.from_pretrained(self.bert_base_chinese_path)
        self.bert_model = transformers.BertModel.from_pretrained(self.bert_base_chinese_path)
        # 提前加载config文件对象
        self.bert_config = transformers.BertConfig.from_pretrained(self.bert_base_chinese_path)
        # bert模型保存路径
        self.bert_classifier_model_save_path = self.root_path + r'bert_base/model/bert_classifier.pt'

        # 参数
        self.epochs = 1
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu') # 适合window
        self.batch_size = 64
        self.lr = 5e-5
        self.max_len = 32
        self.class_num = len(self.id2class)

        # todo 5.bert蒸馏相关路径和参数
        self.distill_bilstm_save_path = self.root_path + r'bert_distill/model/bilstm_model.pt'
        self.embed_size = 128
        self.hidden_size_lstm = 256
        self.num_layers = 3
        self.dropout_p = 0.3
        self.T = 2
        self.alpha = 0.7
        self.lstm_lr = 1e-3
        """
        教师模型：结构复杂，参数量打，需要使用较小学习率，避免过拟合
        学生模型：结构简单，参数量小，需要使用较大学习率，得到充分训练
        """

        print('配置文件初始化动作完成!')
if __name__ == '__main__':
    c = Config()
    print(c.ft_word_auto_model_path)
    print(c.id2class)
