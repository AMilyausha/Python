# Задайте последовательность цифр. Напишите программу, 
# которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

lst = list(map(int, input("Введите числа через пробел:\n").split()))
new_list = []

for i in lst:
    count = 0
    for j in lst:
        if i == j:
            count +=1
    if count == 1:
        new_list.append(i)
print(new_list)