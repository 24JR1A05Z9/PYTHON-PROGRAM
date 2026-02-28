a=" Hello how are you sofi"
b=a.split();
c=set() 
print("after list",b)
for i in range(len(b)):
    c.update(b[i]);
    print(c)
print(" ".join(b))
