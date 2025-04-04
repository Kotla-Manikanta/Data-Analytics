# Inner functions
# def fun1(msg):
#     def fun2():
#         print(msg)
#     fun2()
# fun1('hello')

# CLASS AND OBJECT
# class Dog:
#     sound='bark'
# d=Dog()
# print(d.sound)

# __init__ method
# class Dog:
#     species='Lab'
    
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# d=Dog('Leo',2)
# print(d.name)
# print(d.species)
# print(d.age)

# # __init__ and __str__ method(tostring=called automatically like init)
# class Dog:
#     species='Lab'
    
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
#     def __str__(self):
#         return f"{self.name} is {self.age} months old"
# d=Dog('Leo',2)
# d2=Dog('sunny',12)
# print(d)
# print(d2)

# # instance variable and class variable
# class Dog:
#     species='Lab'
    
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# d=Dog('Leo',2)
# d1=Dog('max',10)
# print(d.name)
# print(d.species)
# print(d2.age)

# #modify instance variables
# d.name='charlie'
# print(d.name)

# #modify class variables
# Dog.species='canine'
# print(d.species)

#Inheritance
# class Animal:
#     def __init__(self,name):
#         self.name=name
        
#     def sound(self):
#         pass

# class Dog(Animal):
#     def sound(self):
#         return "woof"

# a=Animal('Generic animal')  #init method
# d=Dog('Buddy')

# print(a.name)
# print(d.name)
# print(d.sound())

# Class with Inner class
# class color:
#     def __init__(self):
#         self.name="green"
#         self.lg=self.lightgreen()    #inner class invocation
    
#     def show(self):
#         print('name:',self.name)
        
#     class lightgreen:               #inner class created with name light green
#         def __init__(self):
#             self.name='light green'
#             self.code='021ovac'
        
#         def display(self):
#             print('name:',self.name)
#             print('code:',self.code)

# outer = color()    #outer class object creation
# outer.show()       #outer class method invocation

# g=outer.lg       #inner class object creation
# g.display()      #inner class method calling

#super class
# class A:
#     def show(self):
#         print('parent class')
    
# class B(A):
#     def show(self):
#         super().show()
#         print('child class')

# obj=B()
# obj.show()

#private access modifier
# class A:
#     def __init__(self):
#         self.__salary=5000
    
#     def salary(self):
#         return self.__salary

# obj=A()
# print(obj.salary())
# print(obj.__salary)  # raises attribute error

#protected
# class A:
#     def __init__(self):
#         self._salary=5000
    
#     def salary(self):
#         return self._salary

# obj=A()
# print(obj.salary())
# print(obj._salary) 

# Iterators 
# a=[1,2,3,4,5,6]
# i=iter(a)
# print(next(i))  #op:1
# print(next(i))  #op:2

#local scope 
# def func():
#     x=20
#     print(x)
# func()

#enclosing scope 
# def func():
#     x=20
#     def innerfunc():
#         print(x)
#     innerfunc()
# func()

#global scope 
# x=20
# def func():
#     print(x)
# func()
# print(x)

