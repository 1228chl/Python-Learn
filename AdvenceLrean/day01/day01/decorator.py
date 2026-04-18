# 定义装饰器1 先跳转到登录界面输入账号密码
def check_login(func_name):
    def login_inner():
        print('正在登录中...')
        func_name()

    return login_inner


# 定义装饰器2 再输入验证码进行验证校验
def check_code(func_name):
    def code_inner():
        print('验证码校验中...')
        func_name()

    return code_inner
