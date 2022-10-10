import csv
import os
import time

# Задание №1
red = '\x1b[41m'
white = '\x1b[47m'
blue = '\x1b[44m'
stop = '\x1b[0m'
probel = 35 * ' '
print(f'{red}{probel}{stop}\n{white}{probel}{stop}\n{blue}{probel}{stop}')
print(f'{blue}{probel}{stop}\n{white}{probel}{stop}\n{red}{probel}{stop}')
print()

# Задание №2

black = '\x1b[40m'
print('Введите количество повторений:')
number = input()
n = int(number)
for i in range(2):
    probel_1 = 24 * ' '
    print(n * f'{white}{probel_1}{stop}{black}  {stop}{white}{probel_1}{stop}')

k1 = 22
for i in range(3):
    probel_1 = k1 * ' '
    probel_2 = (50 - 2 * k1 - 4) * ' '
    print(n * f'{white}{probel_1}{stop}{black}  {stop}{white}{probel_2}{stop}{black}  {stop}{white}{probel_1}{stop}')
    k1 -= 2
k1 = 15
for i in range(3):
    probel_1 = k1 * ' '
    probel_2 = (50 - 2 * k1 - 6) * ' '
    print(n * f'{white}{probel_1}{stop}{black}   {stop}{white}{probel_2}{stop}{black}   {stop}{white}{probel_1}{stop}')
    k1 -= 3
k1 = 5

probel_1 = k1 * ' '
probel_2 = (50 - 2 * k1 - 8) * ' '
print(n * f'{white}{probel_1}{stop}{black}    {stop}{white}{probel_2}{stop}{black}    {stop}{white}{probel_1}{stop}')
k1 -= 4

probel_2 = 40 * ' '
print(n * f'{black}     {stop}{white}{probel_2}{stop}{black}     {stop}')

print()

# Задание №3
a = []
for i in range(10):
    a.append([])
    for j in range(28):
        a[i].append(0)

for j in range(28):
    a[9][j] = j / 3

for i in range(10):
    a[i][0] = round(1 - i * 1 / 9, 2)

a[0][3] = 10
for i in range(1, 9):
    for j in range(3, 28):
        if (a[i][0] - 1 / a[9][j]) >= (1 / a[9][j] - a[i + 1][0]):
            a[i][j] = -10
        else:
            if a[i - 1][j] == -10:
                a[i][j] = 10

for i in range(0, 9):
    cline = ''
    for j in range(3, 28):
        if a[i][j] == 10:
            cline += f'{black} {stop}'
        else:
            cline += f'{white} {stop}'
    if int(a[i][0]) == 1:
        print('1.00', cline)
    else:
        print(a[i][0], cline)

lline = ''
for j in range(28):
    if a[9][j] % 3 == 0:
        lline += str(a[9][j]) + '      '
print(lline)

print()

# Задание №4
rows = []
with open('C:/Users/79210/PycharmProjects/Lab_2/books.csv') as r_file:
    file_reader = csv.reader(r_file, delimiter=';')
    for row in file_reader:
        rows.append(row)
min = 0
max = 0
for row in rows:
    if (row[7] != 'Цена поступления') and (float(row[7][:-3]) <= 50):
        min += 1
    elif (row[7] != 'Цена поступления') and (float(row[7][:-3]) > 50):
        max += 1

if max > min:
    otn = round(max / min)
    print('Книги дороже 50')
    print(max, otn * f'{red}  {stop}')
    print('Книги до 50')
    print(min, f'{blue}  {stop}')
else:
    otn = round(min / max)
    print('Книги до 50')
    print(min, otn * f'{red}  {stop}')
    print('Книги дороже 50')
    print(max, f'{blue}  {stop}')

print()
f = open('C:/Users/79210/PycharmProjects/Lab_2/Animation.txt')
for i in range(4):
    for j in range(5):
        print(f.readline(), end='')
    time.sleep(1)
    os.system("cls")
f.close()

input()