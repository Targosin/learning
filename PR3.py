import math
def split_even_odd_basic(number):   
    number_str = str(abs(number)) 
    even_digits = []
    odd_digits = []
    
    for digit_char in number_str:
        digit = int(digit_char)
        if digit % 2 == 0:
            even_digits.append(digit)
        else:
            odd_digits.append(digit)
    
    return even_digits, odd_digits


def is_prime_basic(n): #Эт у нас функция для проверки простоты
    if n <= 1:
        return print(n, 'не простое')
    for i in range(2, n):  
        if n % i == 0:
            return print(n, 'не простое')
    return print(n, 'простое')

def triangle_area_heron(number_a, number_b, munber_c):
    # Проверка на существование треугольника
    if number_a <= 0 or number_b <= 0 or number_c <= 0:
        raise ValueError("Длины сторон должны быть положительными")
    # Проверка неравенства треугольника
    if (number_a + number_b <= number_c) or (number_a + number_c <= number_b) or (number_b + number_c <= number_a):
        raise ValueError("Треугольник с такими сторонами не существует")
    p = (number_a + number_b + number_c) / 2
    area = math.sqrt(p * (p - number_a) * (p - number_b) * (p - number_c))
    return area

task_number = str(input('Для выбора задания введите целое число от "0" до "18" :'))
if task_number == '0':
    number_a = int(input("Введите число А"))
    number_b = int(input("Введите число B"))
    number_c = int(input("Введите число С"))
    if number_a < 1 :
        print(number_a, "не подходит")
    elif number_a > 3 :
        print(number_a, "не подходит")
    else:
        print(number_a, "подходит")

    if number_b < 1 :
        print(number_b, "не подходит")
    elif number_b > 3 :
     print(number_b, "не подходит")
    else:
        print(number_b, "подходит")

    if number_c < 1 :
        print(number_c, "не подходит")
    elif number_c > 3 :
        print(number_c, "не подходит")
    else:
        print(number_c, "подходит")

elif task_number == '1':
    number_a = int(input('Введите число а:'))
    number_b = int(input('Введите число b:'))
    print(max(number_a, number_b))

elif task_number == '2':
    number_a = int(input('введите число:'))
    if number_a % 2 == 0:
        print(number_a, 'четное')
    else:
        print(number_a, 'нечётное')

elif task_number == '3':
    num = int(input('введите число'))
    even, odd = split_even_odd_basic(num)
    print(f"Число: {num}")
    print(f"Четные цифры: {even}")
    print(f"Нечетные цифры: {odd}")

elif task_number == '4':
    print(is_prime_basic(int(input('Введите число'))))

elif task_number =='5':
    number_a = int(input('число а:'))
    number_b = int(input('число b:'))
    number_c = int(input('число с:'))
    answer = (number_a + number_b + number_c)/3
    print(answer)

elif task_number == '6':
    number_a = int(input('введите число:'))
    if number_a % 7 == 0 :
        print(number_a, 'кратно 7-ми')
    else:
        print(number_a, 'не кратно 7-ми')

elif task_number == '7':
    year = int(input('введите год:'))
    if year % 100 == 0 :
        if year % 400 == 0:
            print(year, 'високосный')
        else:
            print(year, 'не високосный')
    elif year % 4 == 0 :
        print(year, 'високосный')
    else:
        print(year, 'не високосный')

elif task_number == '8':
    number = str(input('Введите номер месяца в формате "01" "11" и.т.д:'))
    if number in('01', '03', '05', '07', '08', '10', '12'):
        print('31 день')
    elif number in('04', '06', '09', '11'):
        print('30 дней')
    elif number == '02':
        year_status = str(input('Год високосный? ответьте "да" или "нет":'))
        if year_status == 'да':
            print('29 дней')
        elif year_status == 'нет':
            print('28 дней')
        else:
            print('неверный формат ввода данных')
    else:
        print('неверный формат ввода данных')

elif task_number == '9':
    number_a = float(input('число а:'))
    number_b = float(input('число b:'))
    number_c = float(input('число c:'))
    area = triangle_area_heron(number_a, number_b, number_c)
    print(f"Площадь треугольника со сторонами {number_a}, {number_b}, {number_c}: {area:.2f}")

elif task_number == '10':
    number_a = int(input('число а:'))
    number_b = int(input('число b:'))
    number_c = int(input('число с:'))
    if number_a == number_b:
        if number_a == number_c:
            print('числа', number_a,',',number_b,',', number_c, '- равны')
        else:
            print(number_a, number_b, 'и', number_c, 'не равны')
    else:
        print(number_a, number_b, 'и', number_c, 'не равны')

elif task_number == '11':
    user_age = input('введите ваш возраст')
    print('вам', user_age)

elif task_number == '12':
    number_a = int(input('введите число:'))
    if number_a < 0 :
        print('(', number_a, ')', '- отрицательное')
    else:
        print(number_a, '- положительное')

elif task_number == '13':
     year = int(input('введите год:'))
     if year % 100 == 0 :
        if year % 400 == 0:
             print(year, 'високосный, а в феврале 29 дней')
        else:
             print(year, 'не високосный, а в феврале 28 дней')
     elif year % 4 == 0 :
         print(year, 'високосный, а в феврале 29 дней')
     else:
         print(year, 'не високосный, а в феврале 28 дней')

elif task_number == '14':
     x = float(input("Введите координату x: "))
     y = float(input("Введите координату y: "))

     if 0 <= x <= 5 and 0 <= y <= 5:
         print(f"Точка ({x}, {y}) принадлежит квадрату")
     else:
         print(f"Точка ({x}, {y}) НЕ принадлежит квадрату")

elif task_number == '15':
     number_a = int(input('число а:'))
     number_b = int(input('число b:'))
     print ('a + b =', number_a + number_b)
     print ('a - b =', number_a - number_b)

elif task_number == '16':
     number_a = int(input('число а:'))
     if number_a % 3 == 0 :
         if number_a % 5 == 0 :
             print(number_a, 'кратно и 3-ём и 5-ти')
         else:
             print(number_a, 'кратно 3-ём, но не кратно 5-ти')
     elif number_a % 5 == 0 :
         print(number_a, 'кратно 5-ти, но не кратно 3-ём')
     else:
         print(number_a, 'не кратно ни 3-ём, ни 5-ти')

elif task_number == '17':
     year = int(input('введите год:'))
     if year % 100 == 0 :
         print(year, '- вековой')
     else:
         print(year, '- не вековой')

elif task_number == '18':
     number_a = float(input('Введите число:'))
     if number_a == int(number_a):
         print(number_a, '- целое число.')
     else:
         print(number_a, '- дробное число.')