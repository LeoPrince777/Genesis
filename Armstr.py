
a = str(input("Enter the Number"))
b= len(str(a))
print ("b value is",b)
sum =0
for i in a:
    sum = sum+int(i)**b
print(sum)
print(a)
if int(a) == sum:
	print("Armstrong Number")
else:
	print("Not Armstrong Number")