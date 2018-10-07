from math import sin, log

start = float(input("Input primary x: "))
finish = float(input("Input final x: "))
step = float(input("Input step: "))
n = int((finish - start) / step) + 1
xArray = []
yArray = []

for i in range(n):
    xArray.append(start)
    start += step


def iteration(func1, func2, func3, xArray):
    for x in xArray:
        try:
            if x < 0:
                yield func1(x)
            elif x == 0:
                yield func2(x)
            else:
                yield func3(x)
        except ZeroDivisionError:
            print("Divided by zero, when x = %.2f" % x)
        except ValueError:
            print("Unacceptable value, when x = %.2f" % x)


def solution(func1, func2, func3, xArray):
    yArray = []
    generator = iteration(func1, func2, func3, xArray)
    for y in generator:
        yArray.append(y)
    return yArray


print('\nIf x < 0\n'
      '13. Formula: y=sinx/(x+0.5)\n')
print('If x = 0\n'
      '18. Formula: y=(x-3)^2/(x+1)^2\n')
print('If x > 0\n'
      '18. Formula: y=(x^2+x^3)/lnx\n')
yArray = solution(lambda x: sin(x) / (x + 0.5), lambda x: (x - 3) ** 2 / (x + 1) ** 2, lambda x: (x ** 2 + x ** 3) / log(x), xArray)
print (yArray)
