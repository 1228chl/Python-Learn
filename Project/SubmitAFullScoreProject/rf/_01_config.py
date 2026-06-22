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
        # 各种参数

if __name__ == '__main__':
    # 测试配置文件
    config = Config()
    # 打印参数路径
    print(config.train_path)
    print(config.test_path)
    print(config.dev_path)
    print(config.class_path)
    print(config.stop_words_path)
