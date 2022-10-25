# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень 
# следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 
# просто пропускаем данную итерацию степени
# Записываем результат в файл.

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0
import random

A = random.randint(0, 100)
B = random.randint(0, 100)
C = random.randint(0, 100)
k = 2

with open("Task4.txt", "w") as Task4:
    print(f'A = {A}, B = {B}, C = {C}', file=Task4)
    if B != 0 or C != 0:
        print(f'{A}*x^{k} + {B}*x + {C} = 0', file=Task4)
    if B == 0 and C != 0:
        print(f'{A}*x^{k} + {C} = 0', file=Task4)
    if B == 0 and C == 0:
        print(f'{A}*x^{k} = 0', file=Task4)


