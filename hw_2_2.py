
first1 = 1
first2 = 1


while True:
    number = input("Вводите порядковый номер Числа Фибоначчи")
    if not number.isdigit():
        print("Вы ввели не целое число. Попробуйте снова: ")

    elif number.isdigit():
        number = int(number)
        i = 0
        while i < number - 2:
            fib_sum = first1 + first2
            first1 = first2
            first2 = fib_sum
            i = i + 1

        print("Элемент [", number ,'] ряда Чисел Фибоначчи =', first2)
        break




