a = input('Введите число: ')
if a.isdigit() and len(a) == 5:
    a = int(a)
    if a // 10000 == a % 10 and a % 10000 // 1000 == a % 100 // 10:
         print(f'{a} - палиндром')
    else:
        print(f'{a} - не палиндром')
else:
     print('Введено не число или количество разрядов не равно 5')