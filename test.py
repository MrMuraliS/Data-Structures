def func(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    print(sum)

func(1000) # O(n)


def func2(n):
    return (n * (n+1))/2

print(func2(1000)) # O(1)