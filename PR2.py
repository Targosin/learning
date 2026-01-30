import math
x = float(input("Введите переменную Х"))
y = float(input("Введите переменную Y"))
z = float(input("Введите переменную Z"))

print("Выберите задачу введя номер1 или номер4 ")
task_number = str(input())

if task_number == "номер1" :
    left_numerator = 2 * math.cos( x - 2/3)
    print("получим", left_numerator)
    left_denominator = 1/2 + math.sin(x)**2
    print("снизу", left_denominator)
    right_numinator = z**2
    right_denominator = 3 - (z**2)/5
    answer = (left_numerator/left_denominator)*(1+(right_numinator/right_denominator))
    print(answer)