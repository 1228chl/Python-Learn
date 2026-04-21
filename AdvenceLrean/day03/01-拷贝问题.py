import copy

def dm01_putongfuzhi():
    a = 10
    b = a
    d = 10
    print(id(a))
    print(id(b))
    print(id(d))
    print(id(10))

    print("*"*50)


    a = [1,2,3]
    b = [11,22,33]
    c = [a,b]
    d = c
    print(id(a))
    print(id(c[0]))
    print(id(b))
    print(id(c[1]))
    print(id(c))
    print(id(d))

# dm01_putongfuzhi()


a = [1,2,3]
b = [11,22,33]
c = [12,[2,3,4],b]

d = copy.copy(c)
c[1][0] = 4
# c[1] = [1,2,3]
print(c)
print(d)

# a1 = [1, 2, 3]
# b1 = [1, 2, 3]
a1 = (1, 2, 3)
b1 = (1, 2, 3)
c1 = (1, 2, a1, b1)
d1 = (1, 2, a1, b1)
print("c-->", id(c1))
print("d-->", id(d1))
print("d==c?", id(d1)==id(c1))
e = copy.deepcopy(c1)
print(id(e))
g = copy.copy(c1)
print(id(g))