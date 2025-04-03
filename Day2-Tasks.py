# 1.String functions
# str="Hello world"
# up=str.upper() #converts all char into capital 
# print(up)
# lwr=str.lower() #converts all char into small 
# print(lwr)
# swp=str.swapcase()  #converts small to capital and vice vera
# print(swp)
# split=str.split()
# print(split)
# length = len(str)  # Get length of string
# print(length)
# find=str.find("world") #finds the index of specific word
# print(find)


# 2.List Functions
# list=[1,'b',222,5.6,'kmk']
# list.append(999)  #add the new element
# print(list)
# list.pop()  #remove last element
# print(list)
# list.remove('b') #remove specific element
# print(list)
# list.reverse()  #reverse
# print(list)
# list[0] = 555  #update the existing element using index
# print(list)
# list.insert(0,222)  #add element at specific index
# print(list)
# list.sort()   #sort the list in ascending
# print(list)
# list.sort(reverse=True)   #sort the list in descending
# print(list)
# count=list.count(222)  #count the specific element
# print(count)
# length=len(list)  #gives length of list
# print(length)
# list.clear() #removes all elements in list and gives empty list
# print(list)


# 3.Tuple Functions
# tuple = (1, 'b', 222, 5.6, 'kmk')
# count = tuple.count(222)  # Count occurrences of an element
# print(count)
# index= tuple.index('kmk')  # Find index of a specific element
# print(index)
# length = len(tuple)  # Get length of tuple
# print(length)


# 4.Grading using marks
# marks = int(input("Enter your marks: "))
# if 90 <= marks <= 100:
#     print("Grade A")
# elif 70 <= marks <= 89:
#     print("Grade B")
# elif 60 <= marks <= 69:
#     print("Grade C")
# else:
#     print("Fail")


# 5.Reverse a string and check whether it is palindrome
# str=input("enter the string:")
# rev=""
# for i in str:
#     rev=i+rev
# print(rev)
# if str==rev:
#     print("given string is palindrome")
# else:
#     print("given string is not palindrome")


# 6.check given num is prime or not
# num=7
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count+=1
# if count==2:
#     print("given number is prime")
# else:
#     print("given number is not prime")


# 7.Fibonacci series
# n=int(input("enter n:"))
# a=0
# b=1
# for i in range(n):
#     print(a,end=" ")
#     a,b=b,a+b


# 8.check given num is even or not
# num=int(input("enter the num:"))
# if num%2==0:
#     print("given num is even")
# else:
#     print("given num is odd")


# 9.get num from user and check given num is prime or not
# num=int(input("enter the num:"))
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count+=1
# if count==2:
#     print("given number is prime")
# else:
#     print("given number is not prime")


# 10. print num from 1-100 and change even num to @
# for i in range(1,101):
#     if i%2==0:
#         print("@",end=" ")
#     else:
#         print(i,end=" ")


# 11.collection iterate each element and square
# num=[1,2,3,4,5]
# for i in num:
#     print(i*i,end=" ")


# 12. Print keys from dictionary and based on keys the values should display
# a={'name':'kmk','age':25}
# for i,j in a.items():
#     print("key:",i,"Value:",j)


# 13.get the user details from the user and next function is to display the value whatever we got from the user
# def details():
#     username=input("enter the username:")
#     age=int(input("enter the age:"))
#     address=input("enter the address:")
#     display(username,age,address)
# def display(username,age,address):
#     print(username,age,address)
# details()