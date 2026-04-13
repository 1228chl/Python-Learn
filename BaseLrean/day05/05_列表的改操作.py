li = [1,2,5,6,7,2,3,52,341,6,43,2,4,21,3,1,34,13,6,4]
li2 = ["hesdaf","adsfa","fgsfg","wrfdsg","fdgsldfj","fdsireajf"]

li[0] = 143
print(li)

li.reverse()
print(li)
li2.reverse()
print(li2)

li.sort()
print(li)
li2.sort()
print(li2)

li.sort(reverse=True)
print(li)
li2.sort(reverse=True)
print(li2)

# 方法一
li = ["z","l","w","zl","z","sq","zb","z"]
for i in range(li.count("z")):
    li.remove("z")
print(li)

# 方法二 最快，最省内存
li = ["z","l","w","zl","z","sq","zb","z"]
print([x for x in li if "z" != x])

# 方法三
li = ["z","l","w","zl","z","sq","zb","z"]
for i in li.copy():
    if i == "z":
        li.remove(i)
print(li)