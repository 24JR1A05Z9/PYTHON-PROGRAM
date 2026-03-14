def first_dif(s1, s2):
    n = min(len(s1), len(s2))
    for i in range(n):
        if s1[i] != s2[i]:
            return i
    if len(s1) != len(s2):
        return n
    return -1

s1 = input("string1:")
s2 = input("string2:")

result = first_dif(s1, s2)

if result == -1:
    print("both are identical")
else:
    print("strings are different at first location is:")
    print(result)
