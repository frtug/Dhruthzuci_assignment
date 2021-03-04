
def intersect(lst1, lst2): 
    inter = set(lst1) & set(lst2) 
    return list(inter)

l1 = []
l2 = []
n1 = int(input("enter the number for list1"))
n2 = int(input("enter the number for list2"))
for i in range(n1):
    d = int(input(""))
    l1.append(d)
for i in range(n2):
    d = int(input(""))
    l2.append(d)

print(intersect(l1, l2))