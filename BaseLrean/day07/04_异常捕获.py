import os
import random
# try:
#     f = open("heima.txt","r",encoding="utf-8")
#     content = f.readlines()
#     print("wenjian",content)
#     f.close()
# except Exception as e:
#     print(e)
#
# try:
#     0/1
# except Exception as e:
#     print("异常信息",e)
# else:
#     print("没有异常")



# try:
#     if os.path.exists("heima.txt"):
#         f = open("heima.txt","r",encoding="utf-8")
#         content = f.readlines()
#         print("endian",content)
# except Exception as e:
#     print("异常信息：",e)
# finally:
#     print("关闭文件")
#     f.close()
#
# try:
#     with open("heima.txt","r",encoding="utf-8") as f:
#         content = f.readlines()
#         print("endian",content)
# except Exception as e:
#     print("异常信息：",e)
# finally:
#     print("关闭文件")

def guess_number_game():
    guess_num = random.randint(1, 100)
    while True:
        try:
            input_num = int(input("请输入您要猜的整数"))
            if input_num == guess_num:
                print("wing")
                break
            elif input_num > guess_num:
                print(">")
            else:
                print("<")
        except ValueError:
            print("please input int !!!")

guess_number_game()