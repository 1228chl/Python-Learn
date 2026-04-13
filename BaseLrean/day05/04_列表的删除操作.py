li = [1,2,3,4,5,6,7,8,9]

del li[0]
print(li)

print("---" * 20)
temp = li.pop()
print(li)
print(temp)
temp= li.pop(2)
print(li)
print(temp)

print("---" *20)
li.remove(3)
print(li)
if 9 in li:
    li.remove(9)
