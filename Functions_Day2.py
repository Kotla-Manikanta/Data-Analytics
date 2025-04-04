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

# import array 
# fruits=array.array('i',[1,2,3,4,5])
# length=len(fruits)
# print(length)

# lambda functions
# s1='Hello world'
# s2=lambda func:func.upper()
# print(s2(s1))
# n=lambda x:'positive' if x>0 else 'negative' if x<0 else 'zero'
# print(n(-4))
# print(n(5))
# print(n(0))
# sq=lambda x:x*x
# print(sq(5))
# l1=[lambda arg=x:arg * 10 for x in range(1,5)]
# for i in l1:
#     print(i())
# lambda with multiple arguments
cal=lambda x,y:(x+y,x*y,x-y)
res=cal(10,5)
print(res)
# filter
n=[1,2,3,4,5]
even=filter(lambda x: x%2==0,n)
print(list(even))
#map
n=[1,2,3,4,5]
sq=map(lambda x: x*2,n)    # Iterate through collection and apply transformation
print(list(sq))
#reduce
from functools import reduce
n=[1,2,3,4,5]
b=reduce(lambda x,y:x*y,n)
print(b)
#fstring
a=10
print(f'she is {a} years old')
b='she is {} years old'.format(a)
print(b)