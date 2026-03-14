def number_of_factor(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
            print(i)
    return count

num = int(input("enter a number: "))
print("number of factors:", number_of_factor(num))
