### list
# names = ['Kakashi', 'Minato', 'Naruto', 'Sasuke', 'Itachi']
# print(names[ :2])
# for i in names:
#     print(i)

## print largest number in the list
# numbers = [10, 2, 5, 7, 3, 9]
# max_num = numbers[0]
# for i in numbers:
#     if i > max_num :
#         max_num = i
# print(max_num)

### 2D list
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for row in matrix:
#     for item in row:
#         print(item)
# print(matrix[2][2])

### List methods
# numbers = [5, 2, 1, 7, 4]
# numbers.append(0)  # - this method is used to append the value in the last
# numbers.insert(0, 13) # - this method is used to append the value in a specific location in a list
# numbers.remove(1) # - to remove the value from the list
# print(numbers)
#
# numbers.pop()  # - to remove the last value from the list
# print(numbers)
#
# print(numbers.index(4))  # - to print the first occurrence of the value in the list
#
# print(50 in numbers)  # it will return boolean value
# print (numbers.count(5))
#
# numbers.sort()  # in python 'None' is an Object. it represents absence of value and it will print in the ascending order
# print(numbers)
# numbers.reverse() # print the list in descending order
# print(numbers)
#
# numbers2 = numbers.copy()
# numbers.append(10)
# print('LIST 2')
# print(numbers2)
# print('LIST 1')
# print(numbers)
#
# numbers.clear() # - to remove all the value from the list
# print(numbers)

## write a program to remove the duplicate in a list
# numbers = [2,5,7,9,7,3,6,2]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

### Tuples - it is similar like list but immutable. we can add or remove or change value from tuples
# numbers = (1,2,3)
# print(numbers)

### unpacking - can be used for tuple or list
coordinates = (1, 2, 3)
coordinates[0] * coordinates[1] * coordinates[2]
# or
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
# or (unpacking)
x, y, Z = coordinates


###  Dictionaries use to store (key, value) pair
# customer = {
#     "name" : "John Smith",
#     "age" : 30,
#     "is_verified": True
# }
#
# print(customer['name'])
# print(customer.get('Name','AKil'))
#
# phone =  input('Phone: ')
# digits_mapping = {
#     '1' : 'One',
#     '2' : 'Two',
#     '3': 'Three',
#     '4': 'Four',
#     '5': 'Five',
#     '6': 'Six',
#     '7': 'Seven',
#     '8': 'Eight',
#     '9': 'Nine',
#     '0': 'Zero',
# }
# output = ''
# for ch in phone:
#     output += digits_mapping.get(ch,'!') + ' '
# print(output)

# message = input('>')
# words = message.split(' ')
# emojis = {
#     ':)' : '😀',
#     ':(' : '☹',
#     ':>' : '❤'
# }
# output = ''
# for word in words :
#     output += emojis.get(word, word)
# print(output)

### functions & parameters - By default every functions return 'None'
# def greet_user(name):  # -> parameter is the placeholder or position in function. Here 'name' is the paramter
#     print(f"Hi {name}!")
#     print('Welcome aboard')
#
#
# print('start')
# greet_user('akil') # -> argument is the actual information supplied to the function. Here 'akil' is the argument
# print('finish')

###  Keyword argument
# def greet_user(fname,lname):
#     print(f'Hi {fname} {lname}!')
#     print('Welcome aboard')
#
# print('start')
# greet_user('akil', 'parker')  # positional argument
# greet_user(lname='akil', fname='parker')  # keyword argument
# print('stop')


### return statement - By default every functions return 'None'
# def square(number):
#     return number * number
#
# print(square(17))

### Exception
## exit code 0 --> program success
## exit code 1 --> program failed

try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print('Invalid value')
except ZeroDivisionError:
    print('Age cannot be zero')

###  comments
