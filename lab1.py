from math import sin

start = float(input("Input primary x: "))
finish = float(input("Input final x: "))
step = float(input("Input step: "))
n = int((finish - start) / step) + 1
xArray = []

for i in range(n):
    xArray.append(start)
    start += step


def iteration(func, xArray):
    for x in xArray:
        try:
            yield func(x)
        except ZeroDivisionError:
            print("Divided by zero, when x = %.2f" %x)
        except ValueError:
            print("Unacceptable value, when x = %.2f" %x)


def solution(func, xArray):
    yArray = []
    generator = iteration(func, xArray)
    for y in generator:
        yArray.append(y)
    return yArray


print('\n13. Formula: y=sinx/(x+0.5)\n')
y = solution(lambda x: sin(x) / (x + 0.5), xArray)
print(y)

print('\n\n18. Formula: y=(x-3)^2/(x+1)^2\n')
y = solution(lambda x: (x - 3) ** 2 / (x + 1) ** 2, xArray)
print(y)







# print('\n13. Formula: y=sinx/(x+0.5)\n')
#
# x = start
#
# for i in range(n):
#     print("x: %f" % x)
#     try:
#         print("y: %f" % solution(lambda x: sin(x) / (x + 0.5), x))
#     except ZeroDivisionError:
#         print("Divided by zero")
#     except ValueError:
#         print("Unacceptable value")
#     x += step
#
# print('\n\n18. Formula: y=(x-3)^2/(x+1)^2\n')
#
# x = start
#
# for i in range(n):
#     print("x: %f" % x)
#     try:
#         print("y: %f" % solution(lambda x: (x - 3)  2 / (x + 1)  2, x))
#     except ZeroDivisionError:
#         print("Divided by zero")
#     x += step
#
# print('\n\n30. Formula: y=(x^2+x^3)/lnx\n')
#
# x = start
#
# for i in range(n):
#     print("x: %f" % x)
#     try:
#         print("y: %f" % solution(lambda x: (x  2 + x  3) / log(x), x))
#     except ZeroDivisionError:
#         print("Divided by zero")
#     except ValueError:
#         print("Unacceptable value")
#     x += step
