# print('I am Akil')
# print('o----')
# print(' ||||')
# print("*" * 10) #expression
#
# #variables
# price = 10
#
# #price = '20'
# print(price)
#
# #excersice
# name = 'John smith'
# age = 20
# is_new_patient = False
#
# if(is_new_patient):
#      print("he is new patient")
# else:
#     print("he is not new patient")
### receive input
# name = input('What is your name? ')
# color = input("What's your favourite color? ")
# print(name+ " likes "+color+"!!")
# if(color != 'yellow'):
#     print("he is yellow ranger")
# else:
#     print("he is red ranger")

# birth_year = input('Birth year: ')
# print(type(birth_year))
# age = 2022 - int(birth_year)
# print(type(age))
# print(age)
# convert stringt to float/int
# weight_lbs = input('Weight (lbs): ')
# weight_kg = float(weight_lbs) * 2.2
# print(weight_kg)

### String
# name = "Naruto"
# print(name[1:-1])

### formatted string
# first_name = 'John '
# last_name = 'Smith'
# message = first_name + '['+ last_name +'] is a coder'
# msg = f'{first_name}[{last_name}] is a coder'
# print(message)
# print(msg)

### string method
# course = 'Python for beginners'
# len()
# course.upper()
# course.lower()
# course.find()
# course.replace()
# print(course.title())
# print(course.replace('beginners','Expert'))
# isPresent = 'Python' in course
# print(isPresent)

### arithmetic operation
# print(10 + 3)  #addition
# print(10 - 3)  #subraction
# print(10 * 3)  #multiplication
# print(10 / 3)  #divide  - returns a floating point number
# print(10 // 3) #division - returns a int number
# print(10 % 3)  #modulus - returns the reminder
# print(10 ** 3) #exponent - return the number with resp to the power

## Augmented assignment operator
# x=10
# x += 3
# print(x)

### Operator precedence
## orders
# parenthesis
# exponentiation - 2 ** 3
# multiplication or division
# addition or subtraction

# x = (10 + 3) * 2 ** 2
# print(x)

### math functions
# import math  # -> import statement for math operator
# x = 2.4
# print(round(x))   # it will always return the number as whole
# print(abs(-2.5))  # it will return the negative value as positive
# print(math.floor(2.9)) # it will return the floor value
# print(math.ceil(2.9)) # it will return the round value

### if statements
### logical operator(AND, OR, NOT)
# has_high_income = True
# has_good_credit = True
# has_criminal_record = True
#
# if has_high_income and  has_good_credit:
#     print("Eligible for loan")
#
#
# if has_high_income and  not has_criminal_record:
#     print("Eligible for loan")

### comparison operator(>, < ,==, >= ,<=)
# temperatur = 30
#
# if temperatur > 30:
#     print("It's not a hot day")
# else:
#     print("It's not a hot day")

# name = input("Enter your name: ")
# if len(name) < 3:
#     print("name must be at least 3 character")
# elif len(name) > 50:
#     print('Name can be maximum of 50 characters')
# else:
#     print('Name looks good!')

### while loops
# i = 1
# while i <=5:
#     print('*' * i)
#     i += 1
#
# j = 5
# while j >=1:
#     print('*' * j)
#     j -= 1
# print('Done')

### For loop

# for i in ['Python', 'Java', 'C++']:
#     print(i)
# for i in [1,2,3,4,5,6,7,8,9,10]:
#     print(i)
# for i in range(1,11):
#     print(i)
# for i in range(0,11,2):
#     print(i)

# prices = [10,20,30]
# total_price = 0
# for price in prices:
#     total_price += price
# print(f"total price {total_price}")

### nested loops
# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')

## multiply string with int
# numbers = [5, 2, 5, 2, 2]
# for i in numbers:
#     print('X' * i)

## form a 'F' using nested loop
numbers = [2, 2, 2, 2, 7]

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'X'
    print(output)