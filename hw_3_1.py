
a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))


def check(a,b):
    if a > b:
        a, b = b, a
        return a, b
    elif a < b:
        a , b = a , b
        return a, b

def sum_natural_numbers(a, b):
    sum_ = 0

    if a < 0 and b < 0:
        print("Сума двох натуральних чисел = 0")

    elif a == b:
        a = int(a)
        b = int(b)
        sum_ = a + b

    elif a < b:
        if a < 0:
            a = int(a)
            b = int(b)
            for i in range(b + 1):
                sum_ += i
                print('Оце ціле число входить', i)

        elif float(a) > int(a):  # обрізаємо десяті
            a = int(a)
            b = int(b)
            for i in range(a + 1, b + 1):
                sum_ += i
                print('Оце ціле число входить', i)

        else:
            a = int(a)
            b = int(b)
            for i in range(a, b + 1):
                sum_ += i
                print('Оце ціле число входить', i)


    elif a > b:
        if b < 0:
            a = int(a)
            b = int(b)
            for i in range(a + 1):
                sum_ += i
                print('Оце ціле число входить', i)

        elif float(b) > int(b):  # обрізаємо десяті
            x = int(b)  # вводимо нові переміні, для їх заміни
            y = int(a)
            for i in range(x + 1, y + 1):
                sum_ += i
                print('Оце ціле число входить', i)

        else:
            x = int(b)  # вводимо нові переміні, для їх заміни
            y = int(a)
            for i in range(x, y + 1):
                sum_ += i
                print('Оце ціле число входить', i)
    return sum_


if a and b:
    print('Сумма натуральных чисел в диапазоне от', check(a, b), '>>> ', sum_natural_numbers(a,b) )

