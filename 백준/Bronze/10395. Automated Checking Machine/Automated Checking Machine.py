lst1 = [*map(int, input().split())]
lst2 = [*map(int, input().split())]
for i in range(len(lst1)) : lst1[i] += lst2[i]
if lst1[0] == lst1[1] == lst1[2] == lst1[3] == lst1[4] == 1 : print("Y")
else : print("N")
