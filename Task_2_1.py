# Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11 
a = input('Введите число: ')
resultat = 0
element = 0
for i in range(0,len(a)):
    element=a[i]
    if element == '.':
        continue
    resultat =resultat+int(element)
print(resultat)

