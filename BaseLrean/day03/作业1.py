number_p = int(input("请输入顾客人数："))
number_j = int(input("请输入总账单："))
sum_s = number_j / number_p
sum_s += number_j * 0.2
print(f"每人应付{sum_s:.2f}元")

