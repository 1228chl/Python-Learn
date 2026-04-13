score = int(input("请输入分数："))
if score >=90:
    res = "A"
elif score >=80:
    res = "B"
elif score >=70:
    res = "C"
elif score >=60:
    res = "D"
elif score >=50:
    res = "E"
else:
    res = "不合格"

print(res)