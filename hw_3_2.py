

n = input("Вводите порядковый номер Числа Фибоначчи")


def validate_number(input_num):
    num_ok = True
    for x in input_num:
        if (x.isdigit()):
            pass
        else:
            num_ok = False
    return num_ok


def get_fibonachi(n):
    first1 = 1
    first2 = 1
    while True:
        if not n.isdigit():
            print("Вы ввели не целое число. Попробуйте снова: ")
            break

        elif n.isdigit():
            n = int(n)
            i = 0
            while i < n - 2:
                fib_sum = first1 + first2
                first1 = first2
                first2 = fib_sum
                i = i + 1

            print("Элемент [", n ,'] ряда Чисел Фибоначчи =', first2)
            break


if validate_number(n):
    get_fibonachi(n)
else:
    print('Неверный формат ввода данных!')

