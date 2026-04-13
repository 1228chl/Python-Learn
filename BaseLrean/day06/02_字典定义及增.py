d = {}
print(d)
print(type(d))
d = dict()
print(d)
print(type(d))
d = {"name":"张三","age":18,"sex":"男"}
print(d)
d["height"] = 180
print(d)
d["height"]= 190
print(d)
del d["height"]
print(d)
d.clear()
print(d)
d = {"name":"张三","age":18,"sex":"男"}
print(d["name"])
print(d.get("name"))
print(d.get("height"))
print(d.get("height",170))
print(d.keys())
for k in d.keys():
    print(k)
print(list(d.keys()))
print(d.values())
print(d.items())
for k,v in d.items():
    print(k,v)
print(list(d.items()))


