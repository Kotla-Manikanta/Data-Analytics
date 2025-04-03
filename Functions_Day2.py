# #function with return
# def add(a,b):
#     return a+b
# result=add(5,2)
# print(result)

# #function with parameters
# def greet(name):
#     print("hello",name)
# greet("kmk")

# #default parameters
# def greet(name="kmk"):
#     print("hello",name)
# greet()

# #function with multiple return values
# def details():
#     name="kmk"
#     age=24
#     return name, age
# n,a=details()
# print("name:",n,"age:",a)

# #function with multiple arguments 
# def add(*num):
#     return sum(num)
# print(add(1,2,3,4,5))

# #function with keywords arguments
# def dict(**details):
#     for i,j in details.items():
#         print(i,":",j)
# dict(name="kmk",age=25,city="new york")

#arrays
# import array 
# fruits=array.array('u',"apple banana")
# print(fruits[0])

import array 
fruits=array.array('i',[1,2,3,4,5])
length=len(fruits)
print(length)