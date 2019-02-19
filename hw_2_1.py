a = float(input("Please enter a number 1 "))
b = float(input("Please enter a number 2 "))

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

    elif float(a)> int(a): # обрізаємо десяті
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

    elif float(b) > int(b): #обрізаємо десяті
        x = int(b) # вводимо нові переміні, для їх заміни
        y = int(a)
        for i in range(x +1, y + 1):
            sum_ += i
            print('Оце ціле число входить', i)

    else:
        x = int(b)# вводимо нові переміні, для їх заміни
        y = int(a)
        for i in range(x, y + 1):
            sum_ += i
            print('Оце ціле число входить', i)

print("Сума двох натуральних чисел", sum_)






































