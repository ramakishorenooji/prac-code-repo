from collections import defaultdict

d = defaultdict(list)
d['python'].append("learning")
print(d)

for i in d.items():
    print(i)