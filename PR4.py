task_number = str(input('Для выбора задания введите целое число от "1" до "10" :'))
if task_number == '1':
    num_a = int(input('введите число а:'))
    num_b = int(input('введите число b:'))
    for i in range(num_a, num_b+1):
        print(i, end=';')

if task_number == '2':
    num_a = int(input('введите число а:'))
    num_b = int(input('введите число b:'))
    if num_a < num_b:
        for i in range(num_a, num_b+1):
            print(i, end=';')
    else:
        for i in range(num_a, num_b-1, -1):
            print(i, end=';')

if task_number == '3':
     num_a = int(input('введите число а:'))
     num_b = int(input('введите число б:'))
     for i in range(num_a, num_b - 1, -1):
         if i % 2 != 0:
             print(i)

if task_number == '4':
     n = int(input('введите количество чисел:'))
     summ = 0
     for _ in range(n):
         summ += int(input('Введите число:'))
     print(summ)

if task_number == '5':
     n = int(input('введите число:'))
     summ = 0
     for i in range(1, n + 1):
         summ += i ** 3
     print(summ)

if task_number == '6':
     n = int(input('введите число n:'))
     fact = 1
     for i in range(1, n + 1):
         fact *= i
     print(fact)

if task_number == '7':
     n = int(input('введите число n:'))
     summ = 0
     fact = 1
     for i in range(1, n + 1):
         fact *= i
         summ += fact
     print(summ)

if task_number == '8':
     n = int(input('введите число n:'))
     for i in range(1, n + 1):
         for o in range(1, i + 1):
             print(o, end='')
     print()

if task_number == '9':
     n = int(input('введите число n:'))
     a, b = 0, 1
     summ = 0
     for i in range(n):
         summ += a
         a, b = b, a + b
     print(summ)

if task_number == '10':
     n = int(input('введите число n:'))
     k = int(input())
     a, b = 0, 1
     count = 0
     summ = 0
     while count < n + k - 1:
         if count >= k - 1:
             summ += a
             a, b = b, a + b
             count += 1
     print(summ)