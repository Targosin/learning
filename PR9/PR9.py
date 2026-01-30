
with open('ShDA_ZIT252_vvod.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline().strip())
    m = []
    for _ in range(n):
        line = file.readline().strip()
        row = list(map(int, line.split()))
        m.append(row)

t = sum(m[0])
ok = True
for row in m:
    if sum(row) != t: 
        ok = False

for j in range(n):
    if sum(m[i][j] for i in range(n)) != t: 
        ok = False

if sum(m[i][i] for i in range(n)) != t: 
    ok = False

if sum(m[i][n-1-i] for i in range(n)) != t: 
    ok = False

with open('ShDA_ZIT252_vivod.txt', 'w', encoding='utf-8') as file:
    result = "магический" if ok else "не магический"
    file.write(result)
    
# вывод результатa в консоль
print(f"Результат: {result}")
print(f"Результат записан в файл 'ShDA_ZIT252_vivod.txt'")