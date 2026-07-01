from config.config import Config
import os
import pandas as pd

# 提前创建配置对象
config = Config()

def convert_to_words_fasttext():

    # 读取类别映射（数字→类别名）
    id2class = config.id2class
    # 定义转换函数
    def convert_file(input_path,output_path):
        # 读取分词文件，生成Fasttext格式
        # 读取制表符分隔文件，包含 words 和 label 两列
        df = pd.read_csv(input_path,sep='\t')

        with open(output_path,'w',encoding='utf-8') as f:
            for _,row in df.iterrows():
                label_name = id2class[row['label']]
                # 注意：words 列已经是空格分词后的字符串
                line = f"__label__{label_name} {row['words']}\n"
                f.write(line)
        print(f"✅ 已生成 {output_path}")

    # 转换训练集
    convert_file(config.process_train_path, config.process_train_path_words)
    # 转换验证集
    convert_file(config.process_dev_path, config.process_dev_path_words)
    # 转换测试集
    convert_file(config.process_test_path, config.process_test_path_words)
    print("🎯 所有数据格式转换完成！")

def convert_to_chars_fasttext():
    id2class = config.id2class

    def convert_file(input_csv, output_txt):
        """从原始 CSV（含 text 和 label）生成字符级 FastText 格式"""
        df = pd.read_csv(input_csv, sep='\t')  # 制表符分隔

        with open(output_txt, 'w', encoding='utf-8') as f_out:
            for _, row in df.iterrows():
                text = str(row['text'])  # 转为字符串
                # 字符级切分：将每个字符用空格连接
                char_seq = ' '.join(text)  # 例如 "你好" → "你 好"
                label_name = id2class[row['label']]
                line = f"__label__{label_name} {char_seq}\n"
                f_out.write(line)
        print(f"✅ 已生成字符级 FastText 文件：{output_txt}")

    # 转换三个集合
    convert_file(config.train_path, config.process_train_path_chars)
    convert_file(config.dev_path, config.process_dev_path_chars)
    convert_file(config.test_path, config.process_test_path_chars)

    print("🎯 字符级数据转换全部完成！")

if __name__ == '__main__':
    # convert_to_words_fasttext()
    convert_to_chars_fasttext()