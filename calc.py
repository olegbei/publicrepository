def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("На нуль дітити не можна, спробуйте інші числа")
        main()


calc_dict = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
}

def main():
    while True:
        try:
            first_number = float(input('first number -> ').strip())
            second_number = float(input('second_number -> ').strip())
            operation = input('operation -> ' + str(list(calc_dict.keys()))).strip()

        except ValueError:
            print("Не можна вводити строки, введіть число в форматі 4 або 4.0")
            continue

        if operation not in calc_dict.keys():
            print("Ви ввели неправильний оператор, операція почнеться спочатку, введіть один з доступних операторів", calc_dict.keys())
            continue
        res = None

        if operation in calc_dict.keys():
            res = calc_dict[operation](first_number, second_number)  # add(first_number , second_number)
        if res is not None:
            print(res)
        else:
            break

main()
