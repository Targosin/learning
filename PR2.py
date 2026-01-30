import math
x = float(input("Введите переменную Х"))
y = float(input("Введите переменную Y"))
z = float(input("Введите переменную Z"))

task_number = str(input('Выберите задачу введя "номер1" или "номер4":'))

if task_number == "номер1" :
    left_numerator = 2 * math.cos( x - 2/3)
    print("получим", left_numerator)
    left_denominator = 1/2 + math.sin(x)**2
    print("снизу", left_denominator)
    right_numinator = z**2
    right_denominator = 3 - (z**2)/5
    answer = (left_numerator/left_denominator)*(1+(right_numinator/right_denominator))
    print(answer)

if task_number == "номер4" :
    right_power = 1 + (2*((math.sin(y))**2))
    right_down_side = abs(math.cos(x) - math.cos(y))
    right_side = right_down_side**right_power
    left_side = 1 + z + ((z**2)/2) + ((z**3)/2) + ((z**4)/2)
    answer = right_side*left_side
    print(answer)