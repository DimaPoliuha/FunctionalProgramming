m = int(input("Input m: "))
n = int(input("Input n: "))
result = []


def solution(m, n):
    for i in range(m):
        for j in range(n):
            try:
                yield (1 / i ** j)
            except ZeroDivisionError:
                print("Divided by zero, when i = %i; j = %i" % (i, j))


print("13. y = sum(sum(1/i^j))")
generator = solution(m, n)
for i in generator:
    result.append(i)
print(result)
