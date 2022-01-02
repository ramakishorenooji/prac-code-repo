from collections import Counter
# remove_dup_nested_list.py

li = [[1, 2, 1, 4], [3, 2, 3], [3, 4], [1, 2, 1]]
li2 = []
for i in (li):
    li2.append(list(set(i)))
    
print(li2)
    
