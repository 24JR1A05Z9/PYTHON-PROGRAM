a=" Hello how are you sofi"
b=a.split();
c=set()
b=set()
print("after list",b)
for i in range(len(b)):
    c.update(b[i])
d=set(b)
print(c)
print(" ".join(b))
