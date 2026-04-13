li = [2,5,3,7,5,7]
missing_nums = []

max_num = max(li)
min_num = min(li)

for i in range(min_num,max_num):
    if i not in li:
        missing_nums.append(i)
sum_missing_num = sum(missing_nums)
print(sum_missing_num)
print(missing_nums)

for i,j in enumerate(li):
    print(i,j)

s = '5=Five 6=Six 7=Seven'
d = {}
l = s.split()
for i in l:
    k,v = i.split('=')
    d[k] = v
print(d)