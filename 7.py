a=float(input("enter first number"))
b=float(input("enter second number"))
c=abs(a-b);
print(c);
if c<0.001:
    print("close to each other:")
else:
        print("not close to each other")
