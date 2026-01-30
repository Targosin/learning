task_number = str(input('Для выбора задания введите целое число от "1" до "15" :'))
if task_number == '1':
    n = int(input('Введите количество элементов:'))
    arr = [int(input('Введите элемент:')) for _ in range(n)]
    print(max(arr))
    arr.reverse()
    print(arr)

if task_number == '2':
    n = int(input('Введите количество элементов:'))
    arr = [int(input('Введите элемент:')) for _ in range(n)]
    print('минимальный:', min(arr))
    print('индекс:', arr.index(min(arr)))

if task_number == '3':
    n = int(input('Введите количество элементов:'))
    D = [int(input('Введите элемент:')) for _ in range(n)]
    s = sum(D[i] for i in range(1, n, 2))
    print(D)
    print(s)

if task_number == '4':
    arr = [int(input('Введите элемент:')) for _ in range(6)]
    print(max(arr))
    print(arr.index(max(arr)))

if task_number == '5':
    arr = [int(input('Введите элемент:')) for _ in range(10)]
    for i in range(9):
        if arr[i] < 0 and arr[i + 1] < 0:
            print(arr[i], arr[i + 1])

if task_number == '6':
    arr = [int(input('Введите элемент:')) for _ in range(10)]
    m = max(arr)
    less = sum(1 for x in arr if x < m)
    greater = sum(1 for x in arr if x > m)
    print(less)
    print(greater)

if task_number == '7':
    n = int(input('Введите количество элементов:'))
    arr = [int(input('Введите элемент:')) for _ in range(n)]
    even_sum = sum(arr[i] for i in range(0, n, 2))
    odd_prod = 1
    for i in range(1, n, 2):
        odd_prod *= arr[i]
    print(even_sum)
    print(odd_prod)

if task_number == '8':
    arr = [int(input('Введите элемент:')) for _ in range(6)]
    print(sum(arr))
    prod = 1
    for x in arr:
        prod *= x
    print(prod)

if task_number == '9':
    n = int(input('Введите количество элементов:'))
    arr = [int(input('Введите элемент:')) for _ in range(n)]
    print(min(abs(x) for x in arr))
    print(arr[::-1])

if task_number == '10':
    arr = [int(input('Введите элемент:')) for _ in range(8)]
    seen = set()
    dups = []
    for x in arr:
        if x in seen and x not in dups:
            dups.append(x)
        seen.add(x)
    print(dups if dups else "нет")

if task_number == '11':
    arr = [int(input('Введите элемент:')) for _ in range(10)]
    even = [x for x in arr if x % 2 == 0]
    print(max(even) if even else "нет")

if task_number == '12':
    arr = [int(input('Введите элемент:')) for _ in range(10)]
    odd = [x for x in arr if x % 2 != 0]
    print(min(odd) if odd else "нет")

if task_number == '13':
    arr = [int(input('Введите элемент:')) for _ in range(8)]
    d = {}
    for i, x in enumerate(arr):
        if x in d:
            d[x].append(i)
        else:
            d[x] = [i]
    for k, v in d.items():
        if len(v) > 1:
            print(k, v)

if task_number == '14':
    arr = [int(input('Введите элемент:')) for _ in range(10)]
    mi = arr.index(min(arr))
    ma = arr.index(max(arr))
    arr[mi], arr[ma] = arr[ma], arr[mi]
    print(arr)

if task_number == '15':
    arr = [int(input('Введите элемент:')) for _ in range(10)]
    seen = set()
    dups = []
    for x in arr:
        if x in seen and x not in dups:
            dups.append(x)
        seen.add(x)
    print(dups)