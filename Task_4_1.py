# Вычислить число Пи c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

a = 1
sum = 0
for i in range ( 1000000):
    if i % 2 == 0 :
        sum = sum + 4 / a
    else :
        sum = sum - 4 / a
    a =a + 2

d= 0.00001
b = 3+ int((sum - int(sum)) * (1/d))/(1/d)
print(b)