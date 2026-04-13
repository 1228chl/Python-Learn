# 1.导包
# 注意: 必须提前安装ollama: pip install ollama
import ollama

# 2.ollama调用本地大模型
# 老版本ollama默认直接访问: http://127.0.0.1:11434/
# 新版本需要创建客户端对象
new_ollama = ollama.Client(host="http://127.0.0.1:11434")


def get_chat_result(message):
    # 发送请求获取响应
    result = new_ollama.chat(
        model="qwen3.5:4b",
        messages=message,
        # stream=True,
        # think=True
    )
    # 解析响应结果
    return result.message.content


if __name__ == '__main__':
    messages = [{"role": "user", "content": "给我讲一个笑话"}]
    res_data = get_chat_result(messages)
    print(res_data)
    print('=====================================================')
    messages = [{"role": "user", "content": "给我讲一个故事"}]
    res_data = get_chat_result(messages)
    print(res_data)