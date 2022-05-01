### class & constructor
# we use Pascal conversion for class name

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print('Move')
#
#     def draw(self):
#         print('draw')
#
#
# point = Point(10, 20)
# point.x = 11
# print(point.x)
#
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print(f'Hi, I am {self.name}')

# person = Person('akil')
# person.talk()

### Inheritance

# class Animal:
#     def walk(self):
#         print('Walk')
#
# class Dog(Animal):
#     pass
#
# class Cat(Animal):
#     pass
# dog = Dog()
# dog.walk()

### modules
# import convertor
# from convertor import kg_to_lbs
# print(convertor.lbs_to_kg(70))
# print(kg_to_lbs(70))

### packages

##  Three way of importing a package
# import ecommerce.shipping
# from ecommerce.shipping import calc_shipping
# from ecommerce import shipping
#
# ecommerce.shipping.calc_shipping()
# calc_shipping()
# shipping.calc_shipping()

### generate a random value
## - https://docs.python.org/3/py-modindex.html#cap-p
import random
#
# for i in range(3):
#     print(random.random())
#     print(random.randint(10,20))
#
# members = ['Naruto', 'Itachi', 'Minato', 'Jiraiya', 'Kakashi', 'shisui']
# nextHokage = random.choice(members)
# print('Next Hokage '+nextHokage)

### File and Directories  - generated Object is a advance topic

from pathlib import Path
# Absolute Path
# EX :- C:\Users\akilw\PycharmProjects\pythonProject
# Relative Path

# path = Path('ecommerce')
# print(path.exists())

# path = Path('emails')
# print(path.mkdir())
# print(path.rmdir())

# path = Path()
# for file in path.glob('*'):
#     print(file)

