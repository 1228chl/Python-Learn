li = [7,8,9,5,6,7,2,3]
res = []
for i in range(len(li)-1):
    res.append(max(li[i],li[i+1]))
print(res)

ol = [1,2,2,3,3,3,4,4,4,4,5,5,6,6,7]
res = []
for i in ol:
    if i not in res:
        res.append(i)
print(res)