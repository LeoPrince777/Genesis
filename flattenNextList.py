#m-1
list1 = [[1], [2, 3], [4, 5, 6, 7]]

flat_list = sum(list1, [])
print(flat_list)

#m-2
list2 =[[5], [1, 3], [4, 5, 9, 7]]
list3 =[]
for i in list2:
	for j in i:
		list3.append(j)
print(list3)
