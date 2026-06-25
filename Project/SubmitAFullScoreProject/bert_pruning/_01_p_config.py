# 导包
import transformers
import torch


# 定义文件
class Config():
    def __init__(self):
        print('正在初始化配置文件....')
        # 各种路径
        # TODO 1.原始数据路径
        self.root_path = 'F:/szai6_tmf_project/'
        self.train_path = self.root_path + '_01_data/train.txt'
        self.test_path = self.root_path + '_01_data/test.txt'
        self.dev_path = self.root_path + '_01_data/dev.txt'
        # 停用词和类别路径
        self.stop_words_path = self.root_path + '_01_data/stopwords.txt'
        self.class_path = self.root_path + '_01_data/class.txt'
        # TODO 2.随机森林相关路径
        # 随机森林处理后数据存放路径
        self.process_train_path = self.root_path + '_02_rf/processed_data/train_process.txt'
        self.process_test_path = self.root_path + '_02_rf/processed_data/test_process.txt'
        self.process_dev_path = self.root_path + '_02_rf/processed_data/dev_process.txt'
        # 随机森林模型保存路径
        self.rf_save_model_path = self.root_path + '_02_rf/model/rf.pkl'
        self.tfidf_save_path = self.root_path + '_02_rf/model/tfidf.pkl'
        # TODO 3.fasttext相关路径
        # fasttext处理后数据存放路径
        self.process_train_path_chars = self.root_path + '_03_fasttext/processed_data/train_process_chars.txt'
        self.process_test_path_chars = self.root_path + '_03_fasttext/processed_data/test_process_chars.txt'
        self.process_dev_path_chars = self.root_path + '_03_fasttext/processed_data/dev_process_chars.txt'

        self.process_train_path_words = self.root_path + '_03_fasttext/processed_data/train_process_words.txt'
        self.process_test_path_words = self.root_path + '_03_fasttext/processed_data/test_process_words.txt'
        self.process_dev_path_words = self.root_path + '_03_fasttext/processed_data/dev_process_words.txt'
        # fasttext模型保存路径
        self.ft_char_default_model_path = self.root_path + '_03_fasttext/model/ft_char_default.bin'
        self.ft_char_auto_model_path = self.root_path + '_03_fasttext/model/ft_char_auto.bin'
        self.ft_word_default_model_path = self.root_path + '_03_fasttext/model/ft_word_default.bin'
        self.ft_word_auto_model_path = self.root_path + '_03_fasttext/model/ft_word_auto.bin'
        # 分类词表
        self.id2class = {index: line.strip() for index, line in enumerate(open(self.class_path, 'r', encoding='utf8'))}
        # TODO 4.bert相关路径和参数
        # todo 路径
        # bert预训练模型路径
        self.bert_base_chinese_path = self.root_path + '_04_bert_base/bert-base-chinese'
        # 提前加载tokenizer和bert模型对象
        self.bert_tokenizer = transformers.BertTokenizer.from_pretrained(self.bert_base_chinese_path)
        self.bert_model = transformers.BertModel.from_pretrained(self.bert_base_chinese_path)
        # 提前加载config文件对象
        self.bert_config = transformers.BertConfig.from_pretrained(self.bert_base_chinese_path)
        # bert模型保存路径
        self.bert_classifier_model_save_path = self.root_path + '_04_bert_base/model/bert_classifier_model.pt'
        # todo 参数
        # 前面适合window   如果你是mac且支持mps,直接设置'mps'也行
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.epochs = 1
        self.batch_size = 64
        self.lr = 5e-5
        self.max_len = 32
        self.class_num = len(self.id2class)  # 10

        # TODO 5.Bert剪枝相关路径
        self.pruning_bert_model_save_path = self.root_path + '_08_bert_pruning/model/pruning_bert_model.pt'

        print('配置文件初始化动作完成!')


# print(__name__) # 当前文件运行就是__main__,其他位置导包是模块名
# 此处测试必须加main,不加main,其他位置导包的时候自动调用测试代码
if __name__ == '__main__':
    c = Config()
    print(c.pruning_bert_model_save_path)

