# 导包
import fasttext

train_pre = 'data/cooking.pre.train'
valid_pre = 'data/cooking.pre.valid'
train_txt = 'data/cooking_train.txt'
valid_txt = 'data/cooking_valid.txt'


# train data
def train_model():
    # train_data
    model = fasttext.train_supervised(
        input = train_txt,
        autotuneValidationFile = valid_txt,
        autotuneDuration=60*1,
        verbose=3
    )
    # 测试模型
    result = model.test(valid_txt)
    print(result)
    model.save_model('model/my-model.bin')

if __name__ == '__main__':
    train_model()