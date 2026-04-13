s = "lkjadffahghagajdgggggdg"
d = {}
# for i in s:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# print(d)
#
# for i in s:
#     d[i] = d.get(i, 0) + 1
# print(d)

for i in set(s):
    d[i] = s.count(i)
print(d)