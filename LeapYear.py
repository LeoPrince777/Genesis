z = input("Pls give your Year")
if z%4==0 and z%400==0 or z%100!=0:
    print("Leap Year")
else:
    print("Not Leap Year")    