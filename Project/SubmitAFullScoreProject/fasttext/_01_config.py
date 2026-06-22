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
if __name__ == '__main__':
    c = Config()
    print(c.ft_word_auto_model_path)
    print(c.id2class)
