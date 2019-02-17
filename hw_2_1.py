a = float(input("Please enter a number 1"))
b = float(input("Please enter a number 2"))

sum = 0

if a < b:
    if float(a)> int(a): # обрізаємо десяті
        a = int(a)
        b = int(b)
        for i in range(b + 1):
            sum += i
            print('Оце ціле число входить', i)

    else:
        a = int(a)
        b = int(b)
        for i in range(b + 1):
            sum += i
            print('Оце ціле число входить', i)

elif a == b:
    a = int(a)
    b = int(b)
    sum = a + b

elif a > b:
    if float(b) > int(b): #обрізаємо десяті
        x = int(b) # вводимо нові переміні, для їх заміни
        y = int(a)
        for i in range(y + 1):
            sum += i
            print('Оце ціле число входить', i)

    else:
        x = int(b)# вводимо нові переміні, для їх заміни
        y = int(a)
        for i in range(y + 1):
            sum += i
            print('Оце ціле число входить', i)

print("Сума двох натуральних чисел", sum)






































