# Напишите программу, которая по заданному номеру четверти, показывает
# диапазон возможных координат точек в этой четверти (x и y).
num = int (input("Введите номер четверти от 1 до 4: "))
def f(num):
    if num == 1:
        return 'x > 0, y > 0'
    elif num == 2:
         return 'x < 0, y > 0'
    elif num == 3:
         return 'x < 0, y < 0'
    elif num == 4:
         return 'x > 0, y < 0'
    else:
         return 'Введите от 1 до 4'
print(f(num))

