def user_info(username,sex,age=18):
    print(f"当前用户：{username}，性别：{sex}，年龄：{age}")

user_info("赵六","man")
user_info("zhaoliu","man",180)


def user_info(*args):
    print(args)
    print(type(args))

user_info("张三","男",18)

def user_info(*args):
    print(f"当前用户：{args[0]}，性别：{args[1]}，年龄：{args[2]}")

user_info("张三","男",18)

def user_info(**kwargs):
    print(kwargs)
    print(type(kwargs))

user_info(username="张三",sex="男",age=18)

def user_info(**kwargs):
    print(f"当前用户：{kwargs['username']}，性别：{kwargs['sex']}，年龄：{kwargs['age']}")

user_info(username="张三",sex="男",age=18)


