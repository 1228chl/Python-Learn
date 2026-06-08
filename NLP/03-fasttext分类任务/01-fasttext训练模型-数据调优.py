# 导包
import fasttext

train_pre = 'data/cooking.pre.train'
valid_pre = 'data/cooking.pre.valid'
train_txt = 'data/cooking_train.txt'
valid_txt = 'data/cooking_valid.txt'


# train data
def train_model():
    # train_data 本次只指定数据，参数都默认
    model = fasttext.train_supervised(train_txt)
    # 测试模型
    result = model.test(valid_txt)
    print(result)
    label = model.predict(text= ["How much does potato starch affect a cheese sauce recipe?"])
    print(f"预测结果为：{label[0][0][0][9:]}")

def train_model_optimizer_data():
    # train_data 本次只指定数据，参数都默认
    model = fasttext.train_supervised(train_pre)
    # 测试模型
    result = model.test(valid_pre)
    print(result)
    label = model.predict(text = ["How much does potato starch affect a cheese sauce recipe?"])
    print(f"预测结果为：{label[0][0][0][9:]}")
if __name__ == '__main__':
    train_model()
    print('+'*50)
    train_model_optimizer_data()