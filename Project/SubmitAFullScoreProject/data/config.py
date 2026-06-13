class Config:
    def __init__(self):
        self.root_path = r'G:\code\python\Python-Learn\Project\SubmitAFullScoreProject'
        self.train_path = self.root_path + r'/data/train.txt'
        self.dev_path = self.root_path + r'/data/dev.txt'
        self.test_path = self.root_path + r'/data/test.txt'

if __name__ == '__main__':
    # 测试配置文件
    config = Config()
    # 打印参数路径
    print(config.train_path)
    print(config.test_path)
    print(config.dev_path)
