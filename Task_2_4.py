# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры .

from random import randint
numbers = []
for i in range(10):
    numbers.append(randint (-10,10)) # заполнение списка случайными числами
print(numbers)

x = int(input('Введите позицию первого элемента: '))
y = int(input('Введите позицию второго элемента: '))

for i in range(len(numbers)):
    mult = numbers[x]*numbers[y]
print(f'Произведение элементов: {numbers[x]} * {numbers[y]} =', mult)