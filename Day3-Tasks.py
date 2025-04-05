# 1.programs for all types of inheritance
# single inheritance
# class Animal:
#     def speak(self):
#         return "Some sound"

# class Dog(Animal):
#     def walk(self):
#         return "yes"

# d=Dog()
# print(d.speak())
# print(d.walk())

# multilevel inheritance
# class Grandparent:
#     def legacy(self):
#         print("Legacy from Grandparent")

# class Parent(Grandparent):
#     def teach(self):
#         print("Parent teaches")

# class Child(Parent):
#     def play(self):
#         print("Child plays")
# c = Child()
# c.legacy()
# c.teach()
# c.play()

# Hierarchial inheritance
# class Vehicle:
#     def start(self):
#         print("Vehicle starts")

# class Car(Vehicle):
#     def drive(self):
#         print("Car is driving")

# class Bike(Vehicle):
#     def ride(self):
#         print("Bike is riding")

# car = Car()
# bike = Bike()

# car.start()
# car.drive()

# bike.start()
# bike.ride()

#multiple inheritance
# class Father:
#     def farming(self):
#         print("Father knows farming")

# class Mother:
#     def cooking(self):
#         print("Mother knows cooking")

# class Child(Father, Mother):
#     def study(self):
#         print("Child studies")

# c = Child()
# c.farming()
# c.cooking()
# c.study()

# 2.Encapsulation  all the modifiers
#public
# class A:
#     def __init__(self,name):
#         self.name=name
# a=A('kmk')
# print(a.name)

#private
# class A:
#     def __init__(self,name):
#         self.__name=name
#     def getname(self):
#         return self.__name
# a=A('kmk')
# print(a.__name)

#protected
# class A:
#     def __init__(self,name):
#         self._name=name
# a=A('kmk')
# print(a._name)

# 3.polymorphism - method overloading and method overriding
#method overriding
# class Animal:
#     def speak(self):
#         return "Some sound"

# class Dog(Animal):
#     def speak(self):
#         return "Bark"

# class Cat(Animal):
#     def speak(self):
#         return "meo"

# a = Animal()
# d = Dog()
# c = Cat()

# print(a.speak())
# print(d.speak())
# print(c.speak())

