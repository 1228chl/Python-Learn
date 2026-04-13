i = 1
li = []
while i <= 100:
    li.append(i)
    i += 1
print(len(li))

li = []
for i in range(1, 101):
    li.append(i)
print(len(li))

li = [i for i in range(1, 101)]
print(len(li))
print(li[:30])

li = [i * 2 for i in range(1,21) if i % 2 == 0]
print(li)

li = [(i , j) for i in range(1, 3) for j in range(0,3)]
print(li)

dic = {key:value for key , value in li}
print(dic)
dic = {key:value * 2 for key ,value in li if key % 2 != 0}
print(dic)