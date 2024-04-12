a = input('Введите число: ')
if a.isdigit():
    print(f'Введено целое число: {a}')
else:
    while not a.isdigit():
        a = input('Ошибка. Попробуйте еще раз. Введите число: ')
    print(f'Введено верное число: {a}')
