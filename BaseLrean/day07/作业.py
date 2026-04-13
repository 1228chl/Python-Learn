# 1. 先打印提示主界面(1-6的数字): 让用户选择他/她要进行的操作.
# 2. 当用户选择1的时候, 实现操作: 添加学生(学生编号, 学生姓名, 手机号).   注意: 学生编号必须唯一
# 3. 当用户选择2的时候, 实现操作: 删除学生(根据编号删除)
# 4. 当用户选择3的时候, 实现操作: 修改学生信息(先输入学生编号, 只能改姓名, 手机号)
# 5. 当用户选择4的时候, 实现操作: 查询单个学生信息(根据编号查)
# 6. 当用户选择5的时候, 实现操作: 查询所有学生信息
# 7. 当用户选择6的时候, 实现操作: 退出系统         注意: 只要用户不主动退出,那就一直能用!!!

dict_stu = {"1":["张三","1234775757"],
            "2":["张三","1234775757"],
            "3":["张三","1234775757"]
            }



def print_into():
    print("*" * 30)
    print("欢迎来到学生管理系统")
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4.查询单个学生信息")
    print("5.查询所有学生信息")
    print("6.退出系统")
    print("*" * 30)
    print()

def add_stu():
    stu_num = input("请输入学生编号:").strip()
    if stu_num in dict_stu:
        print("这个学生编号已存在,请重新输入")
        add_stu()
    stu_name = input("请输入学生姓名:")
    stu_phone =input("请输入手机号:")
    dict_stu[stu_num] = [stu_name, stu_phone]
    print("添加成功，请回车后继续")
    input()

def del_stu():
    stu_num = input("请输入学生编号:").strip()
    if stu_num not in dict_stu:
        print("系统里没有此信息，请重新输入。")
        del_stu()
    del dict_stu[stu_num]
    print("删除成功，请回车后继续")
    input()

def update_stu():
    stu_num = input("请输入学生编号:").strip()
    if stu_num not in dict_stu:
        print("系统里没有此信息，请重新输入。")
        update_stu()
    stu_name = input("请输入学生姓名:")
    stu_phone = input("请输入手机号:")
    dict_stu[stu_num] = [stu_name, stu_phone]
    print("更新成功，请回车后继续")
    input()

def search_stu():
    stu_num = input("请输入学生编号:").strip()
    if stu_num not in dict_stu:
        print("系统里没有此信息，请重新输入。")
        search_stu()
    print(f"编号：{stu_num} 姓名：{dict_stu[stu_num][0]} 手机号：{dict_stu[stu_num][1]}")
    print("查询成功，请回车后继续")
    input()

def search_stus():
    if len(dict_stu) != 0:
        for k,v in dict_stu.items():
            stu_num = k
            stu_name = v[0]
            stu_phone = v[1]
            print(f"编号：{stu_num}姓名：{stu_name} 手机号：{stu_phone}")
        print("查询成功，请回车后继续")
        input()
    else:
        print("没有数据,请回车后继续")
        input()

def exit_stu():
    exit(0)

while True:
    print_into()
    try:
        num = int(input("请选择功能（输入相应数字）："))
    except ValueError:
        print("请输入有效的数字！")
        continue
    if num < 1 or num > 6:
        print("请输入正确的序号")
    elif num == 1:
        add_stu()
    elif num == 2:
        del_stu()
    elif num == 3:
        update_stu()
    elif num == 4:
        search_stu()
    elif num == 5:
        search_stus()
    elif num == 6:
        exit_stu()


