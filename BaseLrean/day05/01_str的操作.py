file_str= 'hello_.wor.ld.png'

# 切片获取文件类型
print(file_str[-1:-5:-1])
print(file_str[-4:])

# 用find方法获取
# todo:获取的是子串的第一个字符的下标，如果匹配多个子串，只会返回第一个
sub_index = file_str.find('.')
print(file_str[sub_index:])
sub_index1 = file_str.rfind(".")
print(file_str[sub_index1:])

# 修改字符串，相当于新生成一个字符串
tmp_str = "hello world hello world"
# 替换字符串
# “字符串”.replace("旧子串"，“新子串”，“匹配次数”)
re_str = tmp_str.replace("world","python")
print(re_str)
re_str = tmp_str.replace("world","python",1)
print(re_str)

# 分隔字符串
# “字符串”.split("分隔符")
li = tmp_str.split(" ")
print(li)
tmp_str = "hello-world-hello-world"
li = tmp_str.split("-")
print(li)
tmp_str = "hello world hello world"
li = tmp_str.split()#默认分隔符为空格
print(li)

#连接字符串
#“字符串”.join(可迭代对象)
res_str = "+".join(li)
print(res_str)

#需求：将字符串向右旋转n位，例如“abcdef”向右旋转2未得到“efabcd”
# 1. 输入字符串
t = input("请输入字符串：")
# 2. 输入旋转的位数
n = int(input("请输入旋转位数："))
# 3. 旋转位数肯恩超出字符串长度，可以考虑取余
n = n % len(t)
# 4. 使用旋转位置索引截取字符串替换前后位置
# 获取旋转的部分
p = t[-n:]
f = t[:-n]
r = p + f
# 5. 打印结果
print(r)