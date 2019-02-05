first_number = int(input('Please enter your first number: '))

# print('Целое =', int(first_number))
# print('Вещественое =', float(first_number))
# print('Логическое =', bool(first_number))
# print('Cтрока =', str(first_number))

second_number = int(input('Please enter your second number: '))

print('Целое + Целое =', int(first_number) + int(second_number))
print('Целое + Вещественое =', int(first_number) + float(second_number))
print('Целое + Логическое =', int(first_number) + bool(second_number))
print('Целое + Строка = Нельзя')

print('Целое * Целое =', int(first_number) * int(second_number))
print('Целое * Вещественое =', int(first_number) * float(second_number))
print('Целое * Логическое =', int(first_number) * bool(second_number))
print('Целое * Строка =', int(first_number) * str(second_number))

print('Вещественое + Вещественое =', float(first_number) + float(second_number))
print('Вещественое + Логическое =', float(first_number) + bool(second_number))
print('Вещественое + Строка = Нельзя')

print('Вещественое * Вещественое =', float(first_number) * float(second_number))
print('Вещественое * Логическое =', float(first_number) * bool(second_number))
print('Вещественое * Строка = Hельзя')

print('Логическое + Логическое =', bool(first_number) + bool(second_number))
print('Логическое + Строка = Нельзя')


print('Строка + Строка', str(first_number) + str(second_number))







