# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.
n = int (input('Введите число:'))
list = []
a = 2
for i in range(1,n):
    if n % 2 == 0:
        list = list + [2]
        n = n //2 
    elif n % 3 == 0:
        list = list + [3]
        n = n //3
    elif n % 5 == 0:
        list = list + [5]
        n = n // 5
    elif n % 7 == 0:
        list = list + [7]
        n = n // 7
    else:
        print(list)
        break