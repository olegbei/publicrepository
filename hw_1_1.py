first_name = input('Please enter your first name ')
second_name = input('Please enter your second name ')

a = "Hello"
print("{0} {1} {2}".format(a, first_name, second_name))

birthday = int(input('Please enter your day of birth '))
birth_month = int(input('Please enter your birth month '))
birth_year = int(input('Please enter your birth year '))

amount_of_years = 2019 - birth_year - 1
amount_of_months = (amount_of_years * 12) + birth_month

#знаходимо кількість днів, яка лишилась до кінця першого року після народження
amount_of_days_till_the_end_the_first_year = 365 - ((30 - birthday) + (12 - birth_month)*30)
#знаходимо кількість років, які лишились до початку курсу
number_of_years_till_the_start = 2019 - birth_year - 1


#тут знаходимо кількість днів до 01.01.2019 і додаємо 31 день нового року
amount_of_days_till_the_start = number_of_years_till_the_start * 12 * 30 + amount_of_days_till_the_end_the_first_year + 31


print("You are", amount_of_years)
print("You've been living for", amount_of_months, 'months')
print("You've been living for", amount_of_days_till_the_start, "days or", number_of_years_till_the_start * 12 + 1, 'full months or', number_of_years_till_the_start , "full years till the start of this lesson" )



