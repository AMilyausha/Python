# Задайте список из вещественных чисел. Напишите 
# программу, которая найдёт разницу между максимальным
#  и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]
max = 0
min = list[0]
for i in range (0,len(list)):
    if list[i]- int(list[i]) < min:
        min = list[i]- int(list[i])
    if list[i]- int(list[i]) > max:
        max = list[i]- int(list[i])
print(max-min)


