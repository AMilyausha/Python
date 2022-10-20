def Fib(n):
    if n in [1, 2]:                       
        return 1
    else:
        return Fib(n-1) + Fib(n-2)

def NegaFib(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2

list = [0]
Number = int(input('Введите число: '))
for i in range(1, Number + 1):
    list.append(Fib(i))
    list.insert(0, NegaFib(i))
print(list)