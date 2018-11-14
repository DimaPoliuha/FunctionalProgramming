# y = sum(i!)


def result(n):
    sum = 0
    for i in range(n + 1):
        sum += fact(i)
    return sum - 1


def fact(i):
    if i < 2:
        return 1
    else:
        return i * fact(i - 1)


print(result(int(input("Input n: "))))
