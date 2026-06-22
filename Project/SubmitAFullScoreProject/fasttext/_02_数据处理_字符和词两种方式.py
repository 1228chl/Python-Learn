# 导包
from _01_config import Config
import jieba

# 提前创建配置对象
config = Config()

# 定义处理数据的api函数
def process_data(base_path,process_path,is_jieba):
    # 判断是否是jieba分词,如果是就jieba分词,否则字符方式
    if is_jieba:
        # 读取文件
        with open(base_path,'r',encoding='utf8') as fr:
            with open(process_path,'w',encoding='utf8') as fw:
                for line in fr:
                    # 先去除\n,然后切割成列表,最后拆包出text和label
                    text,label = line.strip().split('\t')
                    # 根据label索引获取对应的分类名,然后分词
                    label = config.id2class[int(label)]
                    words = " ".join(jieba.lcut(text))
                    # 拼接成fasttext要求的数据格式
                    ft_line = '__label__' + label + " " + words + '\n'
                    # 写出到文件中
                    fw.write(ft_line)
    else:
        with open(base_path,'r',encoding='utf8') as fr:
            with open(process_path,'w',encoding='utf8') as fw:
                for line in fr:
                    # 先去除\n,然后切割成列表,最后拆包出text和label
                    text, label = line.strip().split('\t')
                    # 根据label索引获取对应的分类名,然后分字符
                    label = config.id2class[int(label)]
                    words = " ".join(list(text))  # 分字符
                    # 拼接成fasttext要求的数据格式
                    ft_line = '__label__' + label + " " + words + '\n'
                    # 写出到文件中
                    fw.write(ft_line)

if __name__ == '__main__':
    process_data(config.train_path, config.process_train_path_chars, is_jieba=False)
    process_data(config.train_path, config.process_train_path_words, is_jieba=True)

    process_data(config.test_path, config.process_test_path_chars, is_jieba=False)
    process_data(config.test_path, config.process_test_path_words, is_jieba=True)

    process_data(config.dev_path, config.process_dev_path_chars, is_jieba=False)
    process_data(config.dev_path, config.process_dev_path_words, is_jieba=True)