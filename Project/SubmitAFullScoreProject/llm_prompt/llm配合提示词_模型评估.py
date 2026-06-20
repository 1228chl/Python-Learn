from zai import ZhipuAiClient
import os
from config import Config
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from tqdm import tqdm

config = Config()

# 初始化客户端
client = ZhipuAiClient(api_key=os.environ.get('ZHIPU_API_KEY'))

SYSTEM_PROMPT = """
Role: 你是一个顶尖的新闻文本分类专家。你的核心任务是根据给定的新闻标题，精准判断其所属的唯一类别。
Constraints & Output Format: 输出要求：你必须有仅且仅返回以下10个英文单词之一，必须有一个类别,如果你没找到合适的,可以默认返回society,
不得包含任何解释、标点符号或换行符。可选类别：finance, realty, stocks, education, science, society, politics, sports, game, entertainment
Category Definition Guidelines (分类判定标准):
请依据以下严格的定义进行逻辑推理：

finance (财经/宏观经济)：涉及货币政策、银行利率、汇率变动、宏观经数据（CPI/PPI）、债券市场、保险行业动态。注：纯股票买卖行为不在此列。
realty (房地产/土地)：涉及土地拍卖、楼盘价格变动、住房政策（非金融属性）、房企债务暴雷、长租公寓、物业管理。
stocks (证券市场/个股/股市)：涉及具体股票代码、股价涨跌停、主力资金流向、上市公司财报（特指因业绩引发的股价波动）、证监会针对股市的监管行为。
education (教育)：涉及高考招生、学校政策（小学至大学）、考研、职业教育、双减政策、课程改革、校园招聘。
science (科学技术/自然科学)：涉及航空航天（非军事用途）、AI大模型发布、生物基因突破、物理化学新材料、互联网技术革新（非商业层面）。
society (社会民生/法制)：涉及社会治安、交通事故、司法案件判决、劳动保障、消费维权、邻里纠纷、自然灾害（非政治层面）。
politics (政治/政务/国际外交)：涉及国家领导人活动、政府机构改革、党章宪法、国际外交会见、联合国声明、涉及台湾/西藏/新疆的政治表述。
sports (体育竞技)：涉及足球、篮球、田径等赛事比分、运动员转会、奥运会（非娱乐综艺类运动）。
game (电子游戏/电竞)：涉及游戏版本更新、电竞赛事战报、游戏公司开发进度（特指内容层面）、游戏防沉迷政策（注意：若提及"游戏公司股价"，则归类为stocks）。
entertainment (娱乐/明星/影视)：涉及影视剧上映、明星八卦绯闻、综艺节目内容、网红炒作（非体育竞技类）。

Few-shot Examples (思维链参考):
请参考以下推理模式：
输入："美联储宣布加息50个基点，美元指数应声走强" 推理：明确提及货币政策与宏观汇率 -> 输出：finance
输入："《黑神话：悟空》首月销量突破2000万份，Steam在线峰值创新高" 推理：涉及电子游戏产品数据与平台表现 -> 输出：game
输入："中国空间站迎来神舟十八号乘组，航天员开展出舱活动" 推理：涉及航天科技探索，非军事，非商业 -> 输出：science
输入："北京市西城区某小区业主因物业费上调发生激烈冲突" 推理：涉及社区纠纷，属社会司法治安范畴 -> 输出：society

Your Response : 必须有一个类别输出,如果你在上述10个类别中没找到合适的,可以默认返回society
"""


# todo 加载原始数据
def load_data(base_path):
    # 提前创建一个列表,用于存储(新闻,标签)元组
    data_list = []
    for line in open(base_path, 'r', encoding='utf8'):
        text, label_str = line.strip().split('\t')
        label = int(label_str)
        # 先封装成元组,再append到列表中
        data_list.append((text, label))
    # 单独获取所有的新闻标题和真实标签
    texts, labels = zip(*data_list)
    # 返回结果
    return texts, labels


def predict_fun(q):
    response = client.chat.completions.create(
        model="glm-5.2",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": q
            }
        ],
        temperature=0.6
    )
    # 获取预测类别
    y_pred_class = response.choices[0].message.content
    # 返回对应索引
    return config.class2id[y_pred_class]


def llm_prompt_eval(path):
    # 获取所有的新闻标题和真实标签
    texts, all_true_labels = load_data(path)
    # 提前创建pred_labels列表,存储预测结果
    all_pred_labels = []
    for q in tqdm(texts):
        y_pred_label = predict_fun(q)
        # print(f'llm模型预测结果:{y_pred_label}')
        all_pred_labels.append(y_pred_label)
    # todo 计算准确率,精确率,召回率,f1分数
    acc = accuracy_score(all_true_labels, all_pred_labels)
    pre = precision_score(all_true_labels, all_pred_labels, average='macro')
    rec = recall_score(all_true_labels, all_pred_labels, average='macro')
    f1 = f1_score(all_true_labels, all_pred_labels, average='macro')
    print(f'准确率:{acc},精确率:{pre},召回率:{rec},f1:{f1}')


if __name__ == '__main__':
    # llm_prompt_eval('test_llm.txt')
    llm_prompt_eval(config.test_path)
