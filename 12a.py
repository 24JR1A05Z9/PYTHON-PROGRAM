a=" Hello how are you sofi"
b=a.split();
c={} 
print("after list",b)
for i in range(len(b)):
    c[i]=b[i];
    print(c)
print(" ".join(b))
