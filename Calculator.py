p = input("Enter you 1st Number")
q = input("Enter your 2nd Number")
r = input(" 1.Add\n 2.Subtract\n 3.Multification\n 4.Division\n")
if r==1:
    print("Addition(+)")
    r = p+q
    print(r)
elif r== 2:
    print("Subtraction(-)")
    r = p-q
    print(r)
elif r== 3:
    print("Mulification(*)")
    r = p*q
    print(r)
elif r== 4:
    print("Division(/)")       
    r= p/q
    print(float(r)) 
else:
    print("Incorrect Value, Pls give proper input")