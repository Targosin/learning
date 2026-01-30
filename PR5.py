task_number = str(input('Для выбора задания введите целое число от "1" до "15" :'))
if task_number == '1':
    text = input()
    words = text.split()
    count = sum(1 for w in words if w[0].lower() == 'е')
    print(count)

if task_number == '2':
    text = input()
    new = text.replace(':', '%')
    print(new)
    print(text.count(':'))

if task_number == '3':
    text = input()
    new = text.replace('.', '')
    print(new)
    print(text.count('.'))

if task_number == '4':
    text = input()
    new = text.replace('а', 'о').replace('А', 'О')
    print(new)
    print(text.count('а') + text.count('А'))
    print(len(text))

if task_number == '5':
    text = input()
    print(text.lower())

if task_number == '6':
    text = input()
    new = text.replace('а', '').replace('А', '')
    print(new)
    print(text.count('а') + text.count('А'))

if task_number == '7':
    text = input()
    n = len(text)
    res = list(text)
    for i in range(n // 2):
        if res[i].lower() == 'п':
            res[i] = '*'
    print(''.join(res))

if task_number == '8':
    text = input()
    words = text.rstrip('.').split()
    print(len(words))

if task_number == '9':
    text = input()
    word = input()
    print(text.lower().split().count(word.lower()))

if task_number == '10':
    text = input()
    print(' '.join(w.capitalize() for w in text.split()))

if task_number == '11':
    text = input()
    max_len = 0
    curr = 0
    for ch in text:
        if ch == 'н':
            curr += 1
            max_len = max(max_len, curr)
        else:
            curr = 0
    new = text.replace('!', '.')
    print(max_len)
    print(new)

if task_number == '12':
    text = input()
    for w in text.split():
        if w.endswith('я'):
            print(w)

if task_number == '13':
    text = input()
    start = text.find('(')
    end = text.find(')')
    if start != -1 and end != -1:
        print(text[start + 1:end])

if task_number == '14':
    text = input()
    for w in text.split():
        if w[0].lower() == 'а':
            print(w)
    for w in text.split():
        if w[-1].lower() == 'я':
            print(w)

if task_number == '15':
    text = input()
    print(text.lower().count('т'))