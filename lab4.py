
# 1
first = [i for i in range(1, 6)]
second = [i for i in range(9, 4, -1)]

result = [i * j for i in first for j in second]
print(result)

# 4
first = [1,2,2,4,54,4,2,63,745,4,24,37,45,'4ewt','twenty','34y']
result = []

for i in range(0, len(first), 3):
    result.append(first[i])
print(result)






# 30
# result = list(set(first) & set(second))
# # or
# # result = [x for x in first if x in second]
# print(result)
#
# # 29
# result = list(set(first) ^ set(second))
#
# print(result)
