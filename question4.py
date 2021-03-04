lst = [] 
n = int(input("Enter number of elements : ")) 
x = 0
for i in range(0, n): 
    e = int(input()) 
    lst.append(e)
    x ^= lst[i]
print(x) 
